from django.db import models

class gallery(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=264)
