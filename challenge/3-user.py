#!/usr/bin/env python3
"""
User class implementation with password validation
"""

class User:
    """User class for managing user information and password validation"""
    
    def __init__(self):
        """Initialize a new user with default values"""
        self.__email = None
        self.__password = None
        self.reset_session()

    @property
    def email(self):
        """Getter for email"""
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email"""
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value

    @property
    def password(self):
        """Getter for password"""
        return self.__password

    @password.setter
    def password(self, value):
        """Setter for password"""
        if not isinstance(value, str):
            raise TypeError("password must be a string")
        self.__password = value

    def reset_session(self):
        """Reset the user's session"""
        self.__session_id = None

    def is_valid_password(self, pwd):
        """Check if the provided password matches the user's password"""
        if not isinstance(pwd, str):
            return False
        if self.__password is None:
            return False
        return pwd == self.__password


if __name__ == "__main__":
    print("Test User")
    u = User()
    u.email = "test@test.com"
    u.password = "test"
    print("is_valid_password should return True if it's the right password")
    print(u.is_valid_password("test"))
