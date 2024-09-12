from pytube import YouTube
from pytube import Playlist

import os

destinationPath = '.\\Audio Files\\'


def downloadFromYoutube(playlistURL="https://www.youtube.com/watch?v=lnUJQNpBCKE&list=PLfWCwAR0WfwXKZtythXhdJ9nE4MsrgMJ8&index=3"):
    playlist = Playlist(playlistURL)

    for url in playlist:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()  # extract only audio
        out_file = video.download(output_path=destinationPath)  # download the file
        base, ext = os.path.splitext(out_file)  # save the file
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.")





if __name__ == '__main__':
    txt = input("Type here playlist url to downloading from youtube: ")
    downloadFromYoutube(txt)