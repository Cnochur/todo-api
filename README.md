# To-do API
---

## Overview

To-do API is a RESTful backend service built using Django and SQLite.

Users will have account management, task management, be able to update individual status and retrieve their list of tasks via a JSON API.

---

## Features

- User Management
- Create a to-do
- Edit a to-do
- Update a todos status
- Filter by status
- REST API responses in JSON

---

## Tech Stack

- Django
- Django REST Framework
- SQLite

---

## Database Design

User

 └── Task

### Task

SATUS_CHOICES = [New, In Progress, Complete]

- id
- user id
- title
- description
- status
- created_on

---

## Endpoints

### Tasks

- GET     /
- GET     /tasks/{id}/
- POST    /tasks/
- PUT     /tasks/{id}/
- DELETE  /tasks/{id}/

### Auth

- POST /auth/login
- POST /auth/register

---

## Installation Steps

git clone [ add repo name here ]

cd todo-api

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

---

