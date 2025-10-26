# Contact Management System - Backend

## Project Overview
This is the backend server for the Contact Management System, providing a RESTful API to manage contact information. The server handles CRUD operations and stores data in an SQLite database.

## Features
- **RESTful API**: Standard HTTP methods for contact management
- **Data Persistence**: SQLite database for reliable data storage
- **CORS Support**: Cross-Origin Resource Sharing enabled for frontend communication
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality
- **Data Validation**: Basic validation for contact data
- **Error Handling**: Consistent error responses and status codes

## Technologies Used
- Python 3.8+
- Flask (Web Framework)
- SQLite (Database)
- Flask-CORS (Cross-Origin Resource Sharing)

## Getting Started
### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Clone or download the repository
2. Navigate to the backend directory:
   ```bash
   cd Jiayao Hu_832301310_contacts_backend
   ```
3. Install the required dependencies:
   ```bash
   pip install flask flask_cors
   ```

### Running the Server
1. Start the Flask development server:
   ```bash
   python -m src.controller.contacts
   ```
   or
   ```bash
   python src\controller\contacts.py
   ```
2. The server will start at `http://localhost:5000`

## API Endpoints
### Get All Contacts
- **Method**: GET
- **Endpoint**: `/contacts`
- **Description**: Retrieve all contacts from the database
- **Parameters**: None
- **Response**: JSON array of contact objects
  ```json
  [
    {
      "first_name": "John",
      "last_name": "Doe",
      "category": "Friend",
      "phone_number": "123-456-7890",
      "email": "john.doe@example.com",
      "address": "123 Main St"
    }
  ]
  ```
- **Status Codes**: 200 OK

### Add a New Contact
- **Method**: POST
- **Endpoint**: `/contacts`
- **Description**: Create a new contact
- **Request Body**: JSON object containing contact information
  ```json
  {
    "first_name": "Jane",
    "last_name": "Smith",
    "category": "Family",
    "phone_number": "987-654-3210",
    "email": "jane.smith@example.com",
    "address": "456 Elm St"
  }
  ```
- **Response**: JSON object of the created contact with status message
  ```json
  {
    "message": "Contact added successfully",
    "contact": {
      "first_name": "Jane",
      "last_name": "Smith",
      "category": "Family",
      "phone_number": "987-654-3210",
      "email": "jane.smith@example.com",
      "address": "456 Elm St"
    }
  }
  ```
- **Status Codes**: 201 Created, 400 Bad Request

### Update a Contact
- **Method**: PUT
- **Endpoint**: `/contacts/<first_name>/<last_name>`
- **Description**: Update an existing contact by first and last name
- **URL Parameters**: 
  - `first_name`: The first name of the contact to update
  - `last_name`: The last name of the contact to update
- **Request Body**: JSON object containing updated contact information
  ```json
  {
    "category": "Colleague",
    "phone_number": "555-555-5555",
    "email": "jane.smith@company.com",
    "address": "789 Oak Ave"
  }
  ```
- **Response**: JSON object with status message
  ```json
  {
    "message": "Contact updated successfully"
  }
  ```
- **Status Codes**: 200 OK, 404 Not Found, 400 Bad Request

### Delete a Contact
- **Method**: DELETE
- **Endpoint**: `/contacts/<first_name>/<last_name>`
- **Description**: Delete a contact by first and last name
- **URL Parameters**: 
  - `first_name`: The first name of the contact to delete
  - `last_name`: The last name of the contact to delete
- **Response**: JSON object with status message
  ```json
  {
    "message": "Contact deleted successfully"
  }
  ```
- **Status Codes**: 200 OK, 404 Not Found

## File Structure
```
Jiayao Hu_832301310_contacts_backend/
├── README.md           # Project documentation
├── codestyle.md        # Code style guidelines
├── contacts.db         # SQLite database file
└── src/                # Source code directory
    ├── __init__.py     # Package initialization
    ├── controller/     # API controllers
    │   └── contacts.py # Main application and API routes
    └── database.py     # Database interaction layer
```

## Database Schema
The application uses an SQLite database with a single `contacts` table:

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key (auto-increment) |
| first_name | TEXT | Contact's first name |
| last_name | TEXT | Contact's last name |
| category | TEXT | Contact category (Friend, Family, etc.) |
| phone_number | TEXT | Contact's phone number |
| email | TEXT | Contact's email address |
| address | TEXT | Contact's physical address |

## Development Notes
- The database file `contacts.db` will be created automatically if it doesn't exist
- The server runs in debug mode by default, which is not recommended for production
- For production deployment, consider using a more robust database and configuring proper security settings

## License
This project can be used for grading purposes only. Do not use it for production purposes.
Strictly follow the code style guidelines in `codestyle.md`
