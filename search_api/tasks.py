from __future__ import absolute_import,unicode_literals
from search_api.models import Search
import youtube_api.settings as settings
from django_cron import CronJobBase, Schedule
import datetime
import requests
from celery import shared_task

@shared_task
def taskfetch():
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    keycheck = False
    time_now = datetime.datetime.now()
    last_request_time = time_now - datetime.timedelta(seconds=10)
    keys = settings.SEARCH_API_KEYS
    res = []
    for key in keys:
        try:
            params = {
                'part': 'snippet',
                'q' : 'cricket',
                'key': key,
                'maxResults': 50,
                'order' : 'date'
            }
            keycheck = True
            r = requests.get(search_url,params=params)
            res = r.json()
        except Exception as e:
            print(e)

        if keycheck:
            break

    if keycheck:
        print(res)
        for obj in res['items']:
            vid_id = obj['id'].get('videoId')
            title = obj['snippet'].get('title')
            description = obj['snippet']['description']
            published_at = obj['snippet']['publishedAt']
            thumbnailsUrls = obj['snippet']['thumbnails']['high']['url']
            channel_id = obj['snippet']['channelId']
            channel_title = obj['snippet']['channelTitle']
        #    print(vid_id,title,description,published_at,thumbnailsUrls,channel_id,channel_title)
            try:
                vid_obj = Search.objects.get(vid_id=vid_id)
            except Search.DoesNotExist:    
                vid_obj = Search.objects.create(
                    vid_id = vid_id,
                    title = title,
                    description = description,
                    published_at = published_at,
                    thumbnailsUrls = thumbnailsUrls,
                    channel_id = channel_id,
                    channel_title = channel_title,
                )
                vid_obj.save()
                