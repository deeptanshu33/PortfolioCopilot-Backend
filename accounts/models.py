from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    class Designation(models.TextChoices):
        STUDENT = 'ST', 'Student'
        PROFESSIONAL = 'PR', 'Professional'
    
    designation = models.CharField(
        max_length=2,
        choices=Designation.choices,
        default=Designation.STUDENT
    )

    def __str__(self):
        return self.email