class User:
    def __init__(self, username, email, password):
        self.username = username
        self.password = password

    def login(self, entered_username, entered_password):
        if entered_username == self.username and entered_password == self.password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password. Please try again.")
            return False

    def logout(self):
        print("Logged out.")

    def update_profile(self, new_data):
        for key, value in new_data.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Attribute '{key}' does not exist in the user profile.")
