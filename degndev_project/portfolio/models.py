from django.db import models

class portfolio(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


class team(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=264)
    detail = models.TextField()
