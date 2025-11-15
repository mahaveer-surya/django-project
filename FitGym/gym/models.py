from django.db import models
from django.contrib.auth.models import User

MEMBERSHIP_CHOICES = [
    ('Basic', 'Basic'),
    ('Premium', 'Premium'),
    ('VIP', 'VIP'),
]

class GymMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male','Male'),('Female','Female')])
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)
    join_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
