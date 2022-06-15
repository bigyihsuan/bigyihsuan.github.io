from googleapiclient.discovery import build
from pprint import pprint as pp
import json

with open("../secrets/apikey") as apikey:
    api_key = apikey.read()
    with build('youtube', 'v3', developerKey=api_key) as service:
        with service.playlistItems() as playlistItems:
            next_page_token = ""
            while next_page_token != None:
                # get "the ready room" playlist
                get_playlist_items = playlistItems.list(
                    part="contentDetails", playlistId="PLKfpV2bmlzODRtAZJmEKsAm8DRXqRqvzY", maxResults=50, pageToken=next_page_token)
                playlist_items = get_playlist_items.execute()
                for i, video in enumerate(playlist_items['items']):
                    print(i, video['contentDetails']['videoId'])
                next_page_token = playlist_items['nextPageToken'] if 'nextPageToken' in playlist_items else None
        # with service.channels() as channels:
        #     get_channel = channels.list(part="snippet", id="UC-lHJZR3Gqxm24_Vd_AJ5Yw") # pewdiepie
        #     channel: dict = get_channel.execute()
        #     pp(channel)
