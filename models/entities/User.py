class User:
    """ This is a user class to represent a user """

    def __init__(self, name, password):
        """
        :param name: username
        :param password: user password 
        """
        self._username = name
        self._password = password

    def validate(self, user_logged_in:str, password_logged_in:str) -> bool:
        """
        Method to validate login

        :param user_logged_in: username logged in login
        :param password_logged_in: user password logged in login
        :Return bool: True is success
        """
        if self._username == user_logged_in and self._password == password_logged_in:
            return True
        else:
            return False

    def get_name(self) -> str:
        """ 
        Method to get a username
        """
        return self._username