from pytube import YouTube, Playlist
import os
from moviepy.editor import VideoFileClip
import whisper


os.makedirs('videos', exist_ok=True)
video_urls = [
    'https://www.youtube.com/watch?v=G3Eup4mfJdA&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=1',
    'https://www.youtube.com/watch?v=480OGItLZNo&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=2',
    'https://www.youtube.com/watch?v=ervLwxz7xPo&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=11',
    'https://www.youtube.com/watch?v=OA2Tj75T3fI&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=4',
    'https://www.youtube.com/watch?v=qrvK_KuIeJk&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=5',
    'https://www.youtube.com/watch?v=oFVuQ0RP_As&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=6',
    'https://www.youtube.com/watch?v=4aPp8KX6EiU&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=7',
    'https://www.youtube.com/watch?v=h8PSWeRLGXs&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=8',
    'https://www.youtube.com/watch?v=Z8qC2tVkGeU&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=9',
    'https://www.youtube.com/watch?v=Y9nM_9oBj2k&list=PLI1yx5Z0Lrv77D_g1tvF9u3FVqnrNbCRL&index=10',
    
]

for url in video_urls:
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        if video_stream:
            video_stream.download(output_path='videos/')
            print(f'Downloaded video: {yt.title}.mp4')
        en_caption = yt.captions.get_by_language_code('en')
        if en_caption:
            en_caption_srt = en_caption.generate_srt_captions()
            with open(f'videos/{yt.title}.srt', 'w') as file:
                file.write(en_caption_srt)
                print(f'Downloaded caption: {yt.title}.srt')
    except Exception as e:
        print(f'Failed to download {url}: {str(e)}')
