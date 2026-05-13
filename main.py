import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="KGO APP-AI", layout="wide")

# --- [API ULASH] ---
if "KGO-API" in st.secrets:
    api_val = st.secrets["KGO-API"]
    genai.configure(api_key=api_val)
    
    # 404 XATOSINI YO'QOTISH UCHUN ENG BARQAROR MODEL
    # models/gemini-pro - bu hamma joyda ishlaydigan klassika
    try:
        model = genai.GenerativeModel('gemini-pro')
    except:
        st.error("Modelni yuklab bo'lmadi. API kalitni tekshiring.")
        st.stop()
else:
    st.error("🚨 KGO-API kaliti topilmadi!")
    st.stop()

# --- [CYBER DIZAYN] ---
st.markdown("""
<style>
    .stApp { background: #000; color: #00f2ff; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #00f2ff !important; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; width: 100%; }
    .res-box { background: rgba(0,242,255,0.1); padding: 20px; border-radius: 15px; border: 1px solid #00f2ff; }
</style>
""", unsafe_allow_html=True)

st.title("🌐 KGO GLOBAL APP-AI")

query = st.text_input("Ilova haqida so'rang:")

if st.button("TAHLIL QILISH"):
    if query:
        with st.spinner("⚡ KGO AI ishlamoqda..."):
            try:
                # Oddiy va aniq chaqiruv
                response = model.generate_content(query)
                st.markdown('<div class="res-box">', unsafe_allow_html=True)
                st.markdown("### 🤖 JAVOB:")
                st.write(response.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Xatolik yuz berdi: {str(e)}")
                st.info("Eslatma: Agar xato davom etsa, Google AI Studio'da yangi API key olib ko'ring.")
    else:
        st.warning("Iltimos, so'rov yozing!")
