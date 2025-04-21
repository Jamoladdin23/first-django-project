# Book Rental Library 📚

## Project Overview
This is a web application for managing book rentals. The project includes:
- Viewing a list of available books.
- Managing categories and genres.
- Secure handling of data using PostgreSQL.
- Storing sensitive information in a `.env` file.
- Authentication and authorization for user accounts.
- This project integrates OpenAI's API to provide advanced functionalities like GPT-based chat support.

## Features
- User registration and login/logout functionality.
- Role-based access (e.g., admin and standard users).
- Encrypted passwords for enhanced security.
- Book rental management system.



---

## Requirements
- Python 3.10
- PostgreSQL
- Dependencies listed in `requirements.txt`

---

## Installation

## 1. Clone the Repository
Clone the project and navigate to its directory:

git clone <https://github.com/Jamoladdin23/first-django-project.git> 

cd: library

## 2. Set Up a Virtual Environment
Create and activate a virtual environment:

python -m venv .venv

source .venv/bin/activate  # Linux/MacOS

.venv\Scripts\activate     # Windows

# Install the required dependencies:
pip install -r requirements.txt

## 3. Configure the .env File
Create a .env file in the project's root directory and add the following:

SECRET_KEY=your_secret_key

NAME=database_name

USER=postgres_username

PASSWORD=your_password

HOST=localhost

PORT=5432

# After setting up the database, apply migrations:

python manage.py makemigrations

python manage.py migrate

# Running the Project

python manage.py runserver

## Open http://127.0.0.1:8000 in your browser.








