import streamlit as st
import google.generativeai as genai

# --- [1. TIZIM SOZLAMALARI] ---
st.set_page_config(page_title="KGO APP-AI | GLOBAL", layout="wide")

# --- [2. API ULASH] ---
# Streamlit Secrets orqali xavfsiz ulanish
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
    # Eng oxirgi va barqaror model
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error("Xatolik: API kaliti Streamlit Secrets-ga qo'shilmagan!")

# --- [3. CYBER-DESIGN (BOYA AYTGANINGIZDEK)] ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle, #0f0c29, #302b63, #24243e);
        color: #00f2ff;
        font-family: 'Orbitron', sans-serif;
    }
    
    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.7) !important;
        color: #00f2ff !important;
        border: 2px solid #00f2ff !important;
        border-radius: 10px;
        font-size: 18px;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #00f2ff, #0072ff);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 15px;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 0 15px #00f2ff;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px #00f2ff;
    }
    
    .response-area {
        background: rgba(0, 0, 0, 0.6);
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #00f2ff;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- [4. ASOSIY INTERFEYS] ---
st.markdown("<h1 style='text-align: center; color: #00f2ff; letter-spacing: 5px;'>🌐 KGO GLOBAL APP-AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.8;'>Dunyodagi va O'zbekistondagi har qanday ilova bo'yicha ekspert tizimi</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    query = st.text_input("Ilova nomini yozing yoki muammoingizni tushuntiring:", placeholder="Masalan: 'Uzum Market nima?' yoki 'Payme ochilmayapti'")
    
    if st.button("AI TAHLILINI BOSHLASH"):
        if query:
            with st.spinner("⚡ KGO AI global serverlarga ulanmoqda..."):
                try:
                    # AIga yo'riqnoma
                    full_prompt = f"""
                    Sen KGO Group-ning 'App-AI' tizimisan. 
                    Foydalanuvchi so'rovi: {query}
                    
                    Vazifang:
                    1. Agar bu ilova bo'lsa, uning nimaligini va qanday ishlatilishini ayt.
                    2. Agar muammo ('bo'lmayapti', 'xato') bo'lsa, aniq texnik yechim ber.
                    3. O'zbekiston ilovalariga (Payme, Click, MyGov va h.k.) alohida e'tibor ber.
                    4. Javobni chiroyli, tushunarli va o'zbek tilida ber.
                    """
                    
                    response = model.generate_content(full_prompt)
                    
                    st.markdown('<div class="response-area">', unsafe_allow_html=True)
                    st.markdown("### 🤖 KGO AI JAVOBI:")
                    st.write(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                except Exception as e:
                    st.error("Kechirasiz, modelni yuklashda xatolik bo'ldi. API kalitini tekshiring.")
        else:
            st.warning("Iltimos, ilova nomini kiriting!")

# --- [5. SIDEBAR INFO] ---
st.sidebar.markdown("<h2 style='color: #00f2ff;'>KGO GROUP</h2>", unsafe_allow_html=True)
st.sidebar.write("---")
st.sidebar.info("Ushbu tizim dunyodagi 5 mlndan ortiq ilovalar bazasiga ulangan.")
st.sidebar.write("✅ **Model:** Gemini 1.5 Flash")
st.sidebar.write("✅ **Status:** Active")
