import pandas as pd
from googleapiclient.discovery import build
from tqdm import tqdm
from decouple import config

# Set up the YouTube API key
# You can get the API key from the Google Cloud Console
API_KEY = config('API_KEY')

# https://commentpicker.com/ gives you the channerl ID
CHANNEL_ID = 'UCyth_6hqft9a7B_thdwYyww'

youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_channel_videos(youtube, channel_id):
    """
    Retrieves all videos from a specified YouTube channel.
    Args:
        youtube (googleapiclient.discovery.Resource): The YouTube API client.
        channel_id (str): The ID of the YouTube channel.
    Returns:
        list: A list of dictionaries, each containing the title, published date, and URL of a video.
    Example:
        youtube = build('youtube', 'v3', developerKey='YOUR_API_KEY')
        channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'
        videos = get_channel_videos(youtube, channel_id)
        for video in videos:
            print(video['title'], video['published_at'], video['url'])
    """
    videos = []
    next_page_token = None
    total_videos = 0
    
    response = youtube.channels().list(
        part='statistics',
        id=channel_id
    ).execute()
    total_videos = int(response['items'][0]['statistics']['videoCount'])
    
    with tqdm(total=total_videos, desc="Downloading videos data", unit="video") as pbar:
        while True:
            response = youtube.search().list(
                channelId=channel_id,
                part='snippet',
                order='date',
                maxResults=50,
                pageToken=next_page_token
            ).execute()
            
            for video in response.get('items', []):
                if video['id']['kind'] == 'youtube#video':
                    title = video['snippet']['title']
                    published_at = video['snippet']['publishedAt']
                    video_id = video['id']['videoId']
                    video_url = f"https://www.youtube.com/watch?v={video_id}"
                    videos.append({'title': title, 'published_at': published_at, 'url': video_url})
                    pbar.update(1)
            
            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break
    
    return videos

def main():
    videos = get_channel_videos(youtube, CHANNEL_ID)
    dataset_title_videos = pd.DataFrame(videos)
    dataset_title_videos.to_csv('channel_videos.csv', index=False)

if __name__ == "__main__":
    main()