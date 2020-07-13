from django.db import models

# Create your models here.

class webfolio(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
