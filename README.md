# Task Tracker API

A Django REST Framework API for creating, tracking, and managing tasks.

## Tech Stack
- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (default local setup)

## Setup & Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/queentoria1/task_tracker.git
   cd task_tracker
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
