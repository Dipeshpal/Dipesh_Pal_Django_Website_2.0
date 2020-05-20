import json
from apiclient.discovery import build
import os


class Youtube_API:
    def __init__(self):
        file_name = "key.json"

        with open(file_name) as file:
            data = json.load(file)

            self.key = data['key']

        self.youtube = build('youtube', 'v3', developerKey=self.key)

    def get_channel_videos(self, channel_id):
        # get Uploads playlist id
        res = self.youtube.channels().list(id=channel_id,
                                      part='snippet, statistics, contentDetails').execute()
        playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        res_copy = res
        videos = []
        next_page_token = None

        while 1:
            res = self.youtube.playlistItems().list(playlistId=playlist_id,
                                               part='snippet',
                                               maxResults=50,
                                               pageToken=next_page_token).execute()
            videos += res['items']
            next_page_token = res.get('nextPageToken')

            if next_page_token is None:
                break

        return videos, res_copy

    def filter_details(self, res):
        channelTitle = res['items'][0]['snippet']['title']
        thu = res['items'][0]['snippet']['thumbnails']['high']['url']

        subs_count = res['items'][0]['statistics']['subscriberCount']
        videoCount = res['items'][0]['statistics']['videoCount']
        viewCount = res['items'][0]['statistics']['viewCount']

        dic = {
            "channelTitle": channelTitle,
            "profile_pic": thu,
            "subs_count": subs_count,
            "videoCount": videoCount,
            "viewCount": viewCount
        }

        return dic


