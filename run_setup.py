import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    # Write output to a log file
    with open('setup_log.txt', 'w') as f:
        sys.stdout = f
        sys.stderr = f
        
        # 1. Activate venv and check pip
        run_cmd(r"venv\Scripts\python.exe -m pip install django pillow reportlab pandas")
        
        # 2. Create apps
        apps = ["accounts", "dashboard", "students", "teachers", "departments", 
                "courses", "subjects", "attendance", "examinations", "marks", 
                "timetable", "announcements", "reports", "settings_app"]
        for app in apps:
            run_cmd(fr"venv\Scripts\python.exe manage.py startapp {app}")
            
        # 3. Makemigrations and migrate
        run_cmd(r"venv\Scripts\python.exe manage.py makemigrations")
        run_cmd(r"venv\Scripts\python.exe manage.py migrate")
        
        print("Done!")

if __name__ == '__main__':
    main()
