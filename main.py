import streamlit as st
import google.generativeai as genai

# --- [SAHIFA SOZLAMALARI] ---
st.set_page_config(page_title="KGO APP-AI", layout="wide")

# --- [API ULASH - KGO-API NOMIGA MOSLANDI] ---
if "KGO-API" in st.secrets:
    api_val = st.secrets["KGO-API"]
    genai.configure(api_key=api_val)
    # Modelni yuklash
    model = genai.GenerativeModel('gemini-1.5-flash')
else:
    st.error("Xato: Secrets-da 'KGO-API' nomi bilan kalit topilmadi!")
    st.stop()

# --- [CYBER DIZAYN] ---
st.markdown("""
<style>
    .stApp { background: #000; color: #00f2ff; }
    input { background-color: #111 !important; color: #00f2ff !important; border: 1px solid #00f2ff !important; }
    .stButton>button { background: #00f2ff; color: black; font-weight: bold; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.title("🌐 KGO GLOBAL APP-AI")

query = st.text_input("Ilova nomini kiriting:")

if st.button("TAHLIL QILISH"):
    if query:
        try:
            with st.spinner("AI qidirmoqda..."):
                response = model.generate_content(f"Iltimos, '{query}' ilovasi nima ekanligi va uni qanday ishlatish haqida o'zbekcha ma'lumot ber.")
                st.success("Tahlil yakunlandi!")
                st.info(response.text)
        except Exception as e:
            st.error(f"AI bilan bog'lanishda xato: {str(e)}")
    else:
        st.warning("Iltimos, biror narsa yozing!")
