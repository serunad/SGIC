from services.LoginServicesMem import LoginServiceMem

class LoginController:
    def __init__(self, service:LoginServiceMem):
        self.__SERVICE:LoginServiceMem = service

    def login(self, username:str, password:str):
        return self.__SERVICE.login(username, password)