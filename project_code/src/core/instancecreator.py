from parser import UserInputParser, EventInputParser
from user import User

class InstanceCreator:

    def __init__(self):
        self.user_parser = UserInputParser()
        self.event_parser = EventInputParser()

    def _new_user_or_login(self):
        response = input("Create a new username or login to an existing account? ")
        if "login" in response:
            return self._load_user()
        else:
            return self._create_user()

    def get_user_info(self, response: str):
        if "yes" in response:
            return self._new_user_or_login()
        else:
            return None

    def _load_user(self):
        username = input("Enter your username: ")
        # Assuming you have a method to retrieve user data from the database
        user_data = database.get_user_data(username)
        if user_data:
            # Assuming User is a class that represents a user
            return User(user_data)  # Create a User object using the retrieved data
        else:
            print("User not found.")
            # You might handle this differently based on your application's requirements
            return None

    def _create_user(self):
        # Assuming you have a method to create a new user
        user_data = self.user_parser.parse_user_data()  # Assuming UserInputParser has a method to parse user data
        return User.create(user_data)  # Assuming User has a class method to create a new user