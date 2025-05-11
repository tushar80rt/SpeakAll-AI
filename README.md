# 🗣️ SpeakAll AI – Multilingual AI Language Coach

**SpeakAll AI** is a voice-enabled AI-powered language coach built using Streamlit, Camel AI, and Groq's LLaMA 4 model. It allows users to practice over 30 languages via voice or text with instant grammar feedback and corrections.

---

## 🖼️ Demo Screenshot

![Screenshot 1](https://github.com/user-attachments/assets/aa3d16de-5d00-4905-97c9-6f9441ebabf4)

![Screenshot 2](https://github.com/user-attachments/assets/c7b92968-ac12-4fbc-b07d-92b9b4ba7731)

![Screenshot 3](https://github.com/user-attachments/assets/ccc53e20-907b-4587-849b-78b703180398)

---


## 🚀 Features

- 🎙️ Practice speaking in your target language
- ✏️ Text input option with grammar corrections
- 🌍 30+ languages supported
- 🧠 Powered by LLaMA 4 and Camel role-based agents
- 💬 Real-time conversation UI
- 🖤 Beautiful dark-themed chat layout

---

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
├── README.md                # Project description
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

Made with ❤️ by [TUSHAR SINGH]
