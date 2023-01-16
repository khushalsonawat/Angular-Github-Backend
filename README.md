# Github-Angular

This project uses Django 4 for it's backend and Angular 15.0.4 for it's frontend.

Django version: 4.1.5

Python version: 3.8.5

Node version: 16.13.0

Package Manager: npm 9.2.0

## Steps to run the project locally

Clone the repository

Create a virtual environment using `python -m venv env`

### Setting up the backend

Activate the virtual environment using `env\Scripts\activate` (for Windows)

Install the required packages using `pip install -r requirements.txt`

Look out for the environment variables from .env.example file

Once done, run `python manage.py makemigrations` and `python manage.py migrate` to migrate the changes to the database

Run the local server using `python manage.py runserver`

The dev server will be live at `http://localhost:8000`
