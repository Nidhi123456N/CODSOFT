class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nCONTACT LIST:")
            for name, details in self.contacts.items():
                print(f"{name} - Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def search_contact(self, keyword):
        results = [(name, details) for name, details in self.contacts.items() if keyword in name or keyword in details['Phone']]
        if not results:
            print(f"No contacts found with '{keyword}'.")
        else:
            print("\nSEARCH RESULTS:")
            for name, details in results:
                print(f"{name} - Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

    def update_contact(self, name, phone, email, address):
        if name in self.contacts:
            self.contacts[name] = {"Phone": phone, "Email": email, "Address": address}
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"No contact found with the name '{name}'.")

def contact_book_app():
    contact_book = ContactBook()

    while True:
        print("\nCONTACT BOOK APPLICATION")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == "2":
            contact_book.view_contacts()

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")
            contact_book.update_contact(name, phone, email, address)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "6":
            print("Exiting the Contact Book application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_book_app()
