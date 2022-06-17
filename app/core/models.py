"""
Database models.
"""
from django.db import models


class Student(models.Model):
    """Student Object."""
    # an auto-incremented id is generated when using models.Model
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
