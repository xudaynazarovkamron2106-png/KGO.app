import streamlit as st
import time

# --- [1. CYBER-PUNK INTERFACE DESIGN] ---
st.set_page_config(page_title="KGO GLOBAL - №1 AI", layout="wide", page_icon="👑")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@400;700&family=Montserrat:wght@300;600&display=swap');
    
    .stApp {
        background: radial-gradient(circle at center, #001d21 0%, #000000 100%);
        color: #00f2ff;
        font-family: 'Montserrat', sans-serif;
    }
    
    .mega-header {
        text-align: center;
        font-family: 'Syncopate', sans-serif;
        font-size: 4.5rem;
        font-weight: 700;
        background: linear-gradient(180deg, #00f2ff, #0072ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 50px rgba(0, 242, 255, 0.5);
    }

    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.9) !important;
        color: #ffffff !important;
        border: 3px solid #00f2ff !important;
        border-radius: 25px;
        height: 70px;
        font-size: 22px;
        padding-left: 25px;
    }

    .stButton>button {
        background: linear-gradient(45deg, #00f2ff, #004e56);
        color: white;
        border: none;
        border-radius: 30px;
        height: 65px;
        font-weight: 900;
        font-size: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 242, 255, 0.3);
        transition: 0.4s;
    }

    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 0 50px #00f2ff;
    }

    .info-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid #00f2ff;
        padding: 40px;
        border-radius: 30px;
        margin-top: 40px;
        backdrop-filter: blur(15px);
        box-shadow: inset 0 0 20px rgba(0, 242, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- [2. THE MEGA DATASET (WORLD KNOWLEDGE)] ---
# Bu yerga dunyodagi deyarli barcha mashhur sayt va ilovalarni qo'shdik
MEGA_DATASET = {
    # IJTIMOIY TARMOQLAR (SOCIAL MEDIA)
    "instagram": "📸 **INSTAGRAM MASTER GUIDE:**\n1. **Tugma:** Story qo'shish tepada '+'. Profil sozlamalari o'ng pastda.\n2. **Akkauntni o'chirish:** Settings -> Accounts Center -> Personal Details -> Ownership.\n3. **Reels yuklash:** Markazdagi '+' tugmasi orqali 'Reels' bo'limini tanlang.\n4. **Maxfiylik:** Settings -> Privacy orqali profilingizni yopishingiz (Private) mumkin.",
    "telegram": "✈️ **TELEGRAM PRO:**\n1. **Yashirin chat:** Kontaktni oching -> Ismi ustiga bosing -> Uch nuqta -> 'Start Secret Chat'.\n2. **Kanal ochish:** Qalam belgisi (pastda) -> New Channel.\n3. **Ikki bosqichli tekshiruv:** Settings -> Privacy and Security -> Two-Step Verification.\n4. **Tezkor qidiruv:** Tepada qidiruv belgisiga biron so'z yoki @username yozing.",
    "facebook": "📘 **FACEBOOK GUIDE:**\n1. **Profilni himoyalash:** Settings -> Profile Locking.\n2. **Sahifa (Page) ochish:** Menu -> Pages -> Create.\n3. **Guruhlar:** Pastki menyuda 'Groups' bo'limi orqali kirasiz.",
    "tiktok": "🎵 **TIKTOK:**\n1. **Video yuklash:** '+' belgisi markazda.\n2. **Effektlar:** '+' ni bosgandan keyin chapda 'Effects' bo'limi.\n3. **Jonli efir:** 1000 ta obunachidan keyin '+' menyusida 'LIVE' tugmasi ochiladi.",
    
    # O'ZBEKISTON ILAVALARI (UZB ECOSYSTEM)
    "payme": "💳 **PAYME:**\n1. **Karta qo'shish:** 'Mening kartalarim' -> '+'.\n2. **O'tkazma:** 'O'tkazmalar' tugmasi markazda turadi. Karta raqamini kiriting.\n3. **Monitoring:** Pastki menyuda 'Monitoring' bo'limida barcha xarajatlar ko'rinadi.",
    "click": "🖱 **CLICK UP:**\n1. **Karta ulash:** 'Kartalarim' bo'limi.\n2. **QR To'lov:** Asosiy ekranda katta QR skaner tugmasi bor.\n3. **Click hamyon:** Pulni kartasiz hamyonda saqlash imkoniyati.",
    "uzum": "🍇 **UZUM MARKET:**\n1. **Buyurtma:** Mahsulotni tanlang -> 'Savatga' -> 'Rasmiylashtirish'.\n2. **To'lov:** Karta orqali yoki topshirish punktida to'lash mumkin.\n3. **Punktlar:** Buyurtma berishda xaritadan uyingizga yaqin punktni tanlang.",
    "my.gov.uz": "🏢 **YAGONA PORTAL (EPIGU):**\n1. **Kirish:** OneID orqali amalga oshiriladi.\n2. **Xizmatlar:** 'Barcha xizmatlar' bo'limida passport, diplom, jarima kabilarni topasiz.",
    
    # GLOBAL SERVISLAR (GLOBAL SERVICES)
    "google": "🔍 **GOOGLE:** Dunyo qidiruv tizimi. Qidiruvda 'site:sayt.com' yozsangiz, faqat o'sha saytdan qidiradi.",
    "youtube": "🎥 **YOUTUBE:** Video tagidagi 'Save' tugmasi orqali keyinroq ko'rish ro'yxatiga qo'shasiz. 'Library' bo'limi pastki o'ngda.",
    "chatgpt": "🤖 **CHATGPT:** OpenAI tomonidan yaratilgan AI. Matn yozish, kod yozish va maslahat berish uchun ishlatiladi.",
    "canva": "🎨 **CANVA:** Dizayn yaratish ilovasi. '+' tugmasini bosib, tayyor shablonlardan foydalanishingiz mumkin.",
    "capcut": "🎬 **CAPCUT:** Video tahrirlash. 'New Project' tugmasini bosib, galereyadan video tanlaysiz.",
    
    # TEXNIK YORDAM (TECHNICAL HELP)
    "iphone": "🍎 **IPHONE:** Skrinshot olish uchun: Yon tugma va ovoz balandlatish tugmasini birga bosing.",
    "android": "🤖 **ANDROID:** Ilovani majburiy to'xtatish: Settings -> Apps -> Ilovani tanlang -> Force Stop.",
    "wifi": "📶 **WIFI:** Parolni bilish: Router sozlamalari odatda 192.168.1.1 manzilida bo'ladi.",
    
    # KGO EXCLUSIVE
    "salom": "Assalomu alaykum, KGO Boss! Biz O'zbekistonda №1 AI tizimmiz. Qaysi ilova yoki tugmani o'rgatishimni xohlaysiz?",
    "kgo": "👑 **KGO GLOBAL:** Bu O'zbekistonning eng kuchli, hech qanday API-larsiz 0 dan qurilgan mustaqil intellektual tizimidir!",
}

# --- [3. SEARCH ENGINE LOGIC] ---
def search_in_mega_brain(query):
    query = query.lower().strip()
    found_info = []
    
    # Har bir so'zni kalit so'zlar bilan tekshirish
    for key, value in MEGA_DATASET.items():
        if key in query:
            found_info.append(value)
            
    if found_info:
        return "\n\n---\n\n".join(found_info)
    else:
        return "⚠️ **MA'LUMOT TOPILMADI:** Boss, hozircha bu ilova bazamda yo'q. Iltimos, pastdagi bo'limdan uni AIga o'rgating!"

# --- [4. WEB INTERFACE] ---
st.markdown('<h1 class="mega-header">ASSALOMU ALAYKUM</h1>', unsafe_allow_html=True)
st.write("<p style='text-align:center; color:#00f2ff; font-size:1.5rem;'>KGO GLOBAL - O'ZBEKISTONNING №1 MUSTAQIL AI TIZIMI</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    user_q = st.text_input("", placeholder="Qaysi sayt, ilova yoki tugmani qidiryapsiz? (Masalan: Instagram, Payme)")
    
    if st.button("KGO MEGA BRAIN - TAHLIL"):
        if user_q:
            with st.spinner("⚡ MEGA-DATA TAHLIL QILINMOQDA..."):
                time.sleep(1) # Tezkor tahlil
                response = search_in_mega_brain(user_q)
                st.markdown(f'<div class="info-card"><h2>🤖 KGO AI YO\'RIQNOMASI:</h2><hr><p style="font-size:1.3rem;">{response}</p></div>', unsafe_allow_html=True)
        else:
            st.warning("Savol yozing, Sherik!")

# --- [5. ADMIN - AI-GA DUNYONI O'RGATISH] ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
with st.expander("🛠 AI GA YANGI ILAVALARNI O'RGATISH (BOSS PANEL)"):
    st.write("Bu bo'lim orqali AI bazasini cheksiz kengaytirish mumkin:")
    app_name = st.text_input("Ilova yoki Sayt nomi:")
    app_guide = st.text_area("To'liq yo'riqnoma (tugmalar qayerdaligi):")
    if st.button("BAZAGA QO'SHISH"):
        if app_name and app_guide:
            MEGA_DATASET[app_name.lower()] = f"📌 **{app_name.upper()}:** {app_guide}"
            st.success(f"✅ Bajarildi! AI endi '{app_name}' haqida hamma narsani biladi.")

# --- [6. FOOTER] ---
st.markdown("<hr style='border:1px solid #00f2ff; opacity:0.2;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:rgba(0,242,255,0.4);'>© 2026 KGO Group Enterprise | №1 AI in Uzbekistan | No API</p>", unsafe_allow_html=True)
