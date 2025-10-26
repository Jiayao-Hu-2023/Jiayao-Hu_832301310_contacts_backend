# This is a sample Python script for Assignment 1 - Contacts
# This script can only be executed by command line
# Created by Jiayao Hu on 10/18/2025

"""
Basic contacts functions
Function 1: add
Basic operations for adding contacts, including name, phone number, etc. and store contacts information in a back-end database
Function 2: modify
Modify the contacts information. must be read from the back-end database, can not use the cache.
Function 3: delete
Requirement as above
"""

# Import the json module to read and write JSON files
import json
import sys
import os

# 添加路径处理 - 必须放在其他导入之前
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Database

# 添加路径处理
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Initialize the Flask app.
app = Flask(__name__)
CORS(app)


# Define a class Contacts to store contacts information,
# with name, phone number, email, and address
class Contacts:
    def __init__(self, first_name, last_name, category="", phone_number="", email="", address=""):
        self.first_name = first_name
        self.last_name = last_name
        self.category = category
        self.phone_number = phone_number
        self.email = email
        self.address = address

    # Overload the __str__ method to print the
    # contact information in a readable format
    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Category: {self.category}, Phone Number: {self.phone_number}, Email: {self.email}, Address: {self.address}"

    # Convert the contact information to a dictionary
    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "category": self.category,
            "phone_number": self.phone_number,
            "email": self.email,
            "address": self.address
        }

# Define a class AddressBook to store contacts information,
class AddressBook:
    # Initialize the AddressBook with database connection
    def __init__(self):
        self.db = Database()

    # Add contact to the AddressBook
    def add_contact(self, contact: Contacts):
        if self.db.add_contact(contact.to_dict()):
            print(f"Contact {contact.first_name} {contact.last_name} is added successfully.")
            return True
        else:
            print(f"Error: Contact with name '{contact.first_name} {contact.last_name}' already exists.")
            return False

    # find contact in the AddressBook by name
    def find_contact_in_list(self, contacts, first_name: str, last_name: str):
        for i, contact in enumerate(contacts):
            if contact['first_name'] == first_name and contact['last_name'] == last_name:
                return i
        return -1

    # Modify contact in the AddressBook
    def modify_contact(self, old_first_name: str, old_last_name: str, contact: Contacts):
        if self.db.update_contact(old_first_name, old_last_name, contact.to_dict()):
            if contact.first_name != old_first_name or contact.last_name != old_last_name:
                print(f"Contact '{old_first_name} {old_last_name}' has been renamed to '{contact.first_name} {contact.last_name}' successfully.")
            else:
                print(f"Contact '{old_first_name} {old_last_name}' is modified successfully.")
            return True
        else:
            print(f"Contact {old_first_name} {old_last_name} is not found.")
            return False

    # Delete contact in the AddressBook
    def delete_contact(self, first_name: str, last_name: str):
        if self.db.delete_contact(first_name, last_name):
            print(f"Contact {first_name} {last_name} is deleted successfully.")
            return True
        else:
            print(f"Contact {first_name} {last_name} is not found.")
            return False

    # Load all contacts from the AddressBook
    def load_contacts(self):
        contacts = self.db.get_all_contacts()
        print(f"{len(contacts)} contacts loaded successfully.")
        return contacts

# Create a global AddressBook instance
address_book = AddressBook()

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = address_book.load_contacts()
    return jsonify(contacts)

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.json
    contact = Contacts(data['first_name'], data['last_name'], data.get('category', ''),
                      data.get('phone_number', ''), data.get('email', ''), data.get('address', ''))
    if address_book.add_contact(contact):
        return jsonify({'message': f'Contact {contact.first_name} {contact.last_name} added successfully'}), 201
    else:
        return jsonify({'error': f'Contact with name {contact.first_name} {contact.last_name} already exists'}), 400

@app.route('/contacts/<first_name>/<last_name>', methods=['PUT'])
def update_contact(first_name, last_name):
    data = request.json
    contact = Contacts(data['first_name'], data['last_name'], data.get('category', ''),
                      data.get('phone_number', ''), data.get('email', ''), data.get('address', ''))
    if address_book.modify_contact(first_name, last_name, contact):
        return jsonify({'message': f'Contact {first_name} {last_name} updated successfully'})
    else:
        return jsonify({'error': f'Contact {first_name} {last_name} not found'}), 404

@app.route('/contacts/<first_name>/<last_name>', methods=['DELETE'])
def delete_contact(first_name, last_name):
    if address_book.delete_contact(first_name, last_name):
        return jsonify({'message': f'Contact {first_name} {last_name} deleted successfully'})
    else:
        return jsonify({'error': f'Contact {first_name} {last_name} not found'}), 404

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)