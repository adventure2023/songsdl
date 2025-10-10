# Contributing to YouTube Audio Downloader

Thank you for considering contributing to this project! 🎉

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear title and description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, browser)

### Suggesting Features

Have an idea? Open an issue with:
- Clear description of the feature
- Why it would be useful
- How it might work

### Code Contributions

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ytdl.git
   cd ytdl
   ```

2. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Test your changes locally
   - Add comments for complex logic

4. **Test thoroughly**
   ```bash
   streamlit run app.py
   ```

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to GitHub**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Describe what you changed and why
   - Reference any related issues

## Development Setup

```bash
# Clone the repo
git clone https://github.com/vibecoded/ytdl.git
cd ytdl

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Code Style

- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Follow PEP 8 for Python code

## Testing

Before submitting:
- [ ] App runs without errors
- [ ] Downloads work correctly
- [ ] UI looks good on desktop and mobile
- [ ] No console errors
- [ ] New features are documented

## Need Help?

Feel free to ask questions in:
- GitHub Issues
- Pull Request comments
- Discussions tab

Thank you for helping make this project better! 🙏
