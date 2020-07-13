from django.db import models

class appfolio(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
