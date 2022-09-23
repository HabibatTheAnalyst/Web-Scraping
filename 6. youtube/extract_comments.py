import os
from googleapiclient.discovery import build
from pprint import pprint
from utils.comments import process_comments, make_csv

api_key = 'AIzaSyDnT1VLyzSJy3jNHQzprY6HwJJD1gK2WGY'
youtube = build('youtube', 'v3', developerKey = api_key)

def comment_threads(channelID, to_csv = False):
    comments_list = []
    request = youtube.commentThreads().list(
        part = "id, snippet, replies",
        order = "time",
        videoId = channelID)
    response = request.execute()
    comments_list.extend(process_comments(response['items']))

    while response.get('nextPageToken', None):
        request = youtube.commentThreads().list(
            part = "id, snippet, replies",
            order = "time",
            videoId = channelID,
            pageToken = response['nextPageToken'])
        response = request.execute()
        comments_list.extend(process_comments(response['items']))

    print(f'Finished fetching comments for {channelID}. {len(comments_list)} comments found.')

    if to_csv:
        make_csv(comments_list, channelID)
    return comments_list

def main():
    comment_threads('NM-2XSQc2q0', to_csv = True) 

if __name__ == "__main__":
    main()