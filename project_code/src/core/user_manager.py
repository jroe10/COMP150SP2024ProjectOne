import hashlib
import secrets

class UserManager:
    def __init__(self):
        self.users = {}  # Simulated database

    def register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        
        if username in self.users:
            print("Username already exists.")
            return False
        else:
            salt = secrets.token_hex(16)  # Generate a random salt
            hashed_password = self._hash_password(password, salt)
            self.users[username] = {'password': hashed_password, 'salt': salt}
            print("User registered successfully.")
            return True

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
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