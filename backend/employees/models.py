from django.db import models


class Employee(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) 
