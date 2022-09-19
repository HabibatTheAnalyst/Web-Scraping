from urllib import request
from googleapiclient import build

api_key = 'AIzaSyDnT1VLyzSJy3jNHQzprY6HwJJD1gK2WGY'
video_id = 'a0zrnEnUiYo'
youtube = build('youtube', 'v3', developer_key = api_key)

# function to extract video details
def get_video_comments(youtube, video_id):
    request = youtube.commentThreads().list(
                part = 'snippet, replies',
                order = 'time',
                videoId = video_id)
    response = request.execute
    return response

get_video_comments(youtube, video_id)