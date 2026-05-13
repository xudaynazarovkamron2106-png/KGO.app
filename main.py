import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="KGO APP-AI", layout="wide")

# --- [API ULASH] ---
if "KGO-API" in st.secrets:
    api_val = st.secrets["KGO-API"]
    genai.configure(api_key=api_val)
    
    # Modelni aniqlash (Eng oxirgi barqaror nomlar)
    try:
        # 1-urinish: Hozirgi eng standart nom
        model = genai.GenerativeModel('models/gemini-1.5-flash')
    except:
        try:
            # 2-urinish: Agar birinchisi o'xshamasa
            model = genai.GenerativeModel('models/gemini-pro')
        except:
            # 3-urinish: Eski format
            model = genai.GenerativeModel('gemini-pro')
else:
    st.error("🚨 KGO-API kaliti topilmadi!")
    st.stop()

# --- [DIZAYN] ---
st.markdown("""
<style>
    .stApp { background: #000; color: #00f2ff; font-family: sans-serif; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #00f2ff !important; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; width: 100%; border-radius: 10px; }
    .res-box { background: rgba(0,242,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid #00f2ff; }
</style>
""", unsafe_allow_html=True)

st.title("🌐 KGO GLOBAL APP-AI")

query = st.text_input("Ilova haqida so'rang:", placeholder="Masalan: Uzum Market haqida ma'lumot...")

if st.button("TAHLILNI BOSHLASH"):
    if query:
        with st.spinner("⚡ KGO AI qidirmoqda..."):
            try:
                # generate_content'ni ishga tushirish
                response = model.generate_content(query)
                st.markdown('<div class="res-box">', unsafe_allow_html=True)
                st.markdown("### 🤖 JAVOB:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Tizimda xatolik: {str(e)}")
                st.info("Maslahat: API kalitingiz Google AI Studio'da faol ekanligini tekshiring.")
    else:
        st.warning("Iltimos, biror narsa yozing!")

st.sidebar.write("---")
st.sidebar.write("👑 **KGO Group Exclusive**")
