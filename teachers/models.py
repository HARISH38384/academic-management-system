from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.name if hasattr(self, 'name') else self.title
