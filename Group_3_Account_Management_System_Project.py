import os
from datetime import datetime
import random
import string
import unicodedata


# ============================================================
# Helper Functions
# ============================================================
#Aykut
def unicoder(text: str) -> str:
    """Removes accents and special characters.
    """
    return unicodedata.normalize("NFKD", text)\
        .encode("ASCII", "ignore")\
        .decode("utf-8")\
        .strip()


def username_suggester(name: str, surname: str, existing_usernames: list):
    """Generates two unique username suggestions."""
    name = unicoder(name).lower()
    surname = unicoder(surname).lower()

    variants = [
        f"{name}.{surname}",
        f"{name}_{surname}",
        f"{name}{surname}",
        f"{surname}.{name}",
        f"{name}{surname[0]}",
        f"{name[0]}_{surname}",
        f"{name}{random.randint(1, 99)}",
        f"{name}_{random.randint(10, 99)}"
    ]

    existing_usernames_lower = [usnam.lower() for usnam in existing_usernames]
    random.shuffle(variants)

    suggestions = []
    for sug in variants:
        if sug.lower() not in existing_usernames_lower and sug not in suggestions:
            suggestions.append(sug)
        if len(suggestions) == 2:
            break

    while len(suggestions) < 2:
        sug = f"{name}{random.randint(100,999)}"
        if sug.lower() not in existing_usernames_lower:
            suggestions.append(sug)

    return suggestions


def password_strength(password: str) -> bool:
    """Checks password strength."""
    has_letter = has_digit = has_symbol = False

    for pas in password:
        if pas.isalpha():
            has_letter = True
        elif pas.isdigit():
            has_digit = True
        elif not pas.isspace():
            has_symbol = True

    return len(password) >= 8 and has_letter and has_digit and has_symbol


def check_username_exists(username: str, filepath: str) -> bool:
    """Checks if username already exists."""
    if not os.path.exists(filepath):
        return False

    with open(filepath, "r", encoding="utf-8") as accfile:
        for line in accfile:
            if line.split("|")[0].lower() == username.lower():
                return True
    return False
#Aykut

# ============================================================
# Core Functions
# ============================================================
#Zeljko
def create_account(filepath: str):
    """Creates a new user (MASTER only)."""

    existing_usernames = []
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as accfile:
            existing_usernames = [line.split("|")[0] for line in accfile]

    name = input("Enter your first name: ").strip()
    surname = input("Enter your last name: ").strip()

    suggestions = username_suggester(name, surname, existing_usernames)

    print("\nHere are some username suggestions:")
    print(f"1. {suggestions[0]}")
    print(f"2. {suggestions[1]}")
    print("3. I want to choose my own username")

    while True:
        choice = input("Choose (1/2/3): ").strip()
        if choice in {"1", "2"}:
            username = suggestions[int(choice) - 1] # index number starts with 0 that's why -1
            break
        elif choice == "3":
            username = input("Enter username: ").strip().lower()
            if check_username_exists(username, filepath):
                print("Username already exists.")
            else:
                break
        else:
            print("Invalid choice.")

    print(f"\nSelected username: {username}")

    while True:
        pw_choice = input(
            "\n1. Generate a strong password\n"
            "2. Choose my own password\n"
            "Choice (1/2): "
        ).strip()

        if pw_choice == "1":
            chars = string.ascii_letters + string.digits + string.punctuation.replace("|", "")
            password = "".join(random.choice(chars) for _ in range(12))
            print(f"Generated password: {password}")
            break

        elif pw_choice == "2":
            password = input("Enter password: ").strip()
            if password_strength(password):
                print("Password is strong. Logging in...")
                break
            else:
                print(
                    "Weak password.\n"
                    "A strong password must contain:\n"
                    "- at least one letter\n"
                    "- one digit\n"
                    "- one symbol\n"
                )
        else:
            print("Invalid choice. \n Please press 1 to have a generated Password or " \
            "\n Press 2 to write your own password")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{username}|MASTER|{password}|{timestamp}\n") #Username and Master pass recorded after the first log in. 

    print("\nUser created successfully.")
    print("Please log in, to save accounts.\n")
#Zeljko 
#Yücel
def login(filepath: str):
    """User login."""

    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if not os.path.exists(filepath):
        print(
            "User not found.\n"
            "Please choose:\n"
            "2 - Create New Account\n"
            "3 - Exit"
        )
        return

    with open(filepath, "r", encoding="utf-8") as accfile:
        for line in accfile:
            parts = line.strip().split("|")
            if len(parts) < 4:
                continue

            user, tag, stored_pass = parts[0], parts[1], parts[2]

            if user.lower() == username and tag == "MASTER":
                if stored_pass == password:
                    print(f"\nWelcome {username}!")
                    view_accounts(username, filepath)
                    return
                else:
                    print("Incorrect password. Please control your password!")
                    return

    print("User not found. Try again.")
#Yücel
#Aykut
def add_account(username: str, filepath: str):
    """Adds a new service account."""

    account_name = input("Account name (e.g. Facebook, Gmail, Twitter or etc.): ").strip().lower()
    account_password = input("Account password: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as accfile:
        accfile.write(f"{username}|{account_name}|{account_password}|{timestamp}\n")

    print(f"Account '{account_name}' added.")

def view_accounts(username: str, filepath: str):
    """Shows user accounts, allows viewing, adding new ones, or exiting."""

    while True:

        accounts = []
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if parts[0] == username and parts[1] != "MASTER":
                    accounts.append(parts)

        # -------- NO ACCOUNTS --------
        if not accounts:
            print("\nYou do not have any account yet.")
            print("A. Add a new account")
            print("Q. Logout")

            choice = input("Choose: ").strip().lower()

            if choice == "a":
                add_account(username, filepath)
                continue
            elif choice == "q":
                print("Logged out.\n")
                return
            else:
                print("Please enter A or Q.")
                continue

        # -------- ACCOUNTS EXIST --------
        print("\nYour saved accounts are:")
        i = 1
        for acc in accounts:
            print(f"{i}. {acc[1].title()}")
            i += 1

        print("A. Add another account")
        print("Q. Exit")

        choice = input("\nPlease select an option: ").strip().lower()

        # ---- EXIT ----
        if choice == "q":
            print("Logged out.\n")
            return

        # ---- ADD ACCOUNT ----
        if choice == "a":
            add_account(username, filepath)
            continue

        # ---- VIEW PASSWORD ----
        if not choice.isdigit():
            print("Please enter a valid number, A, or Q.")
            continue

        choice = int(choice)

        if 1 <= choice <= len(accounts):
            selected = accounts[choice - 1]
            print(f"\nPassword for {selected[1].title()}: {selected[2]}")
            print(f"Created on: {selected[3]}")
            # come back to the list
            continue
        else:
            print("Invalid selection.")

#Aykut
#Yücel

# ============================================================
# Main Menu
# ============================================================

def main_menu():
    filepath = "accounts.txt" #accfile
    print("=== Welcome to Account Management System! ===\n")

    while True:
        print("Please make a choice")
        print("1. Login")
        print("2. Create New Account")
        print("3. Exit\n")

        choice = input("Choose (1/2/3): ").strip()

        if choice == "1":
            login(filepath)
        elif choice == "2":
            create_account(filepath)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. To Login Press 1, To Create new account Press 2 or to Exit press 3\n")


# ============================================================
# Program Start
# ============================================================

if __name__ == "__main__":
    main_menu()
# Yücel