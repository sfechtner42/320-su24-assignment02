'''
Classes for user information for the social network project
'''
# pylint: disable=R0903
import sys
from loguru import logger


# set-up logging for user_status.py
logger.remove()
logger.add("log_file_{time:YYYY_MMM_DD}.log")
logger.add(sys.stderr, level='ERROR')
# logger.info("users.py is imported")
# logger.error("Problem here users.py")
# logger.debug("Debug here users.py")


class Users():
    '''
    Contains user information
    '''

    def __init__(self, user_id, email, user_name, user_last_name):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.user_last_name = user_last_name
        logger.debug("User Class initialized")


class UserCollection():
    '''
    Contains a collection of Users objects
    '''

    def __init__(self):
        self.database = {}

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        if user_id in self.database:
            # Rejects new status if status_id already exists
            logger.debug("User already exists")
            return False
        new_user = Users(user_id, email, user_name, user_last_name)
        self.database[user_id] = new_user
        logger.debug("User added successfully")
        return True

    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''
        if user_id not in self.database:
            logger.debug("User not modified-does not exist")
            return False
        self.database[user_id].email = email
        self.database[user_id].user_name = user_name
        self.database[user_id].user_last_name = user_last_name
        logger.debug("User modified successfully")
        return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        if user_id not in self.database:
            logger.debug("User not deleted/does not exist")
            return False
        del self.database[user_id]
        logger.debug("User deleted successfully")
        return True

    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        if user_id not in self.database:
            return Users(None, None, None, None)
        logger.debug(f"{user_id} searched and found")
        return self.database[user_id]
