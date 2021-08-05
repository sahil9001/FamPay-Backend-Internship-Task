import youtube_api.settings as settings
from django_cron import CronJobBase, Schedule
import datetime
import requests 

class FetchToDatabase(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'search_api.fetch_to_database'    # a unique code
    def do(self):
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
                    'maxResults': 5,
                }
                keycheck = True
                r = requests.get(search_url,params=params)
                res = r.json()
            except Exception as e:
                break

            if keycheck:
                break

        if keycheck:
            for obj in res['items']:
                vid_id = obj['id']['videoId']
                title = obj['snippet']['title']
                description = obj['snippet']['description']
                published_at = obj['snippet']['publishedAt']
                thumbnailsUrls = obj['snippet']['thumbnails']['high']['url']
                channel_id = obj['snippet']['channelId']
                channel_title = obj['snippet']['channelTitle']
                print(vid_id,title,description,published_at,thumbnailsUrls,channel_id,channel_title)
                
                
                