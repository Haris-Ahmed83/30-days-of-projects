# Day 03 - Password Manager

## Project Description

This project is a secure command-line Password Manager built with Python. It allows users to store, retrieve, and generate strong passwords. To ensure security, all passwords are encrypted using the `cryptography` library's Fernet symmetric encryption, and the encryption key is stored locally in a separate file.

## Features

*   **Secure Storage**: Passwords are encrypted before being saved to a JSON file.
*   **Password Retrieval**: Decrypts and displays passwords for specific websites.
*   **Automatic Generation**: Generates high-entropy, random passwords of custom lengths.
*   **Site Management**: Lists all websites for which credentials have been saved.
*   **Data Persistence**: Uses `passwords.json` for storage and `secret.key` for encryption.

## Security Note

This application uses a local `secret.key` file. **Never share this key** or upload it to a public repository if you intend to use this manager for real passwords. For the purpose of this challenge, the key file is generated on the first run.

## How to Run

1.  **Navigate to the project directory**:

    ```bash
    cd "Day_03_Password_Manager"
    ```

2.  **Install dependencies**:

    ```bash
    pip install cryptography
    ```

3.  **Run the password manager**:

    ```bash
    python3 password_manager.py
    ```

## Usage

Upon running the script, you can choose from the following options:

1.  **Add New Password**: Store a username and password for a new site (option to generate one).
2.  **Retrieve Password**: View the credentials for a stored site.
3.  **List All Sites**: See which sites are currently in your database.
4.  **Generate Secure Password**: Create a random string for use elsewhere.
5.  **Exit**: Safely close the application.
