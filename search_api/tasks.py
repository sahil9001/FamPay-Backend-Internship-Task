from __future__ import absolute_import, unicode_literals
from search_api.models import Search
import youtube_api.settings as settings
import requests
from celery import shared_task

# Celery Task for searching youtube every 10 seconds with results are ordered by date
@shared_task
def taskfetch():
    # Fetching environment variables
    search_url = settings.SEARCH_URL
    keys = settings.SEARCH_API_KEYS

    res = []
    # Validates youtube key for the given query
    keycheck = False
    for key in keys:
        try:
            # Parameters for youtube api search, ordering by date and only returning the first 50 results
            params = {
                "part": "snippet",
                "q": "cricket",
                "key": key,
                "maxResults": 50,
                "order": "date",
            }
            # Making a request to youtube api
            r = requests.get(search_url, params=params)
            # If youtube key is valid, then setting keycheck to True
            if r.status_code == 200:
                # Converting the response to json and storing it in a list
                res = r.json()
                keycheck = True
                break
        except r.status_code == 403 or r.status_code == 400:
            print(r.status_code)
        # If youtube key is valid, then break the loop
        if keycheck:
            break

    # print(keycheck)
    if keycheck:
        # If youtube key is valid, then fetching the search results
        for obj in res["items"]:
            vid_id = obj["id"].get("videoId")
            title = obj["snippet"].get("title")
            description = obj["snippet"]["description"]
            published_at = obj["snippet"]["publishedAt"]
            thumbnailsUrls = obj["snippet"]["thumbnails"]["high"]["url"]
            channel_id = obj["snippet"]["channelId"]
            channel_title = obj["snippet"]["channelTitle"]
            # Creating a new search object
            try:
                # Checking if the search object already exists
                vid_obj = Search.objects.get(vid_id=vid_id)
            except Search.DoesNotExist:
                # If not, then creating a new search object
                vid_obj = Search.objects.create(
                    vid_id=vid_id,
                    title=title,
                    description=description,
                    published_at=published_at,
                    thumbnailsUrls=thumbnailsUrls,
                    channel_id=channel_id,
                    channel_title=channel_title,
                )
                vid_obj.save()
