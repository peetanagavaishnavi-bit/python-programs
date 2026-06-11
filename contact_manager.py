import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                if "," in line:
                    name, phone = line.strip().split(",", 1)
                    contacts[name] = phone
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

contacts = load_contacts()

while True:
    print("\n--- 📞 Contact Manager (File Storage) ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Exit")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        if name and phone:
            contacts[name] = phone
            save_contacts(contacts)
            print(f"Success: {name} saved permanently to contacts.txt!")
        else:
            print("Name and phone cannot be empty.")

    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            print("\n--- Saved Contacts ---")
            for name, phone in contacts.items():
                print(f"👤 {name}: 📱 {phone}")

    elif choice == "3":
        print("Exiting Contact Manager. Goodbye!")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
