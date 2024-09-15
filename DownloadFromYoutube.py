
import ydl as ydl
import youtube_dl
from pytube import YouTube
from pytube import Playlist
import os
import time
destinationPath = '.\\Audio Files\\'


def download_from_url(url):
    pass


def downloadFromYoutube(playlistURL="https://www.youtube.com/watch?v=lnUJQNpBCKE&list=PLfWCwAR0WfwXKZtythXhdJ9nE4MsrgMJ8&index=3"):
    playlist = Playlist(playlistURL)
    for url in playlist:
        #download_audio(url)
        download_from_url(url)


    # for url in playlist:
    #     yt = YouTube(url)
    #     video = yt.streams.filter(only_audio=True).first()  # extract only audio
    #     out_file = video.download(output_path=destinationPath)  # download the file
    #     base, ext = os.path.splitext(out_file)  # save the file
    #     new_file = base + '.mp3'
    #     os.rename(out_file, new_file)
    #     print(yt.title + " has been successfully downloaded.")



def download_audio(url, retries=3):
    """Downloads audio from a YouTube video with retries on failure."""
    for attempt in range(retries):
        try:
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            if not video:
                print(f"No audio stream found for {yt.title}. Skipping...")
                return
            out_file = video.download(output_path=destinationPath)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"{yt.title} has been successfully downloaded.")
            return
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            if attempt < retries - 1:
                print("Retrying...")
                time.sleep(2)  # Wait before retrying
            else:
                print(f"Failed to download {url} after {retries} attempts.")




if __name__ == '__main__':
    #txt = input("Type here playlist url to downloading from youtube: ")
    #downloadFromYoutube(txt)

    downloadFromYoutube()
