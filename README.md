# 🗣️ SpeakAll AI – Multilingual AI Language Coach

**SpeakAll AI** is a voice-enabled AI-powered language coach built using Streamlit, Camel AI, and Groq's LLaMA 4 model. It allows users to practice over 30 languages via voice or text with instant grammar feedback and corrections.

---

## 🖼️ Screenshot

![SpeakAll AI Screenshot](assets/speakall-screenshot.png)

> 💡 Save your screenshot as `speakall-screenshot.png` and place it in an `assets/` folder.

---

## 📹 Demo

🎥 **[Click to watch the demo](DONE2-demo.mp4)**  
> Or upload to YouTube and link it here.

---

## 🚀 Features

- 🎙️ Practice speaking in your target language
- ✏️ Text input option with grammar corrections
- 🌍 30+ languages supported
- 🧠 Powered by LLaMA 4 and Camel role-based agents
- 💬 Real-time conversation UI
- 🖤 Beautiful dark-themed chat layout

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/speakall-ai.git
cd speakall-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `config.py` file:

```python
GROQ_API_KEY = "your_groq_api_key"
```

> ⚠️ **Important:** Do not push this file to GitHub if your repo is public. Use `.gitignore`.

### 4. Run the app

```bash
streamlit run main_app.py
```

---

## 📁 Folder Structure

```
SpeakAll-AI/
├── camel_agents/            # Camel AI role-based language coach
├── main_app.py              # Streamlit frontend app
├── config.py                # API key file (keep secret)
├── assets/                  # Screenshot and media
├── README.md                # Project description
├── DONE2-demo.mp4           # Demo video
```

---

## 🧠 Tech Stack

- [Camel AI](https://github.com/camel-ai/camel)
- [Groq API](https://console.groq.com/)
- [Streamlit](https://streamlit.io/)
- [LLaMA 4 Maverick 17B](https://groq.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)

---

## 📜 License

MIT License.

---

## 🙏 Credits

Made with ❤️ by [Your Name]
