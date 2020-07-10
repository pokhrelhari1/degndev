from django.db import models

class team(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=264)
    detail = models.TextField()
