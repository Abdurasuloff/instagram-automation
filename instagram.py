from credentials import username, password
from instagrapi import Client
from youtube import download_shorts


def upload_reel(shorts_list):
    cl = Client()
    cl.login(username, password)
    for shorts in shorts_list:
        shorts_id = shorts['id']['videoId']
        video_path = download_shorts(shorts_id)
        if video_path == None:
            return "Video yuklab olish uchun yaroqli emas!"
        else:
            video_description = shorts['snippet']['title']
            cl.clip_upload(video_path, caption=video_description)
            print("Bajarildi:", video_description)
    return "Bajarildi!"


