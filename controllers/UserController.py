from models.entities.User import User
from services.UserServicesMem import UserServiceMem

class UserController:
    def __init__(self, service:UserServiceMem):
        self.__SERVICE:UserServiceMem = service

    def login(self, username:str, password:str) -> bool:
        return self.__SERVICE.login(username, password)
        
    def create_user(self, user:User) -> bool:
        return self.__SERVICE.create_user(user)
    
    def exists(self, user:str) -> bool:
        return self.__SERVICE.exists(user)
    
    def toString(self):
        self.__SERVICE.toString()