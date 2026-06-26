@echo off
echo ==========================================
echo Setting up Academic Management System...
echo ==========================================

echo [1] Creating Virtual Environment...
python -m venv venv

echo [2] Activating Virtual Environment and Installing Dependencies...
call venv\Scripts\activate
pip install django pillow reportlab pandas

echo [3] Creating Django Apps...
python manage.py startapp accounts
python manage.py startapp dashboard
python manage.py startapp students
python manage.py startapp teachers
python manage.py startapp departments
python manage.py startapp courses
python manage.py startapp subjects
python manage.py startapp attendance
python manage.py startapp examinations
python manage.py startapp marks
python manage.py startapp timetable
python manage.py startapp announcements
python manage.py startapp reports
python manage.py startapp settings_app

echo [4] Connecting Database (Creating db.sqlite3)...
python manage.py makemigrations
python manage.py migrate

echo ==========================================
echo Setup Complete! db.sqlite3 has been created successfully.
echo You can now run the server:
echo python manage.py runserver
echo ==========================================
pause
