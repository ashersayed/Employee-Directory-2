# Employee Directory

A simple app to add, view, edit and delete employees.

- Frontend: React + TypeScript (Vite), Axios, plain CSS
- Backend: Python (Django) REST API
- Database: MySQL



## Requirements

- Python 3.10+
- Node.js (LTS)
- MySQL 8.0+

## Setup

### 1. Database

Start MySQL, then create an empty database:

```bash
mysql -u root -p -e "CREATE DATABASE employee_directory"
```

### 2. Backend

Open `backend/config/settings.py` and set your MySQL password in `DATABASES`.

In a terminal:

```bash
cd backend
pip install -r requirements.txt
python manage.py makemigrations employees
python manage.py migrate
python manage.py runserver
```

The API runs at http://127.0.0.1:8000.

### 3. Frontend

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173.

## Notes

- CORS is enabled for `http://localhost:5173` in `settings.py`.
- Django 5.2 is used because Django 6 requires MySQL 8.4 or newer.
