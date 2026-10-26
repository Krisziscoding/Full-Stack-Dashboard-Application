# Example Python Code to Insert a Document

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None, host='localhost', port=27017, db='aac', col='animals'):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is hard-wired to use the aac
        # database, the animals collection, and the aac user.
        #
        # You must edit the password below for your environment.
        #
        # Connection Variables
        # Use passed parameters or fall back to default values
        USER = username if username else 'aacuser'
        PASS = password if password else 'InsertWittyPasswordHere'
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

        # Create a method to return the next available record number for use in the create method


    def create(self, data):
        """
        Inserts a single document (dictionary) into the animals collection.
        
        Parameters:
            data (dict): A dictionary containing the animal's record to insert.
            
        Returns:
            bool: True if the insertion was successful, False otherwise.
        """
        try:
            # Check if data is a dictionary
            if not isinstance(data, dict):
                raise TypeError("Data parameter must be a dictionary.")
            
            # Check if dictionary is empty
            if not data:
                raise ValueError("Data dictionary cannot be empty.")
                
            self.database.animals.insert_one(data)
            print("Document successfully inserted!")
            return True
                
        except Exception as e:
            # Catch and log any insertion errors
            print(f"Error occurred while inserting document: {e}")
            return False

    def read(self, data):
        """
        Queries and retrieves documents from the animals collection.
        
        Parameters:
            data (dict): A dictionary representing the query filter.
            
        Returns:
            list: A list of matching documents, or an empty list if an error occurs.
        """
        try:
            # Check if data is a dictionary
            if not isinstance(data, dict):
                raise TypeError("Data parameter must be a dictionary.")
            
            # NOTE: Empty dictionaries are intentionally allowed here in case 
            # the user wants to return the entire collection.
            
            # Execute find query and convert the cursor to a list
            result = list(self.database.animals.find(data))
            return result
            
        except Exception as e:
            # Catch and log any query execution errors
            print(f"Error occurred while reading document: {e}")
            return []

    def update(self, data, query):
        """
        Updates documents matching the query with the new data using the $set operator.
        
        Parameters:
            data (dict): The fields and new values to update.
            query (dict): The filter criteria to find the target documents.
            
        Returns:
            int: The number of documents modified.
        """
        try:
            # Check if data is a dictionary and not empty
            if not isinstance(data, dict):
                raise TypeError("Data parameter must be a dictionary.")
            if not data:
                raise ValueError("Data dictionary cannot be empty.")
                
            # Check if query is a dictionary
            if not isinstance(query, dict):
                raise TypeError("Query parameter must be a dictionary.")
                
            # NOTE: Empty dicts are intentionally allowed for queries in case there is a need for mass updates.
            
            # Apply updates to matching documents
            result = self.database.animals.update_many(query, {"$set": data})
            return result.modified_count
            
        except Exception as e:
            # Catch and log any update errors
            print(f"Error occurred while updating document: {e}")
            return 0

    def delete(self, query):
        """
        Deletes one or more documents matching the query from the animals collection.
        
        Parameters:
            query (dict): The filter criteria to find the documents to delete.
            
        Returns:
            int: The number of documents deleted.
        """
        try:
            # Check if query is a dictionary
            if not isinstance(query, dict):
                raise TypeError("Query parameter must be a dictionary.")
                
            # Check if query dictionary is empty
            if not query:
                raise ValueError("Query dictionary cannot be empty.")
                
            # Delete documents matching the search query
            result = self.database.animals.delete_many(query)
            return result.deleted_count
            
        except Exception as e:
            # Catch and log any deletion errors
            print(f"Error occurred while deleting document: {e}")
            return 0