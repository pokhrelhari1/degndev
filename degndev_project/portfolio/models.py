from django.db import models

class portfolio(models.Model):
    title = models.CharField(max_length=264)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='video/', null=True)

    def __str__(self):
        return self.title
