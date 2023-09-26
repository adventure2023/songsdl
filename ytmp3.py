import os
import streamlit as st
from pytube import YouTube

st.title("Get MP3") 
st.subheader("Enter the URL:") 
url = st.text_input(label='URL')
# Create a checkbox
get_mp4 = st.checkbox("Get MP4")
destination = '.'
input_done = st.button("Enter")

if input_done and  url != '':
    yt = YouTube(url)
    st.image(yt.thumbnail_url, width=200)
    st.subheader('''
    {}
    ### Length: {} seconds
    '''.format(yt.title , yt.length ))
    video = yt.streams
    if len(video) > 0:
        file_ext = ".mp3"
        downloaded , download_audio = False , False
        # download_video = st.button("Download Video")
        # if yt.streams.filter(only_audio=True):
        #     download_audio = st.button("Download Audio Only")
        # if download_video:            
        #     outfile = video.get_highest_resolution().download(output_path=destination)
        #     downloaded = True
        if get_mp4:
            only_audio = False
            outfile = video.get_highest_resolution().download(output_path=destination)
            downloaded = True
            file_ext = ".mp4"
        elif yt.streams.filter(only_audio=True):# download_audio:
            outfile = video.filter(only_audio=True).last().download(output_path=destination)
            downloaded = True
        if downloaded:
            # save the file
            base, ext = os.path.splitext(outfile)
            new_file = base + file_ext
            os.rename(outfile, new_file)
            with open(new_file, "rb") as f:
                st.download_button('Download file', f, file_name=os.path.basename(new_file))
            os.remove(new_file)
    else:
        st.subheader("Sorry, this video can not be downloaded")