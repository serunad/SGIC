from config.MemoryDb.InMemoryDB import InMemoryDB
from models.entities.User import User

class UserMemRepository:
    def __init__(self):
        self.__db:InMemoryDB = InMemoryDB()

    def add_user(self, user:User) -> bool:
        """
        Method to add users if they don't exist
        :param user: User class
        :return bool: True if added
        """
        if not self.exists(user.get_name()):
            self.__db.set_user(user)
            return True
        else:
            return False

    def update_user(self, user:User):
        """
        Method to update users if they exist
        :param user: User class
        :return bool: True if updated
        """
        if self.exists(user.get_name()):
            self.__db.set_user(user)
            return True
        else:
            return False
    
    def find_user(self, name:str) -> User | None:
        """
        Method to find a user saved in database
        :return users dictionary or None if not exists
        """
        return self.__db.get_user(name)
    
    def exists(self, name:str) -> bool:
        """
        Method to validate if a user exist in database
        :return True if exists
        """
        return self.__db.user_exists(name)
    
    def toString(self):
        self.__db.printer_users()