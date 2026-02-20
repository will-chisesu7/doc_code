import getpass
import hashlib
import json
import os
from datetime import datetime

USERS_FILE = "users.json"


def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return []


def save_user(user):
    users = load_users()
    users.append(user)
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login():
    print("=" * 50)
    print("           LOGIN PORTAL")
    print("=" * 50)

    try:
        name = input("\nEnter your name: ").strip()
        surname = input("Enter your surname: ").strip()

        if not name or not surname:
            print("\nError: Name and surname cannot be empty.")
            return False

        while True:
            try:
                age = int(input("Enter your age: "))
                if age <= 0:
                    print("Error: Please enter a valid age.")
                else:
                    break
            except ValueError:
                print("Error: Age must be a number.")

        country = input("Enter your country: ").strip()
        province = input("Enter your province: ").strip()

        if not country or not province:
            print("\nError: Country and province cannot be empty.")
            return False

        while True:
            password = getpass.getpass("Create a password: ")
            if len(password) < 6:
                print("Error: Password must be at least 6 characters.")
                continue
            confirm = getpass.getpass("Confirm password: ")
            if password != confirm:
                print("Error: Passwords do not match. Try again.")
            else:
                break

        print()
        print("=" * 50)

        if age < 18:
            print("ACCESS DENIED!")
            print("=" * 50)
            print(f"Sorry {name} {surname}, you must be at least 18 to access this portal.")
            print("=" * 50)
            return False
        else:
            user = {
                "name": name,
                "surname": surname,
                "age": age,
                "country": country,
                "province": province,
                "password": hash_password(password),
                "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            save_user(user)

            print("LOGIN SUCCESSFUL!")
            print("=" * 50)
            print(f"Welcome, {name} {surname}!")
            print(f"Age:      {age}")
            print(f"Country:  {country}")
            print(f"Province: {province}")
            print("Your details have been saved.")
            print("=" * 50)
            return True

    except KeyboardInterrupt:
        print("\n\nLogin cancelled.")
        return False


def view_users():
    users = load_users()
    print("\n" + "=" * 50)
    print("           REGISTERED USERS")
    print("=" * 50)

    if not users:
        print("No users registered yet.")
    else:
        for i, user in enumerate(users, start=1):
            print(f"\nUser {i}:")
            print(f"  Name:        {user['name']} {user['surname']}")
            print(f"  Age:         {user['age']}")
            print(f"  Country:     {user['country']}")
            print(f"  Province:    {user['province']}")
            print(f"  Registered:  {user['registered_at']}")

    print("\n" + "=" * 50)


def edit_user():
    users = load_users()
    print("\n" + "=" * 50)
    print("              EDIT A USER")
    print("=" * 50)

    if not users:
        print("No users registered yet.")
        print("=" * 50)
        return

    for i, user in enumerate(users, start=1):
        print(f"  {i}. {user['name']} {user['surname']} (Age: {user['age']}, Registered: {user['registered_at']})")

    print("=" * 50)

    try:
        choice = int(input("\nEnter the number of the user to edit (0 to cancel): "))
        if choice == 0:
            print("Cancelled.")
            return
        if choice < 1 or choice > len(users):
            print("Invalid selection.")
            return

        user = users[choice - 1]
        print(f"\nEditing {user['name']} {user['surname']} — press Enter to keep current value.\n")

        name = input(f"Name [{user['name']}]: ").strip()
        surname = input(f"Surname [{user['surname']}]: ").strip()

        while True:
            age_input = input(f"Age [{user['age']}]: ").strip()
            if age_input == "":
                age = user["age"]
                break
            try:
                age = int(age_input)
                if age <= 0:
                    print("Error: Please enter a valid age.")
                else:
                    break
            except ValueError:
                print("Error: Age must be a number.")

        country = input(f"Country [{user['country']}]: ").strip()
        province = input(f"Province [{user['province']}]: ").strip()

        change_password = input("Change password? (yes/no): ").strip().lower()
        if change_password in ["yes", "y"]:
            while True:
                password = getpass.getpass("New password: ")
                if len(password) < 6:
                    print("Error: Password must be at least 6 characters.")
                    continue
                confirm = getpass.getpass("Confirm new password: ")
                if password != confirm:
                    print("Error: Passwords do not match. Try again.")
                else:
                    user["password"] = hash_password(password)
                    break

        user["name"] = name if name else user["name"]
        user["surname"] = surname if surname else user["surname"]
        user["age"] = age
        user["country"] = country if country else user["country"]
        user["province"] = province if province else user["province"]

        users[choice - 1] = user
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=4)

        print(f"\nUser {user['name']} {user['surname']} has been updated.")
        print("=" * 50)

    except ValueError:
        print("Invalid input.")


def delete_user():
    users = load_users()
    print("\n" + "=" * 50)
    print("             DELETE A USER")
    print("=" * 50)

    if not users:
        print("No users registered yet.")
        print("=" * 50)
        return

    for i, user in enumerate(users, start=1):
        print(f"  {i}. {user['name']} {user['surname']} (Age: {user['age']}, Registered: {user['registered_at']})")

    print("=" * 50)

    try:
        choice = int(input("\nEnter the number of the user to delete (0 to cancel): "))
        if choice == 0:
            print("Cancelled.")
            return
        if choice < 1 or choice > len(users):
            print("Invalid selection.")
            return

        user = users[choice - 1]
        confirm = input(f"Are you sure you want to delete {user['name']} {user['surname']}? (yes/no): ").strip().lower()
        if confirm in ["yes", "y"]:
            users.pop(choice - 1)
            with open(USERS_FILE, "w") as f:
                json.dump(users, f, indent=4)
            print(f"User {user['name']} {user['surname']} has been deleted.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input.")


def main():
    while True:
        print("\n" + "=" * 50)
        print("              MAIN MENU")
        print("=" * 50)
        print("  1. Register a new user")
        print("  2. View all users")
        print("  3. Edit a user")
        print("  4. Delete a user")
        print("  5. Exit")
        print("=" * 50)

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            view_users()
        elif choice == "3":
            edit_user()
        elif choice == "4":
            delete_user()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
