import os

FILENAME = "user_info.txt"

def add_user():
    """Add a new user to the file"""
    name = input("Enter your name: ")

    with open(FILENAME, "a") as file:
        file.write(f"Name: {name}\n")

    print("✅ User info saved.\n")


def show_users():
    """Display all users from the file"""
    if not os.path.exists(FILENAME):
        print("⚠️ No user file found yet.\n")
        return

    with open(FILENAME, "r") as file:
        data = file.read()
        if data.strip() == "":
            print("⚠️ No users found.\n")
        else:
            print("\n📋 All Users:\n")
            print(data)


def main():
    while True:
        print("====== User Info Menu ======")
        print("1. Add User")
        print("2. Show All Users")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_user()
        elif choice == "2":
            show_users()
        elif choice == "3":
            print("👋 Exiting... Bye!")
            break
        else:
            print("❌ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
