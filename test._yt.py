from pytube import YouTube

url = "https://www.youtube.com/watch?v=Lj7nJBB0Eog"
yt = YouTube(url)

destination = "."
video = yt.streams

if yt.streams.filter(only_audio=True):# download_audio:
    outfile = video.filter(only_audio=True).last().download(output_path=destination)
    downloaded = True
