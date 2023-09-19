from googleapiclient import discovery
from pprint import pprint as print
import requests
from pytube import YouTube

api_key = "AIzaSyCZDX7fxHm9OZJ_Kwc-Kr3ZfXowIuAgGJA"
youtube = discovery.build("youtube", 'v3', developerKey=api_key)

def search_shorts(keyword:str, max_results=10):
    req = youtube.search().list(q=keyword, part='snippet', type='video', maxResults=max_results, pageToken=None)
    response = req.execute()
    shorts = []
    for video in response['items']:
        video_id = video['id']['videoId']
        request = requests.head("https://www.youtube.com/shorts/" + str(video_id))
        print(request.status_code)
        if request.status_code == 200:
            shorts.append(video)
    return shorts


def download_shorts(shorts_id):
    VIDEO_SAVE_DIRECTORY = "videos"
    FILENAME = shorts_id
    link = "https://www.youtube.com/shorts/"+str(shorts_id)
    video = YouTube(link)
    try:
        video = video.streams.get_highest_resolution()
        print("Video yuklab olindi.")
        return video.download(VIDEO_SAVE_DIRECTORY, filename=FILENAME)
    except:
        print("Videoni yuklab bo'lmadi.")
        return None


