import os
import subprocess

def main():
    print("Creating Admin User for Login...")
    script = """
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academic_management.settings')
django.setup()
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('SUCCESS: Admin user created (Username: admin | Password: admin)')
else:
    print('SUCCESS: Admin user already exists. You can login with (Username: admin | Password: admin)')
    """
    
    with open('temp_admin_create.py', 'w') as f:
        f.write(script)
        
    subprocess.run(r"venv\Scripts\python.exe temp_admin_create.py", shell=True)
    os.remove('temp_admin_create.py')

if __name__ == '__main__':
    main()
