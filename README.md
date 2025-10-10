# Password-Generator---BIT2025


PASSWORD GENERATOR - Group Project(Aykut, Yücel, Zeljko)

This document presents the project scenario, user flow, example workflow, and data structure for the 'Password Generator' Python application. The project is part of the Programming Foundations module and demonstrates user interaction, data validation, and file processing capabilities.
1. Project Scenario
Our team project is a Password Manager Application developed in Python. The goal is to create a console-based program that allows users to securely manage their passwords by registering with an email and master password, generating strong passwords for different accounts, storing them in a file, and retrieving them when needed.

The project fulfills all three core requirements of the assignment:
- Interactive Application: Processes user input (email, password, menu options) through the console.
- Data Validation: Checks input formats (valid email, password length, character requirements, etc.).
- File Processing: Stores and retrieves user and password data from a text file.
2. User Story & Flow
Step 1 – Registration (Sign-up)
- The user enters an email address. The program validates it (must contain '@'). 
- The user is asked to re-enter the email to confirm. If they don’t match, the program asks again.
- Next, the user chooses a master password, which is entered twice to ensure accuracy.
- The password strength is checked. It must be at least 6 characters long and contain letters, digits, and special symbols.
- Once a strong password is chosen, the account is saved to a file (accounts.txt).
Step 2 – Login
- When the user returns, they must log in with their email and master password.
- If the credentials match, they gain access to the main application.
Step 3 – Main Menu
After login, the main menu appears:
1.	Add a new account – For example, create a password for a service like Instagram, Amazon, or Gmail.
2.	View saved passwords – List all stored accounts and their passwords.
3.	Exit – Log out of the application.
Step 4 – Adding a New Account
- The program generates a strong random password based on predefined criteria (length, symbols, etc.).
- The user can accept the password, which will then be stored along with the account name and timestamp in the text file.
Step 5 – Viewing and Selecting a Password
- The user can view all previously saved accounts.
- Each password is listed with a number.
- The user selects the number of the password they want to use, and the program displays it on the screen.
3. Example Workflow (User Scenario)
1.	Registration:
   - Email: ali@example.com
   - Master password: A1i!Pass
2.	Login:
  - Ali enters his email and master password.
3.	Add new account:
  - Ali chooses to add a password for Instagram.
  - The system suggests: Gm@7x!Qr1Z.
  - Password is saved.
4.	Retrieve password:
  - Ali logs in later and selects Instagram from the list.
  - Password Gm@7x!Qr1Z is shown for copy-paste usage.
4. File Structure
All data is stored in a text file 'accounts.txt' with the following structure:

email|site|password|timestamp

Example:
ali@example.com|MASTER|A1i!Pass|2025-09-26 14:10:05
ali@example.com|Instagram|Gm@7x!Qr1Z|2025-09-26 14:15:22
