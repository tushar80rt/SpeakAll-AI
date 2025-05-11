import streamlit as st
import speech_recognition as sr
import pyttsx3
import threading
import re
from camel_agents.camel_language_coach import CamelLanguageCoach
from config import GROQ_API_KEY

# ========== PAGE CONFIG ========== 
st.set_page_config(
    page_title="SpeakAll AI",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="auto"
)

# ========== DARK THEME CSS ========== 
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: #0f172a;
        color: #e2e8f0;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #f8fafc !important;
    }
    .header { text-align: center; margin-bottom: 2rem; }
    .card {
        background: #1e293b;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border: 1px solid #334155;
    }
    .chat-box {
        background: #1e293b;
        border-radius: 12px;
        padding: 1rem;
        height: 400px;
        overflow-y: auto;
        margin-bottom: 1rem;
        border: 1px solid #334155;
    }
    .user-msg {
        background: #3b82f6;
        color: white;
        border-radius: 12px 12px 0 12px;
        padding: 10px 15px;
        margin: 8px 0;
        max-width: 80%;
        float: right;
        clear: both;
    }
    .bot-msg {
        background: #334155;
        color: #e2e8f0;
        border-radius: 12px 12px 12px 0;
        padding: 10px 15px;
        margin: 8px 0;
        max-width: 80%;
        float: left;
        clear: both;
    }
    .stButton>button {
        background: #3b82f6;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        width: 100%;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background: #2563eb;
    }
    .stTextInput>div>div>input {
        background: #1e293b;
        color: #e2e8f0;
        border-radius: 8px;
        padding: 10px 14px;
        border: 1px solid #334155;
    }
    .stRadio>div {
        flex-direction: row;
        gap: 10px;
    }
    .stRadio>div>label {
        color: #e2e8f0 !important;
    }
    .stSelectbox>div>div>select {
        background: #1e293b;
        color: #e2e8f0;
        border: 1px solid #334155;
    }
    ::-webkit-scrollbar {
        width: 6px;
    }
    ::-webkit-scrollbar-track {
        background: #1e293b;
    }
    ::-webkit-scrollbar-thumb {
        background: #3b82f6;
        border-radius: 3px;
    }
    .stSpinner>div>div {
        border-color: #3b82f6 transparent transparent transparent !important;
    }
    hr {
        border-color: #334155;
    }
    .stCaption {
        color: #94a3b8 !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== HEADER ========== 
st.markdown("""
<div class="header">
        <h1>SpeakAll AI 🌍</h1>
    <p style="color: #94a3b8;">Practice languages with AI</p>
</div>
""", unsafe_allow_html=True)

# ========== INITIALIZE TTS ========== 
engine = pyttsx3.init()
is_speaking = False
lock = threading.Lock()

def clean_text_for_speech(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'[*_`#]', '', text)
    return text.strip()

def speak_response(response: str):
    global is_speaking
    with lock:
        if not is_speaking:
            is_speaking = True
            def speak():
                clean_text = clean_text_for_speech(response)
                if clean_text:
                    engine.say(clean_text)
                    engine.runAndWait()
                global is_speaking
                is_speaking = False
            threading.Thread(target=speak).start()

# ========== LANGUAGE SELECTION ========== 
languages = [
    "English", "Spanish", "French", "German", "Hindi", "Japanese", "Chinese", 
    "Arabic", "Russian", "Italian", "Portuguese", "Dutch", "Turkish", "Korean", 
    "Bengali", "Punjabi", "Vietnamese", "Thai", "Urdu", "Tamil", "Gujarati", 
    "Marathi", "Malayalam", "Kannada", "Odia", "Punjabi", "Nepali", "Swahili", 
    "Polish", "Czech", "Hungarian", "Bhojpuri"
]
# ========== MAIN LAYOUT ========== 
col1, col2 = st.columns([1, 2])

with col1:
    with st.container():
        st.markdown("### Language Settings")
        language = st.selectbox("Choose language", languages, label_visibility="collapsed")
        
        st.markdown("### Input Method")
        input_method = st.radio("", ("Voice 🎙️", "Text ✏️"), horizontal=True, label_visibility="collapsed")

# ========== SESSION STATE ========== 
if "coach" not in st.session_state or st.session_state.language != language:
    st.session_state.coach = CamelLanguageCoach(language=language, groq_api_key=GROQ_API_KEY)
    st.session_state.language = language
    st.session_state.chat_history = []
    st.session_state.spoken = ""
    st.session_state.last_user_input = ""

# ========== AUDIO PROCESSING ========== 
def listen_to_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        with st.spinner("Listening..."):
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        st.warning("Couldn't understand audio")
        return None

# ========== CHAT INTERFACE ========== 


with col2:
    st.markdown("### Conversation 🗣️")
    chat_container = st.container()

    last_bot_msg = None
    with chat_container:
        for role, msg in st.session_state.chat_history:
            if role == "user":
                st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)
                last_bot_msg = msg

    # Speak only the latest assistant message
    if last_bot_msg and st.session_state.spoken != last_bot_msg:
        speak_response(last_bot_msg)
        st.session_state.spoken = last_bot_msg

    if input_method == "Voice 🎙️":
        if st.button("Start Recording", type="primary"):
            user_input = listen_to_audio()
            if user_input:
                # Check if the input is the same as the last one
                if user_input != st.session_state.last_user_input:
                    st.session_state.chat_history.append(("user", user_input))
                    with st.spinner("Thinking..."):
                        reply = st.session_state.coach.chat(user_input)
                        st.session_state.chat_history.append(("assistant", reply))
                        st.session_state.last_user_input = user_input  # Update last input
                    st.rerun()
                else:
                    st.warning("You already said that. Try something else.")
    else:
        user_input = st.text_input("Type your message", key="text_input", placeholder="Type here...")
        if user_input:
            # Check if the input is the same as the last one
            if user_input != st.session_state.last_user_input:
                st.session_state.chat_history.append(("user", user_input))
                with st.spinner("Generating response..."):
                    reply = st.session_state.coach.chat(user_input)
                    st.session_state.chat_history.append(("assistant", reply))
                    st.session_state.last_user_input = user_input  # Update last input
                st.rerun()
            else:
                st.warning("You already said that. Try something else.")

# ========== FOOTER ========== 
st.markdown("---")
st.caption("Powered by Camel AI and Groq")

