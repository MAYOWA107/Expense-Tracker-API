Expense Tracker API
This is a Django Rest Framework (DRF) based API for tracking expenses. The API allows users to create, read, update, and delete expense records, with additional features such as filtering by category and date, as well as user authentication.

Table of Contents
Features
Installation
Usage
API Endpoints
Authentication
Filtering
Testing
Contributing


Features
JWT Authentication: Secure user authentication using JSON Web Tokens.
Expense Management: Create, read, update, and delete expenses.
Filtering: Filter expenses by category, date, and amount range.
User Registration: Support for user registration and management through djoser.
Custom User Model: Extendable user model with custom fields.


Installation
Clone the repository:

git clone https://github.com/MAYOWA107/Expense-Tracker-API.git
cd Expense-Tracker-API

Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install the dependencies:
pip install -r requirements.txt

Run the migrations:
python manage.py migrate
Create a superuser (optional):
python manage.py createsuperuser

Run the development server:
python manage.py runserver


Usage
Use a tool like Postman or cURL to interact with the API. You can manage expenses, authenticate users, and apply filters to the expense data.

API Endpoints
Authentication
POST /api/token/: Obtain JWT token.
POST /api/token/refresh/: Refresh JWT token.
User Management (via Djoser)
POST /auth/users/: Register a new user.
POST /auth/jwt/create/: Obtain JWT token via credentials.
POST /auth/jwt/refresh/: Refresh JWT token.
Expenses
GET /: List all expenses.
POST /create/: Create a new expense.
GET /expense/{id}/: Retrieve a specific expense.
PUT /expense/{id}/: Update an existing expense.
DELETE /expense/{id}/: Delete an expense.

Authentication
The API uses JWT for authentication. Obtain a token via /api/token/ and include it in the Authorization header of your requests as Bearer <your_token>.

Filtering
Filter expenses by using query parameters:

By Date: /expenses/?date=YYYY-MM-DD
By Category: /expenses/?category=food
By Amount Range: /expenses/?min_amount=50&max_amount=200

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
