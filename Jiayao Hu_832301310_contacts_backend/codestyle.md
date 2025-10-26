# Backend Code Style Guide

This document outlines the coding standards and best practices for the Contact Management System backend.

## Python
- **PEP 8 Compliance**: Follow PEP 8 guidelines for Python code
- **Indentation**: Use 4 spaces for indentation (do not use tabs)
- **Naming Conventions**: 
  - Use snake_case for variables, functions, and module names
  - Use PascalCase for class names
  - Use UPPER_CASE for constants
- **Docstrings**: Include docstrings for all functions, classes, and modules
- **Imports**: 
  - Group imports by category (standard library, third-party, local)
  - Use absolute imports where possible
  - Avoid wildcard imports (from module import *)
- **Type Hints**: Use type hints to improve code readability and enable static analysis
- **Line Length**: Keep lines to a maximum of 79 characters
- **Whitespace**: 
  - Use blank lines to separate functions and logical sections
  - Add a single space after commas and around operators
  - Do not use trailing whitespace

## Flask
- **Application Structure**: Organize code into controllers, models, and utilities
- **Blueprints**: Use blueprints to modularize the application (for larger projects)
- **Routes**: Define clear, descriptive route names
- **Request Handling**: Use Flask's request object to access incoming data
- **Response Formatting**: Use jsonify for consistent JSON responses
- **Error Handling**: Implement consistent error handling with appropriate status codes
- **Configuration**: Use environment variables or configuration files for settings
- **Logging**: Implement proper logging for debugging and monitoring

## Database
- **SQLite**: Use parameterized queries to prevent SQL injection
- **Connection Management**: Open and close database connections properly
- **Transactions**: Use transactions for atomic operations
- **Schema Design**: 
  - Use meaningful table and column names
  - Define appropriate data types
  - Implement proper indexing
- **Abstraction**: Use the Database class to abstract database operations
- **Error Handling**: Handle database errors gracefully and provide meaningful messages

## API Design
- **RESTful Principles**: Follow RESTful design principles
- **HTTP Methods**: Use appropriate HTTP methods (GET, POST, PUT, DELETE)
- **Status Codes**: Return standard HTTP status codes
- **Request/Response**: 
  - Use JSON for request and response bodies
  - Validate incoming data
  - Provide consistent error messages
- **Endpoint Naming**: Use descriptive and consistent endpoint naming conventions
- **Authentication/Authorization**: Implement proper authentication (for production)

## Security
- **Input Validation**: Validate all user inputs
- **Parameterized Queries**: Use parameterized queries to prevent SQL injection
- **CORS Configuration**: Restrict CORS origins in production
- **Error Messages**: Avoid exposing sensitive information in error messages
- **HTTPS**: Use HTTPS in production environments

## Code Organization
- **Modularity**: Split code into logical modules and files
- **Single Responsibility**: Each function and class should have a single responsibility
- **Comments**: Add comments to explain complex logic and decisions
- **Refactoring**: Regularly refactor code to improve readability and maintainability

## Testing
- **Unit Tests**: Write unit tests for individual functions and classes
- **Integration Tests**: Test the integration between components
- **API Tests**: Test API endpoints with various inputs and scenarios
- **Test Coverage**: Aim for high test coverage

## Commit Messages
- **Clarity**: Write clear, concise commit messages
- **Structure**: Use the format: "<type>: <description>"
- **Types**: 
  - feat: New feature
  - fix: Bug fix
  - docs: Documentation changes
  - style: Code style changes
  - refactor: Code refactoring
  - test: Adding or modifying tests
  - chore: Build tasks or maintenance
- **Detail**: Provide additional context in the commit body when necessary

## Version Control
- **Branching**: Use feature branches for development
- **Pull Requests**: Use pull requests for code review
- **Merging**: Merge only after code review and successful tests
