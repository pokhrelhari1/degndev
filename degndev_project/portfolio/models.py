from django.db import models
from django import forms

class portfolio(models.Model):
    title = models.CharField(max_length=264)
    video = models.FileField(upload_to='video/', null=True)

    def __str__(self):
        return self.title
