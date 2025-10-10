# 🎵 YouTube Audio Downloader

A beautiful, easy-to-use Streamlit web app that downloads audio from YouTube videos and converts them to high-quality MP3 files.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🎵 **High-Quality MP3** - 192kbps audio downloads
- 📸 **Video Preview** - See thumbnail and metadata before downloading
- 📊 **Progress Tracking** - Real-time download progress with speed and ETA
- 🎨 **Beautiful UI** - Clean, modern interface with gradients and animations
- 🚀 **Fast & Free** - No registration required, completely free
- 🔒 **Private** - No data stored or tracked
- ☁️ **Cloud Ready** - Deploy to Streamlit Cloud in minutes

## 🚀 Quick Start

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd ytdl
```

2. **Create a virtual environment**
```bash
# Using uv (recommended)
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Or using standard venv
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**
```bash
# Using uv (faster)
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

That's it! **No additional setup needed** - FFmpeg binaries are automatically included via `imageio-ffmpeg`.

### Running Locally

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## ☁️ Deploy to Streamlit Cloud (Free!)

1. **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-github-repo-url>
git push -u origin main
```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Connect your GitHub repository
   - Select `app.py` as the main file
   - Click "Deploy"!

3. **Done!** Your app will be live at `https://<your-app-name>.streamlit.app`

### Deployment Files Included

- ✅ `requirements.txt` - Python dependencies
- ✅ `packages.txt` - System dependencies (FFmpeg)
- ✅ `.gitignore` - Clean repo

## 📖 Usage

1. Open the app in your browser
2. Paste a YouTube video URL
3. Click "Download Audio"
4. Watch the progress and preview video info
5. Download your MP3 file!

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** - Web framework
- **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** - YouTube downloader
- **[imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg)** - FFmpeg binaries for audio conversion
- **Python 3.8+** - Programming language

## 📝 Legal Notice

This tool is for personal use only. Please respect copyright laws and only download content you have the right to download or that is in the public domain.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the amazing YouTube download library
- [Streamlit](https://streamlit.io/) for making web apps so easy
- [imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg) for bundled FFmpeg binaries

---

Made with ❤️ by [Your Name]

**[🌐 Live Demo](https://your-app-name.streamlit.app)** | **[⭐ Star on GitHub](https://github.com/your-username/ytdl)**
