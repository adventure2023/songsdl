# 🚀 Quick Reference Card

## For End Users

### How to Use
1. Go to the website
2. Paste YouTube URL
3. Click "Download Audio"
4. Wait for conversion
5. Click "Download MP3"

### Supported URLs
✅ YouTube videos
✅ YouTube Music
✅ Standard youtube.com links
✅ youtu.be short links

### Quality
- **Audio**: 192 kbps MP3
- **Format**: MP3 (or original if conversion fails)

---

## For Developers

### Local Development
```bash
# Install
pip install -r requirements.txt

# Run
streamlit run app.py

# Access
http://localhost:8501
```

### Key Files
- `app.py` - Main application
- `requirements.txt` - Python packages
- `packages.txt` - FFmpeg for cloud
- `.streamlit/config.toml` - Theme

### Deploy to Streamlit Cloud
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main
```
Then visit: https://share.streamlit.io/

### Environment Variables
None required! Everything is self-contained.

---

## Troubleshooting

### Problem: "Failed to find downloaded audio file"
**Solution**: Check internet connection, try different video

### Problem: Slow downloads
**Solution**: Normal on free tier, try smaller videos

### Problem: "An error occurred"
**Solutions**:
- Check URL is valid YouTube link
- Video might be private/restricted
- Try different video
- Check internet connection

### Problem: App won't start
**Solutions**:
- Verify Python 3.8+ installed
- Run: `pip install -r requirements.txt`
- Check no other app on port 8501

---

## Performance Tips

### For Users
- Use shorter videos for faster downloads
- Wait for progress bar to complete
- Don't refresh page during download

### For Developers
- Deploy on paid tier for high traffic
- Use CDN for static assets
- Consider caching for popular videos
- Add rate limiting if needed

---

## Legal & Privacy

### What's Stored
❌ No user data
❌ No download history
❌ No cookies
❌ No tracking
✅ Everything in memory
✅ Auto-cleanup

### Legal
⚠️ Only download content you have rights to
⚠️ Respect copyright laws
⚠️ Personal use only

---

## Support & Resources

### Documentation
- `README.md` - Full documentation
- `DEPLOYMENT.md` - Deploy guide
- `CONTRIBUTING.md` - Contribute guide
- `PROJECT_SUMMARY.md` - Technical details

### Get Help
- 🐛 **Bugs**: GitHub Issues
- 💡 **Ideas**: GitHub Discussions
- 📖 **Docs**: Streamlit Docs
- 💬 **Chat**: GitHub Discussions

### Links
- **Live Demo**: [Your deployed URL]
- **GitHub**: https://github.com/vibecoded/ytdl
- **Streamlit**: https://streamlit.io
- **yt-dlp**: https://github.com/yt-dlp/yt-dlp

---

## Quick Commands

```bash
# Start locally
streamlit run app.py

# Install deps
pip install -r requirements.txt

# Update yt-dlp
pip install -U yt-dlp

# Check logs
streamlit run app.py --logger.level=debug

# Different port
streamlit run app.py --server.port=8502
```

---

**Made with ❤️ | Free Forever | No Registration Required**
