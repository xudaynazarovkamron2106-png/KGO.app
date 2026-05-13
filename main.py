import streamlit as st
import google.generativeai as genai

# --- [1. SAHIFA KONFIGURATSIYASI] ---
st.set_page_config(
    page_title="KGO GLOBAL AI",
    page_icon="🇺🇿",
    layout="wide"
)

# --- [2. API ULASH] ---
if "Gemini-API-Key" in st.secrets:
    api_val = st.secrets["Gemini-API-Key"]
    genai.configure(api_key=api_val)
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("🚨 Secrets-da 'Gemini-API-Key' topilmadi!")
    st.stop()

# --- [3. MILLIY VA ZAMONAVIY DIZAYN (CSS)] ---
st.markdown("""
<style>
    /* Asosiy fon va shriftlar */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    .stApp {
        background-color: #001219;
        background-image: url("https://www.transparenttextures.com/patterns/oriental-tiles.png"); /* Milliy naqsh foni */
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
    }

    /* Assalomu alaykum bo'limi */
    .welcome-text {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #00f2ff;
        text-shadow: 2px 2px 10px rgba(0, 242, 255, 0.5);
        margin-bottom: 5px;
    }
    
    .uzb-sub {
        text-align: center;
        color: #00d9ff;
        font-size: 1.2rem;
        letter-spacing: 2px;
        margin-bottom: 40px;
    }

    /* Kiritish maydoni */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 2px solid #00f2ff !important;
        border-radius: 15px;
        padding: 15px;
        font-size: 18px;
    }

    /* Tugma dizayni */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #0072ff);
        color: #000 !important;
        font-weight: bold;
        border-radius: 50px;
        padding: 10px 30px;
        border: none;
        transition: 0.3s;
        width: 100%;
        font-size: 1.2rem;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 20px #00f2ff;
        transform: scale(1.02);
    }

    /* Javob bloki */
    .res-box {
        background: rgba(0, 0, 0, 0.6);
        border-left: 5px solid #00f2ff;
        padding: 25px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        color: #e0e0e0;
    }
    
    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        width: 100%;
        text-align: center;
        font-size: 12px;
        color: rgba(255,255,255,0.4);
    }
</style>
""", unsafe_allow_html=True)

# --- [4. SAYTNING KO'RINISHI] ---

# Tepadagi salomlashish
st.markdown('<h1 class="welcome-text">Assalomu alaykum</h1>', unsafe_allow_html=True)
st.markdown('<p class="uzb-sub">KGO GLOBAL APP-AI TIZIMIGA XUSH KELIBSIZ</p>', unsafe_allow_html=True)

# Markaziy qism
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    query = st.text_input("", placeholder="Qanday yordam bera olaman, Boss?")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("TAHLIL QILISH"):
        if query:
            with st.spinner("⚡ AI o'ylamoqda..."):
                try:
                    # Milliyroq tushuntirish so'raladi
                    full_prompt = f"Sen O'zbekistondagi eng aqlli AIsan. Foydalanuvchi savoli: {query}. Unga o'zbek tilida, juda tushunarli va professional javob ber."
                    response = model.generate_content(full_prompt)
                    
                    st.markdown('<div class="res-box">', unsafe_allow_html=True)
                    st.markdown("### 🤖 KGO AI JAVOBI:")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Xatolik: {e}")
        else:
            st.warning("Savol yozishni unutdingiz!")

# Sidebar - Qo'shimcha ma'lumot
with st.sidebar:
    st.markdown("<h2 style='color:#00f2ff'>KGO GROUP</h2>", unsafe_allow_html=True)
    st.write("Ushbu platforma O'zbekistonning eng ilg'or texnologiyalari asosida yaratilgan.")
    st.info("API Status: ONLINE ✅")
    st.write("---")
    st.write("🇺🇿 Biz bilan kelajak sari!")

# Footer
st.markdown('<div class="footer">© 2026 KGO Group | Powered by Gemini 1.5 Flash</div>', unsafe_allow_html=True)
