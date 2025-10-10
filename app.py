import streamlit as st
import yt_dlp
import os
from pathlib import Path
import tempfile
import imageio_ffmpeg
from datetime import timedelta

# Get FFmpeg path from imageio-ffmpeg
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
os.environ['FFMPEG_BINARY'] = ffmpeg_path

# Verify FFmpeg is available
if not os.path.exists(ffmpeg_path):
    print(f"WARNING: FFmpeg not found at {ffmpeg_path}")

st.set_page_config(
    page_title="YouTube Audio Downloader",
    page_icon="🎵",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .stDownloadButton button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 10px;
    }
    .stDownloadButton button:hover {
        background: linear-gradient(90deg, #764ba2 0%, #667eea 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎵 YouTube Audio Downloader</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Convert YouTube videos to high-quality MP3 files instantly</div>', unsafe_allow_html=True)

# Input URL with better styling
st.markdown("### 🔗 Enter YouTube URL")
url = st.text_input(
    "Paste your YouTube video URL here:",
    placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    label_visibility="collapsed"
)

if st.button("Download Audio", type="primary"):
    if not url:
        st.error("Please enter a YouTube URL")
    else:
        try:
            # First, fetch video info without downloading
            status_placeholder = st.empty()
            status_placeholder.info("🔍 Fetching video information...")
            
            with tempfile.TemporaryDirectory() as temp_dir:
                # Configure yt-dlp options for info extraction
                info_opts = {
                    'quiet': True,
                    'no_warnings': True,
                    'extract_flat': False,
                    'socket_timeout': 30,
                    'retries': 3,
                }
                
                # Get video info first
                with yt_dlp.YoutubeDL(info_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    title = info.get('title', 'Unknown')
                    duration = info.get('duration', 0)
                    thumbnail = info.get('thumbnail', None)
                    uploader = info.get('uploader', 'Unknown')
                    view_count = info.get('view_count', 0)
                
                # Display video metadata
                status_placeholder.empty()
                
                col1, col2 = st.columns([1, 2])
                
                with col1:
                    if thumbnail:
                        st.image(thumbnail, use_container_width=True)
                    else:
                        st.info("No thumbnail available")
                
                with col2:
                    st.write(f"**Title:** {title}")
                    st.write(f"**Uploader:** {uploader}")
                    if duration:
                        duration_str = str(timedelta(seconds=duration))
                        st.write(f"**Duration:** {duration_str}")
                    if view_count:
                        st.write(f"**Views:** {view_count:,}")
                
                st.divider()
                
                # Progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                def progress_hook(d):
                    if d['status'] == 'downloading':
                        try:
                            percent = d.get('_percent_str', '0%').strip('%')
                            percent_float = float(percent.replace('%', ''))
                            progress_bar.progress(min(int(percent_float), 100) / 100)
                            
                            downloaded = d.get('_downloaded_bytes_str', '?')
                            total = d.get('_total_bytes_str', '?')
                            speed = d.get('_speed_str', '?')
                            eta = d.get('_eta_str', '?')
                            
                            status_text.text(f"⬇️ Downloading: {downloaded}/{total} | Speed: {speed} | ETA: {eta}")
                        except:
                            status_text.text("⬇️ Downloading...")
                    elif d['status'] == 'finished':
                        status_text.text("🔄 Converting to MP3...")
                        progress_bar.progress(100)
                
                # Configure yt-dlp options for download
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
                    'progress_hooks': [progress_hook],
                    'quiet': False,
                    'no_warnings': True,
                    'socket_timeout': 30,
                    'retries': 3,
                    'fragment_retries': 3,
                    'ffmpeg_location': ffmpeg_path,  # Explicitly set FFmpeg path
                    'keepvideo': False,  # Don't keep the original video file
                }
                
                # Download the audio
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                status_text.text("🔍 Looking for converted file...")
                    
                # Find the downloaded MP3 file - check all files
                all_files = os.listdir(temp_dir)
                # Debug info (comment out for production)
                # st.write(f"Debug: Files in temp dir: {all_files}")
                
                mp3_file = None
                # Look for MP3 files first
                for file in all_files:
                    if file.endswith('.mp3'):
                        mp3_file = os.path.join(temp_dir, file)
                        break
                
                # If no MP3 found, look for any audio file
                if not mp3_file:
                    for file in all_files:
                        if any(file.endswith(ext) for ext in ['.m4a', '.webm', '.opus', '.ogg']):
                            mp3_file = os.path.join(temp_dir, file)
                            st.warning(f"MP3 conversion may have failed. Found: {file}")
                            break
                
                if mp3_file and os.path.exists(mp3_file):
                    # Read the file
                    with open(mp3_file, 'rb') as f:
                        audio_bytes = f.read()
                    
                    file_size_mb = len(audio_bytes) / (1024 * 1024)
                    file_extension = os.path.splitext(mp3_file)[1]
                    
                    status_text.empty()
                    progress_bar.empty()
                    
                    # Success message with styling
                    st.markdown("---")
                    st.balloons()  # Celebration effect!
                    st.success(f"✅ **Successfully converted!**")
                    
                    # File info in a nice format
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.metric("📦 File Size", f"{file_size_mb:.2f} MB")
                    with col_b:
                        st.metric("🎵 Format", file_extension.upper().replace('.', ''))
                    
                    st.markdown("---")
                    
                    # Provide download button
                    st.download_button(
                        label=f"📥 Download MP3 File",
                        data=audio_bytes,
                        file_name=f"{title}{file_extension}",
                        mime="audio/mpeg" if file_extension == '.mp3' else "audio/webm",
                        use_container_width=True
                    )
                    
                    st.caption(f"🎼 {title}")
                else:
                    st.error("❌ Failed to find the downloaded audio file")
                    st.info("Please try again or contact support if the issue persists.")
                    
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("**Troubleshooting tips:**")
            st.write("- Check your internet connection")
            st.write("- Verify the URL is valid and accessible")
            st.write("- Try a different video")
            st.write("- The video might be region-restricted or private")

# Add some information in the sidebar
with st.sidebar:
    st.header("ℹ️ About")
    st.write("""
    Download high-quality audio from YouTube videos as MP3 files, quickly and easily!
    
    **How to use:**
    1. 📋 Paste a YouTube video URL
    2. 🎵 Click "Download Audio"
    3. ⏳ Wait for processing
    4. 💾 Download your MP3 file
    
    **Features:**
    - High-quality 192kbps MP3
    - Fast downloads
    - No registration required
    - Free forever
    """)
    
    st.header("📝 Legal Notice")
    st.caption("""
    Please respect copyright laws. Only download content you have the right to download or that is in the public domain.
    """)
    
    st.header("🔒 Privacy")
    st.caption("""
    Your downloads are private. No data is stored or tracked.
    """)
