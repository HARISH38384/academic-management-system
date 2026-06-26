from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]
    
    # Personal Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    address = models.TextField()
    
    # Academic Details
    enrollment_number = models.CharField(max_length=20, unique=True)
    admission_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Active')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.enrollment_number})"
