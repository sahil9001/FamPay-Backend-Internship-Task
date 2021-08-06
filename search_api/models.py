from django.db import models

# Create your models here.
class Search(models.Model):
    # Database Model: Search (For saving cached results)
    id = models.AutoField(primary_key=True)
    vid_id = models.CharField(max_length=1000, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField()
    thumbnailsUrls = models.URLField(max_length=1000)
    channel_id = models.CharField(max_length=100)
    channel_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
