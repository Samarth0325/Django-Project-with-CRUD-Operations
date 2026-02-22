from django.db import models

class Student(models.Model):
    roll_no = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"