import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY", "")

# ─── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DapurPintar",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ─── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&family=JetBrains+Mono:wght@400&display=swap');

:root {
    color-scheme: light;
}

*,
*::before,
*::after {
    box-sizing: border-box;
    color-scheme: light !important;
}

html,
body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
section.main,
[data-testid="stSidebar"] {
    background: #FBFBFA !important;
    color: #2F3437;
    font-family: 'DM Sans', 'Helvetica Neue', Arial, sans-serif;
}

header[data-testid="stHeader"],
footer,
#MainMenu {
    display: none !important;
}

.block-container {
    max-width: 760px !important;
    padding: 2.5rem 1.5rem 6rem !important;
    margin: 0 auto;
}

/* Header */

.dp-eyebrow {
    display: inline-block;
    font-size: .67rem;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: #346538;
    background: #EDF3EC;
    padding: 3px 10px;
    border-radius: 9999px;
    margin-bottom: .6rem;
}

.dp-title {
    font-family: 'Newsreader', serif;
    font-size: 2rem;
    font-weight: 600;
    letter-spacing: -.03em;
    line-height: 1.1;
    color: #111111;
    margin-bottom: .35rem;
}

.dp-subtitle {
    font-size: .85rem;
    color: #787774;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

.dp-divider {
    border: none;
    border-top: 1px solid #EAEAEA;
    margin-bottom: 2rem;
}

/* Chat */

[data-testid="stChatMessage"] {
    background: #FFFFFF !important;
    border: 1px solid #EAEAEA !important;
    border-radius: 8px !important;
    padding: 14px 18px !important;
    margin-bottom: 8px !important;
    animation: fadeUp .4s cubic-bezier(.16,1,.3,1) both;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: #F7F6F3 !important;
}

[data-testid="stChatMessageAvatarUser"],
[data-testid="stChatMessageAvatarAssistant"] {
    display: none !important;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span {
    font-size: .9375rem !important;
    line-height: 1.65 !important;
    color: #2F3437 !important;
}

[data-testid="stChatMessage"] strong {
    color: #111111 !important;
    font-weight: 500 !important;
}

[data-testid="stChatMessage"] code {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: .82rem !important;
    background: #F7F6F3 !important;
    border: 1px solid #EAEAEA !important;
    border-radius: 4px !important;
    padding: 1px 6px !important;
    color: #1F6C9F !important;
}

/* Chat input */

[data-testid="stChatInputContainer"],
[data-testid="stChatInputContainer"] > div,
[data-testid="stChatInputContainer"] > div > div {
    background: #FFFFFF !important;
    box-shadow: none !important;
}

[data-testid="stChatInputContainer"] {
    border: 1px solid #EAEAEA !important;
    border-radius: 6px !important;
}

[data-testid="stChatInput"] textarea {
    background: #FFFFFF !important;
    color: #111111 !important;
    font-size: .9rem !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #ADADAD !important;
}

[data-testid="stChatInputContainer"] button {
    background: transparent !important;
    border: none !important;
    color: #787774 !important;
}

/* Text input */

.stTextInput input {
    border: 1px solid #EAEAEA !important;
    border-radius: 6px !important;
    background: #FFFFFF !important;
    color: #111111 !important;
    padding: 10px 14px !important;
}

.stTextInput input:focus {
    border-color: #ADADAD !important;
    box-shadow: none !important;
}

.stTextInput label {
    color: #787774 !important;
    font-size: .82rem !important;
}

/* Button */

.stButton > button {
    background: #111111 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 4px !important;
    padding: 8px 20px !important;
    font-size: .85rem !important;
    transition: transform .12s ease;
}

.stButton > button:hover {
    background: #111111 !important;
}

.stButton > button:active {
    transform: scale(.98);
}

/* API key card */

.dp-key-card {
    background: #FFFFFF;
    border: 1px solid #EAEAEA;
    border-radius: 8px;
    padding: 28px 32px;
    margin-top: 1.5rem;
}

.dp-key-card h3 {
    font-family: 'Newsreader', serif;
    color: #111111;
}

.dp-key-card p {
    color: #787774;
    font-size: .85rem;
}

/* Scrollbar */

::-webkit-scrollbar {
    width: 4px;
}

::-webkit-scrollbar-track {
    background: transparent;
}

::-webkit-scrollbar-thumb {
    background: #DDDDD9;
    border-radius: 2px;
}

/* Thinking indicator */

.thinking-wrapper {
    width: 100%;
    display: flex;
    align-items: center;
    min-height: 48px;
}

.thinking-indicator {
    display: flex;
    gap: 6px;
}

.thinking-indicator span {
    width: 7px;
    height: 7px;
    background: #787774;
    border-radius: 50%;
    animation: dpBounce 1.2s infinite ease-in-out;
}

.thinking-indicator span:nth-child(2) {
    animation-delay: .2s;
}

.thinking-indicator span:nth-child(3) {
    animation-delay: .4s;
}

/* Animations */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes dpBounce {
    0%,80%,100% {
        transform: scale(.7);
        opacity: .35;
    }

    40% {
        transform: scale(1);
        opacity: 1;
    }
}

</style>
""", unsafe_allow_html=True)

# ─── System Prompt ───────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """Kamu adalah DapurPintar, asisten memasak berbahasa Indonesia yang berpengetahuan luas, ringkas, dan praktis.

Kepribadian:
- Bicara seperti koki berpengalaman yang mengajari teman — hangat tapi to-the-point
- Tidak bertele-tele, langsung ke inti jawaban
- Jangan gunakan emoji berlebihan. Boleh 1 emoji per respons jika sangat relevan, tapi tidak wajib
- Gunakan bahasa Indonesia yang natural dan mudah dipahami

Yang bisa kamu bantu:
1. Resep — berikan langkah yang jelas dengan bahan, takaran, dan waktu memasak
2. Teknik memasak — jelaskan cara yang benar (menumis, memanggang, merebus, dll.)
3. Substitusi bahan — jika bahan tidak ada, sarankan pengganti yang logis
4. Menu dari bahan yang tersedia — bantu pengguna memaksimalkan isi kulkas
5. Tips penyimpanan dan food safety — waktu simpan, cara menyimpan yang benar
6. Estimasi porsi — sesuaikan resep untuk jumlah orang tertentu

Format respons:
- Untuk resep: tulis Bahan lalu Langkah sebagai daftar bernomor
- Untuk pertanyaan singkat: jawab langsung dalam 2-4 kalimat
- Gunakan **bold** untuk nama bahan utama atau istilah teknis penting
- Ukuran: gunakan satuan yang familiar (sendok makan, cangkir, gram)

Batasan:
- Hanya menjawab topik seputar memasak, resep, bahan makanan, dan dapur
- Jika pertanyaan di luar topik dapur, tolak dengan sopan dan arahkan kembali ke topik memasak
"""

# ─── LLM Config ─────────────────────────────────────────────────────────────────
# temperature=0.7  — cukup kreatif untuk variasi resep, tidak terlalu acak
# max_tokens=2048  — cukup untuk resep lengkap dengan langkah detail
# top_p=0.9        — memberi ruang kosakata kuliner yang beragam
# streaming=True   — output muncul token per token, lebih responsif
LLM_CONFIG = dict(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=2048,
    model_kwargs={"top_p": 0.9},
    streaming=True,
)

# ─── Header ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dp-eyebrow">Asisten Dapur</div>
<div class="dp-title">DapurPintar</div>
<div class="dp-subtitle">Tanyakan resep, teknik memasak, atau ide menu dari bahan yang kamu punya.</div>
<hr class="dp-divider">
""", unsafe_allow_html=True)

# ─── API Key Gate ────────────────────────────────────────────────────────────────
if not groq_api_key:
    st.markdown("""
<div class="dp-key-card">
    <h3>Masukkan API Key</h3>
    <p>Diperlukan GROQ API Key untuk menjalankan chatbot ini.</p>
</div>
""", unsafe_allow_html=True)
    input_api_key = st.text_input("GROQ API Key", type="password", placeholder="gsk_...")
    if st.button("Mulai", key="submit_key"):
        if input_api_key:
            os.environ["GROQ_API_KEY"] = input_api_key
            groq_api_key = input_api_key
            st.rerun()
    st.stop()

# ─── LLM Client ─────────────────────────────────────────────────────────────────
client = ChatGroq(**LLM_CONFIG)

# ─── Chat History Init ───────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        SystemMessage(SYSTEM_PROMPT),
        AIMessage(
            "Halo! Saya DapurPintar. Tanyakan resep, teknik memasak, atau ide menu dari bahan yang kamu punya."
        )
    ]

# ─── Render History ──────────────────────────────────────────────────────────────
for msg in st.session_state["chat_history"]:
    if isinstance(msg, HumanMessage):
        with st.chat_message("human"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("ai"):
            st.markdown(msg.content)

# ─── User Input ──────────────────────────────────────────────────────────────────
user_input = st.chat_input("Tanya resep, bahan, atau teknik memasak...")
if not user_input:
    st.stop()

st.session_state["chat_history"].append(HumanMessage(user_input))
with st.chat_message("human"):
    st.markdown(user_input)

# ─── Streaming Response ──────────────────────────────────────────────────────────
# ─── Streaming Response ──────────────────────────────────────────────────────────
with st.chat_message("ai"):

    thinking_placeholder = st.empty()

    thinking_placeholder.markdown(
        """
        <div class="thinking-wrapper">
        <div class="thinking-indicator">
            <span></span>
            <span></span>
            <span></span>
        </div>
    </div>
        """,
        unsafe_allow_html=True,
    )

    response_placeholder = st.empty()
    response_text = ""

    first_chunk = True

    for chunk in client.stream(st.session_state["chat_history"]):

        if first_chunk:
            thinking_placeholder.empty()
            first_chunk = False

        if chunk.content:
            response_text += chunk.content
            response_placeholder.markdown(response_text)

st.session_state["chat_history"].append(
    AIMessage(response_text)
)