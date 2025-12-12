

# Password Generator - BIT2025
Group Project (Aykut, Yücel, Zeljko)

This document describes the project scenario, user flow, example workflow, and data structure of the Password Manager Application developed as part of the Programming Foundations module.

The project demonstrates core Python concepts such as user interaction, data validation, and file processing through a console-based application.

1. Project Scenario

Our group project is a console-based Password Manager Application written in Python.
The goal of the application is to allow users to:

Create a user account with a username and master password

Log in securely

Generate and store passwords for different online services

Retrieve stored passwords when needed

The application is designed for educational purposes and focuses on clear logic and beginner-friendly code structure.

2. Assignment Requirements Fulfilled

The project fulfills all three core requirements of the assignment:

Interactive Application
The program interacts with the user via the console using menus and input prompts.

Data Validation
User inputs such as passwords and usernames are validated (minimum length, required characters, etc.).

File Processing
All user and account data is stored in and retrieved from a text file (accounts.txt).

3. User Flow
Step 1 – Create New User Account

The user enters their first name and last name.

The program generates two available username suggestions.

The user selects one of the suggested usernames or enters a custom one.

The user creates a master password:

Minimum 8 characters

Must contain letters, digits, and special characters

The user can also let the program generate a strong password automatically.

The user account is saved to a file.

Step 2 – Login

The user logs in using their username and master password.

If the credentials match the stored data, access is granted.

Step 3 – Main Menu

After logging in, the following options are available:

Add a new account
Store a password for a service such as Facebook, Gmail, or Instagram.

View saved account passwords
Display stored accounts and retrieve their passwords.

Log out
Exit the current user session.

Step 4 – Adding a New Account

The user enters the account name (e.g., Facebook, Twitter).

The password for the account is entered manually.

A timestamp is automatically added.

The data is saved to the file.

Step 5 – Viewing Saved Accounts

The user sees a list of saved accounts.

Each account displays its creation date.

The user can select an account to view its password.

4. Example Workflow

Create User Account

Name: Ali Yılmaz

Suggested usernames: ali.yilmaz, yilmaz_ali

Master password: A1i!Pass99

Login

Username: ali.yilmaz

Password: A1i!Pass99

Add New Account

Account name: Instagram

Password: Gm@7x!Qr1Z

Retrieve Password

User selects Instagram from the list

Password Gm@7x!Qr1Z is displayed

5. File Structure

All data is stored in a text file named accounts.txt.

Each line represents one saved record using the following format:

username|master_password|account_name|account_password|timestamp

Example:
ali.yilmaz|A1i!Pass99|instagram|Gm@7x!Qr1Z|2025-09-26 14:15:22

6. Notes

This project is intended for learning purposes only.

Passwords are stored in plain text and are not encrypted.

In a real-world application, passwords would be hashed and stored securely in a database.