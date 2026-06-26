import os
import subprocess
import sys

def run_cmd(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("ERRORS:", result.stderr)

def main():
    print("Updating Database...")
    run_cmd(r"venv\Scripts\python.exe manage.py makemigrations")
    run_cmd(r"venv\Scripts\python.exe manage.py migrate")
    print("Done! You can now start the server with: python manage.py runserver")

if __name__ == '__main__':
    main()
