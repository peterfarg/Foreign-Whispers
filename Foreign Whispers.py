from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

playlist_url = "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"

def download_videos_from_playlist(playlist_url):
    playlist = YouTube(playlist_url)
    videos = playlist.video_urls

    for video_url in videos:
        download_video(video_url)

def download_video(video_url):
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(progressive=True, file_extension="mp4").first()
    video_stream.download()
    video_id = video_url.split("v=")[1]
    captions = YouTubeTranscriptApi.get_transcript(video_id)
    with open(f"{video_id}.txt", "w", encoding="utf-8") as file:
        for caption in captions:
            file.write(caption["text"] + "\n")

if __name__ == "__main__":
    download_videos_from_playlist(playlist_url)
