from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    duration_years = models.IntegerField()
    credits = models.IntegerField()

    def __str__(self):
        return self.name if hasattr(self, 'name') else self.title
