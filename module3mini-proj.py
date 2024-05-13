# User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:
# ``` Welcome to the Contact Management System! Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file
# Import contacts from a text file *BONUS
# Quit "> 

# Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).
# Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact with all relevant details.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact by searching for their unique identifier.
# Searching for a contact by their unique identifier and displaying their details.
# Displaying a list of all contacts with their unique identifiers.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system. * BONUS
# User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.
# Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.


contacts = {}
file_path = 'directory.txt'

def add_contact(contacts):
    name = input("Enter your first and last name: ").title()
    phone = input("Enter your phone number: ")
    email = input("Enter your e-mail: ")
    address = input("Enter your address: ").title()
    notes = input("Add a note: ")
    try:
        contacts[email] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "notes": notes
        }
        print("Contact added successfully!")
    except:
        print("Invalid input")




def update_contact_info(access_info, change_info):
    access_info = input("What is your email? ")
    if access_info in contacts:
        change_info = input("What information would you like to change. Type 'name', phone', 'email', 'address', 'notes'. ").lower()
        if change_info in contacts[access_info]:
            updated_info = input("Enter the new information: ")
            contacts[access_info][change_info] = updated_info


def remove_contact():
    delete_email = input("Enter in your e-mail address. ")
    if delete_email in contacts:
        del contacts[delete_email]
        print(f"{delete_email} has been removed from contacts. ")
    else:
        print("Could not find contact entered. ")


def get_email_input():
    return input("Enter email: ")


def search_contact(email, contacts):
    if email in contacts:
        contact_details = contacts[email]
        print("Contact found:")
        print(f"Email: {email}")
        print(f"Name: {contact_details['name']}")
        print(f"Phone: {contact_details['phone']}")
        print(f"Address: {contact_details['address']}")
        print(f"Notes: {contact_details['notes']}")
    else:
        print("Contact not found")


def add_directory(email, details):
    with open("directory.txt", "a") as file:
        if email in details:
            file.write(f"{email}\n")
            for person_info, person_details in details[email].items():
                file.write(f"   {person_info}: {person_details}\n")
            print(f"Contact {email} exported successfully.")
        else:
            print(f"Contact {email} not found in contacts.")



def import_contacts(file_path, contacts):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(':')
                if len(data) == 5:  # 5 for name, phone, email, address, notes
                    name, phone, email, address, notes = data
                    contacts[email] = {
                        "name": name,
                        "phone": phone,
                        "email": email,
                        "address": address,
                        "notes": notes
                    }
                    print(f"Contact {email} imported successfully.")
                else:
                    print(f"Invalid data format in line: {line.strip()}")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"Error occurred while importing contacts: {e}")

# Main loop updated
while True:
    action = input('''Welcome to the Contact Management System!
    Menu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit

    Enter the number corresponding to your desired action: ''')

    if action == '1':
        add_contact(contacts)
    elif action == '2':
        update_contact_info(contacts)
    elif action == '3':
        remove_contact()
    elif action == '4':
        email_input = get_email_input()  # Call the function to get email input
        search_contact(email_input, contacts)  # Pass the email input as an argument
    elif action == '5':
        print(contacts)
    elif action == '6':
        export_email = input("Enter the email you want to export to text file: ")
        add_directory(export_email, contacts)
    elif action == '7':
        import_contacts(file_path, contacts)
    else:
        break


    # cannot get import to work correctly