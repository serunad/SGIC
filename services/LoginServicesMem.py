from models.entities.User import User
from models.repository.UserMemRepository import UserMemRepository

class LoginServiceMem:
    """
    Service to methods of user
    """
    def __init__(self, repository:UserMemRepository):
        self.__REPOSITORY:UserMemRepository = repository

    def login(self, username:str, password:str) -> bool:
        user: User = self.__REPOSITORY.find_user(username)

        if user is None:
            return False
        else:
            return user.validate(username, password)