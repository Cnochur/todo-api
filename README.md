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

- GET     tasks/
- POST    tasks/add/
- PUT     tasks/edit-task/
- PATCH   tasks/update-status/
- DELETE  tasks/delete/

### Auth

- POST /user/login
- POST /user/register

---

## Installation Steps (Linux)

    git clone https://github.com/Cnochur/todo-api.git
    
    cd todo-api
    
    python -m venv venv
    
    source venv/bin/activate
    
    pip install -r requirements.txt
    
    cd todo
    
    python manage.py migrate
    
    python manage.py runserver

---

