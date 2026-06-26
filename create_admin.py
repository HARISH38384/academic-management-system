import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academic_management.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Admin user created successfully! Username: admin | Password: admin")
else:
    print("Admin user already exists. Username: admin | Password: admin")
