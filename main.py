import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="KGO APP-AI", layout="wide")

# --- [KGO-API ULASH] ---
if "KGO-API" in st.secrets:
    api_val = st.secrets["KGO-API"]
    genai.configure(api_key=api_val)
    
    # 404 Xatosini yengish uchun bir nechta modelni tekshiramiz
    try:
        # 1-urinish: Eng yangi flash modeli
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
    except:
        try:
            # 2-urinish: Standart flash modeli
            model = genai.GenerativeModel('gemini-1.5-flash')
        except:
            # 3-urinish: Eng barqaror pro modeli
            model = genai.GenerativeModel('gemini-pro')
else:
    st.error("🚨 KGO Boss, 'KGO-API' kaliti topilmadi!")
    st.stop()

# --- [DIZAYN] ---
st.markdown("""
<style>
    .stApp { background: #000; color: #00f2ff; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #00f2ff !important; }
    .stButton>button { background: #00f2ff; color: #000; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.title("🌐 KGO GLOBAL APP-AI")

query = st.text_input("Ilova haqida so'rang:")

if st.button("TAHLIL QILISH"):
    if query:
        with st.spinner("⚡ KGO AI o'ylamoqda..."):
            try:
                # generate_content'dan oldin modelni tekshirib olamiz
                response = model.generate_content(query)
                st.markdown("---")
                st.markdown("### 🤖 KGO AI Javobi:")
                st.write(response.text)
            except Exception as e:
                # Agar hali ham 404 bersa, pro modeliga majburan o'tkazamiz
                st.warning("Flash modelida muammo, Pro modeliga ulanishga harakat qilinmoqda...")
                model_alt = genai.GenerativeModel('gemini-pro')
                response = model_alt.generate_content(query)
                st.write(response.text)
    else:
        st.warning("So'rov yozing!")
