from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer (models.Model):
    first_name = models.CharField(max_length = 150)
    middle_name = models.CharField (max_length = 150)
    last_name = models.CharField(max_length = 150)
    username = models.CharField(max_length = 150)
    e_mail = models.EmailField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username 