from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hod = models.CharField(max_length=100)
    established_date = models.DateField()

    def __str__(self):
        return self.name if hasattr(self, 'name') else self.title
