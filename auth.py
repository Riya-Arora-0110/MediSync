class Authenticator:
    def __init__(self):
        self.users = {"admin": "password123", "john_doe", "securepass"}

    def login(self, username, password):
        """Check if the provided credentials are correct"""
        if username in self.users and self.users[username] == password:
            return f"Login successful! Welcome, {username}"
        else:
            return "Invalid Credentials. Please try again."

if __name__ == "__main__":
    auth = Authenticator()

    print(auth.login("admin", "password123"))

    print(auth.login("admin", "wrongpassword"))