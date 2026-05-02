from models.entities.User import User
from models.repository.UserMemRepository import UserMemRepository

class UserServiceMem:
    """
    Service to methods of user
    """
    def __init__(self, repository:UserMemRepository):
        self.__REPOSITORY:UserMemRepository = repository
        
    def create_user(self, user:User) -> bool:
        return self.__REPOSITORY.add_user(user)
    
    def exists(self, user:str) -> bool:
        return self.__REPOSITORY.exists(user)
    
    def toString(self):
        self.__REPOSITORY.toString()