import json
import os
import random
import string
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key_file="secret.key", data_file="passwords.json"):
        self.key_file = key_file
        self.data_file = data_file
        self.key = self.load_key()
        self.fernet = Fernet(self.key)
        self.passwords = self.load_passwords()

    def load_key(self):
        """Load the encryption key from a file or generate a new one."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            return key

    def load_passwords(self):
        """Load passwords from the JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_passwords(self):
        """Save passwords to the JSON file."""
        with open(self.data_file, "w") as f:
            json.dump(self.passwords, f, indent=4)

    def encrypt(self, text):
        """Encrypt a string."""
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, encrypted_text):
        """Decrypt an encrypted string."""
        return self.fernet.decrypt(encrypted_text.encode()).decode()

    def add_password(self, site, username, password):
        """Add a new password for a site."""
        encrypted_password = self.encrypt(password)
        self.passwords[site] = {
            "username": username,
            "password": encrypted_password
        }
        self.save_passwords()
        print(f"Password for {site} saved successfully!")

    def get_password(self, site):
        """Retrieve and decrypt a password for a site."""
        if site in self.passwords:
            entry = self.passwords[site]
            decrypted_password = self.decrypt(entry["password"])
            return entry["username"], decrypted_password
        return None

    def list_sites(self):
        """List all sites stored in the manager."""
        return list(self.passwords.keys())

    def generate_password(self, length=16):
        """Generate a secure random password."""
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for i in range(length))

def main():
    manager = PasswordManager()
    
    while True:
        print("\n--- Password Manager ---")
        print("1. Add New Password")
        print("2. Retrieve Password")
        print("3. List All Sites")
        print("4. Generate Secure Password")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            site = input("Enter website name: ")
            username = input("Enter username: ")
            gen_choice = input("Generate a password? (y/n): ").lower()
            if gen_choice == 'y':
                password = manager.generate_password()
                print(f"Generated Password: {password}")
            else:
                password = input("Enter password: ")
            manager.add_password(site, username, password)
            
        elif choice == "2":
            site = input("Enter website name: ")
            result = manager.get_password(site)
            if result:
                username, password = result
                print(f"Username: {username}")
                print(f"Password: {password}")
            else:
                print("Site not found.")
                
        elif choice == "3":
            sites = manager.list_sites()
            if sites:
                print("\nStored Sites:")
                for site in sites:
                    print(f"- {site}")
            else:
                print("No passwords stored yet.")
                
        elif choice == "4":
            try:
                length = int(input("Enter desired password length (default 16): ") or 16)
                print(f"Generated Password: {manager.generate_password(length)}")
            except ValueError:
                print("Invalid input. Using default length 16.")
                print(f"Generated Password: {manager.generate_password()}")
                
        elif choice == "5":
            print("Exiting Password Manager. Stay secure!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
