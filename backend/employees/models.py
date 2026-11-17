from django.db import models


class Employee(models.Model):
    # id (primary key) is added automatically by Django
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    role = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)  # filled in automatically
