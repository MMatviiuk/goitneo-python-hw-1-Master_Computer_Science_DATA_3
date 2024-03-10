import os
import json
from datetime import datetime

# Define the path to the contacts data file
contacts_data_file = os.path.join(os.path.dirname(__file__), "contacts.json")

# Initialize an empty dictionary to store contacts
contacts = {}

# Define a list of commands
commands = ["add", "change", "find", "list", "close", "exit"]

# Define a dictionary with command descriptions
command_descriptions = {
    "add": "Add a new contact.",
    "change": "Change the phone number of an existing contact.",
    "find": "Find the phone number of a contact.",
    "list": "List all contacts.",
    "close": "Close the bot.",
    "exit": "Close the bot.",
}

# Initial list of contacts
initial_contacts = [
    {"name": "John", "surname": "Forbes Nash Jr.", "birthday": "1928-06-13"},
    {"name": "Andrew", "surname": "Wiles", "birthday": "1953-04-11"},
    {"name": "Guido", "surname": "van Rossum", "birthday": "1956-01-31"},
    {"name": "Satya", "surname": "Nadella", "birthday": "1967-08-19"},
    {"name": "Demis", "surname": "Hassabis", "birthday": "1976-07-27"}
]

# Function to load contacts from a file
def load_contacts():
    global contacts
    if os.path.isfile(contacts_data_file):
        with open(contacts_data_file, "r") as f:
            try:
                contacts = json.load(f)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in contacts.json")
                contacts = {}
    else:
        contacts = {}
    return contacts

# Function to save contacts to a file
def save_contacts():
    with open(contacts_data_file, "w") as f:
        json.dump(contacts, f, default=str, indent=4)

# Load contacts from the data file on startup
contacts = load_contacts()

# Add initial contacts to the contacts dictionary
for contact in initial_contacts:
    name = f"{contact['name']} {contact['surname']}"
    birthday = datetime.strptime(contact["birthday"], "%Y-%m-%d")
    contacts[name] = birthday

# Function to add a new contact
def add_contact():
    name = input("Enter the name of the contact: ").strip().capitalize()
    surname = input("Enter the surname of the contact: ").strip().capitalize()
    while True:
        birthday_str = input("Enter the birthday (DD/MM/YYYY) of the contact: ").strip()
        try:
            birthday = datetime.strptime(birthday_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")

    full_name = f"{name} {surname}"
    if full_name in contacts:
        print(f"Contact with name {full_name} already exists.")
    else:
        contacts[full_name] = birthday
        print(f"Contact {full_name} added.")
        save_contacts()

# Function to change the phone number of an existing contact
def change_phone_number(name, new_phone_number):
    print("This functionality is not available in this version of the bot.")

# Function to find the phone number of a contact
def find_phone_number(name):
    print("This functionality is not available in this version of the bot.")

# Function to list all contacts
def list_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, birthday in contacts.items():
            if birthday is not None:
                print(f"{name} - Birthday: {birthday.strftime('%Y-%m-%d')}")
            else:
                print(f"{name} - Birthday: Unknown")

# Main loop of the bot
while True:
    command = input("Enter a command (add/change/find/list/close/exit): ").strip().lower()

    if command not in commands:
        print("Invalid command. Please enter a valid command.")
        continue

    if command == "add":
        add_contact()
    elif command == "change":
        print("This functionality is not available in this version of the bot.")
    elif command == "find":
        print("This functionality is not available in this version of the bot.")
    elif command == "list":
        list_contacts()
    elif command == "close" or command == "exit":
        print("Closing the bot.")
        break
