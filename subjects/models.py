from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.name if hasattr(self, 'name') else self.title
