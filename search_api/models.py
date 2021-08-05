from django.db import models

# Create your models here.
class Search(models.Model):
    vid_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField()
    thumbnailsUrls = models.URLField(max_length=1000)
    channel_id = models.CharField(max_length=100)
    channel_title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
