# 🚀 Deployment Guide

## Deploy to Streamlit Cloud (Recommended - Free!)

### Prerequisites
- GitHub account
- Git installed on your machine

### Steps

1. **Initialize Git repository** (if not already done)
```bash
git init
git add .
git commit -m "Initial commit - YouTube Audio Downloader"
```

2. **Create GitHub repository**
   - Go to https://github.com/new
   - Create a new repository (e.g., `youtube-audio-downloader`)
   - Don't initialize with README (we already have one)

3. **Push to GitHub**
```bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
git branch -M main
git push -u origin main
```

4. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Click "New app" button
   - Connect your GitHub account (if first time)
   - Select your repository
   - Set branch: `main`
   - Set main file path: `app.py`
   - Click "Deploy"!

5. **Wait for deployment** (usually 2-5 minutes)
   - Streamlit will install dependencies from `requirements.txt`
   - System packages from `packages.txt` (FFmpeg) will be installed
   - Your app will be available at: `https://YOUR-APP-NAME.streamlit.app`

### Troubleshooting

#### App won't start
- Check the logs in Streamlit Cloud dashboard
- Verify all dependencies are in `requirements.txt`
- Ensure `packages.txt` includes `ffmpeg`

#### FFmpeg errors
- The `packages.txt` file should contain: `ffmpeg`
- Check that `imageio-ffmpeg` is in `requirements.txt`

#### Slow downloads
- This is normal on free tier
- Consider upgrading to Streamlit Cloud Pro for better performance

## Alternative Deployment Options

### Deploy on Railway

1. Install Railway CLI: https://docs.railway.app/develop/cli
2. Login: `railway login`
3. Deploy: `railway up`

### Deploy on Heroku

1. Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
```

### Deploy on Google Cloud Run

1. Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

2. Deploy:
```bash
gcloud run deploy youtube-downloader --source .
```

## Custom Domain

If you want a custom domain like `download.yourdomain.com`:

1. Go to Streamlit Cloud settings
2. Click "Custom domain"
3. Follow instructions to configure DNS

## Performance Tips

- **Free tier** is great for personal use and demos
- For **high traffic**, consider:
  - Streamlit Cloud Pro ($20/month)
  - Railway Pro ($5/month base)
  - Self-hosting on VPS

## Security Notes

- App doesn't store any user data
- All downloads happen in temporary memory
- Files are automatically deleted after download
- No cookies or tracking

## Updating Your App

When you push changes to GitHub:
```bash
git add .
git commit -m "Your update message"
git push
```

Streamlit Cloud will automatically redeploy! 🎉

## Getting Help

- **Streamlit Docs**: https://docs.streamlit.io/
- **Streamlit Forum**: https://discuss.streamlit.io/
- **yt-dlp Issues**: https://github.com/yt-dlp/yt-dlp/issues

---

**Need help?** Open an issue on GitHub or reach out!
