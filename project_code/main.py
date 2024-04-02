import sys
import hashlib
import secrets
from src.core.game import Game

class UserManager:
    def __init__(self):
        self.users = {}  # Simulated database

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists.")
            return False
        else:
            salt = secrets.token_hex(16)  # Generate a random salt
            hashed_password = self._hash_password(password, salt)
            self.users[username] = {'password': hashed_password, 'salt': salt}
            print("User registered successfully.")
            return True

    def login_user(self, username, password):
        if username in self.users:
            stored_password = self.users[username]['password']
            salt = self.users[username]['salt']
            hashed_password = self._hash_password(password, salt)
            if stored_password == hashed_password:
                print("Login successful.")
                return True
        print("Invalid username or password.")
        return False

    def _hash_password(self, password, salt):
        # Hash the password with the salt using SHA-256
        hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
        return hashed_password

class User:
    def __init__(self, username):
        self.username = username
        self.current_game = None

    def save_game(self):
        # Implement saving game data
        pass

class UserInputParser:
    def parse(self, prompt):
        return input(prompt)

def start_game():
    """Entry point for starting the game."""
    parser = UserInputParser()
    user_manager = UserManager()

    response = parser.parse("Would you like to start a new game? (yes/no) ")
    if response.lower() == "yes":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if user_manager.login_user(username, password):
            print("Welcome back, {}!".format(username))
            # Start the game logic
            start(username)
        else:
            print("Login failed. Creating a new account.")
            if user_manager.register_user(username, password):
                print("Account created successfully. Starting the game.")
                # Start the game logic
                start(username)
            else:
                print("Failed to create an account. Exiting.")
                sys.exit()
    else:
        print("Goodbye!")
        sys.exit()

def start(username):
    """Starts the game for the specified user."""
    print(f"Welcome to the game, {username}!")
    while True:
        choice = input("What would you like to do? (1) Play (2) Save and Quit: ")
        if choice == "1":
            play_game(username)
        elif choice == "2":
            save_game(username)
            print("Game saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter '1' to play or '2' to save and quit.")

def play_game(username):
    """Handles the game logic."""
    print("Playing the game...")

    game = Game(username)

    while True:
        choice = input("What would you like to do? (1) Continue (2) Quit: ")
        if choice == "1":
            # Continue playing the game
            pass  # Add your game logic here
        elif choice == "2":
            print("Exiting the game...")
            break  # Exit the game loop
        else:
            print("Invalid choice. Please enter '1' to continue or '2' to quit.")

def save_game(username):
    """Saves the game progress."""
    print("Saving game data...")
    # Implement game saving logic here

if __name__ == '__main__':
    username = input("Enter your username: ")
    start(username)