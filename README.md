# Quiz App

A web application built with Django and MySQL to create and take quizzes.

## Features
- Take multiple choice quizzes
- See your score after each quiz
- Admin panel to manage quizzes and questions
- User authentication (login/logout)

## Tech Stack
- Python
- Django
- MySQL
- Bootstrap 5
- Git/GitHub

## How to Run
1. Clone the repository
2. Install dependencies: `pip install django mysqlclient`
3. Create MySQL database called `quizapp`
4. Update database settings in `settings.py`
5. Run migrations: `python manage.py migrate`
6. Create superuser: `python manage.py createsuperuser`
7. Run server: `python manage.py runserver`
8. Visit `http://127.0.0.1:8000`

## Author
Shareque Khan