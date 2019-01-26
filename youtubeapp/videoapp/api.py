from django.conf import settings
import requests

def enable_search_specific_channel(user):
 
    searchbrchannel = requests.get(
        'https://www.googleapis.com/youtube/v3/search', params={
            'part':snippet,
            'channelId':UCGBpxWJr9FN0cFYA5GkKrMg,
            'maxResults':25,
            'key':settings.YOUTUBE_API_KEY,
            'forUsername': user,
        })
    searchbrchannel.raise_for_status()

main_api = 'https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCGBpxWJr9FNOcFYA5GkKrMg&maxResults=25&q=sama&key=AIzaSyBdtsP3kZ4s4iUFoGl8n_qDRGgC9BpsB3s'

json_data = requests.get(main_api).json()

for item in json_data['items']:
    if 'youtube#video' in item['id']['kind']:
        print(item['id']['videoId'])