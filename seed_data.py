import os
import django
import random
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'academic_management.settings')
django.setup()

from students.models import Student
from teachers.models import Teacher
from departments.models import Department
from courses.models import Course
from subjects.models import Subject
from announcements.models import Announcement

def seed_db():
    print("Seeding database with default dummy data...")

    # Departments
    depts = ['Computer Science', 'Electrical Engg', 'Mechanical Engg', 'Civil Engg', 'Information Tech']
    for d in depts:
        Department.objects.get_or_create(name=d, defaults={'hod': f'Dr. {d.split()[0]} Head', 'established_date': date(2000, 1, 1)})
    
    # Courses
    courses = [('B.Tech CSE', 4, 160), ('B.Tech ECE', 4, 160), ('B.Tech Mech', 4, 160), ('B.Sc IT', 3, 120)]
    for name, dur, cred in courses:
        Course.objects.get_or_create(name=name, defaults={'duration_years': dur, 'credits': cred})
        
    # Subjects
    subjects = [('Data Structures', 'CS101', 4), ('Circuits', 'EC101', 3), ('Thermodynamics', 'ME101', 4), ('Web Dev', 'IT101', 3)]
    for name, code, cred in subjects:
        Subject.objects.get_or_create(code=code, defaults={'name': name, 'credits': cred})

    # Teachers
    for i in range(1, 11):
        Teacher.objects.get_or_create(
            email=f'teacher{i}@college.edu',
            defaults={
                'name': f'Prof. Teacher {i}',
                'phone': f'98765432{i:02d}',
                'qualification': 'Ph.D' if i % 2 == 0 else 'M.Tech',
                'experience': random.randint(3, 20)
            }
        )

    # Students
    for i in range(1, 31):
        Student.objects.get_or_create(
            enrollment_number=f'ENR2026{i:03d}',
            defaults={
                'first_name': f'Student',
                'last_name': f'Name{i}',
                'email': f'student{i}@student.edu',
                'phone': f'87654321{i:02d}',
                'gender': random.choice(['Male', 'Female']),
                'dob': date(2005, 1, 1) + timedelta(days=random.randint(1, 365)),
                'address': f'{i} College Road, City',
                'status': 'Active'
            }
        )

    # Announcements
    for i in range(1, 6):
        Announcement.objects.get_or_create(
            title=f'Important Notice {i}',
            defaults={
                'content': f'This is the detailed content for announcement {i}. Please check the portal for more details.',
            }
        )

    print("Successfully added default data! Dashboard will now show real counts.")

if __name__ == '__main__':
    seed_db()
