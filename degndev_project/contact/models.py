from django.db import models
from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    package = models.CharField(max_length=20, default='package')
    plan = models.CharField(max_length=20, default='plan')
    message = models.TextField()
    def str(self):
        return self.name
