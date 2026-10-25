import streamlit as st

# Page configurations
st.set_page_config(
    page_title="School No. 165 Minsk — English Project",
    page_icon="🏫",
    layout="wide"
)

# --- THEME & BACKGROUND GRADIENT SETTINGS ---
st.sidebar.header("🎨 Theme & Style Settings")

# Checkbox now defaults to TRUE (Starts dark automatically!)
dark_mode = st.sidebar.checkbox("🌙 Dark Mode (Default)", value=True)

# Sliders to control the animated gradient angles and speed
gradient_speed = st.sidebar.slider("⚡ Gradient Speed (seconds)", 5, 20, 12)
gradient_angle = st.sidebar.slider("📐 Gradient Angle (degrees)", 0, 360, 135)

# Dynamic CSS based on user selection — КРАСИВЫЕ И КОНТРАСТНЫЕ ЦВЕТА
if dark_mode:
    # High-contrast Cyber Dark Theme (Deep space black, violet-blue, neon teal)
    bg_color_1 = "#08090c"  # Глубокий темный основной фон
    bg_color_2 = "#1c1b35"  # Контрастный темно-фиолетовый
    bg_color_3 = "#0d2b35"  # Контрастный темно-бирюзовый
    text_color = "#f1f5f9"
    card_bg = "rgba(255, 255, 255, 0.05)"
    border_color = "rgba(255, 255, 255, 0.12)"
else:
    # High-contrast Light Theme (Soft sky blue, pastel pink, clean white)
    bg_color_1 = "#e0f2fe"  # Нежно-голубой
    bg_color_2 = "#fce7f3"  # Нежно-розовый
    bg_color_3 = "#ffffff"  # Чистый белый
    text_color = "#0f172a"
    card_bg = "rgba(0, 0, 0, 0.03)"
    border_color = "rgba(0, 0, 0, 0.08)"

# Injecting Custom CSS for Background Gradient, Text Colors, and Content Containers
sidebar_text_color = "#ffffff" if dark_mode else "#0f172a"

st.markdown(f"""
    <style>
    /* Main App Background with Controllable Animated High-Contrast Gradient */
    .stApp {{
        background: linear-gradient({gradient_angle}deg, {bg_color_1}, {bg_color_2}, {bg_color_3}, {bg_color_1});
        background-size: 300% 300%;
        animation: gradientAnimation {gradient_speed}s ease-in-out infinite;
        color: {text_color} !important;
        transition: background 0.5s ease, color 0.5s ease;
    }}
    
    @keyframes gradientAnimation {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}

    /* Text color for main content area */
    .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label, .stApp li {{
        color: {text_color} !important;
    }}

    /* Perfect contrast fix for the Sidebar container depending on Light/Dark mode */
    [data-testid="stSidebar"] {{
        background-color: {"#11131c" if dark_mode else "#f1f5f9"} !important;
        border-right: 1px solid {border_color};
    }}
    
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span, 
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] strong {{
        color: {sidebar_text_color} !important;
    }}

    /* Styling the content blocks to look like elegant glass cards */
    .custom-card {{
        background: {card_bg};
        padding: 22px;
        border-radius: 16px;
        border: 1px solid {border_color};
        margin-bottom: 18px;
        backdrop-filter: blur(8px);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.2);
    }}
    
    .custom-card, .custom-card b, .custom-card li {{
        color: {text_color} !important;
    }}

    /* Стиль для интерактивной ссылки на главный сайт школы */
    .school-link-card {{
        display: block;
        text-decoration: none !important;
        background: {card_bg};
        padding: 20px;
        border-radius: 12px;
        border: 2px solid {border_color};
        text-align: center;
        margin-top: 25px;
        transition: transform 0.3s ease, background 0.3s ease;
        position: relative;
        overflow: hidden;
    }}

    /* Эффект увеличения и запуск анимации контура при наведении */
    .school-link-card:hover {{
        transform: translateY(-3px);
        background: rgba(255, 255, 255, 0.08);
        animation: borderGlow 1.2s ease-in-out forwards;
    }}

    .school-link-card h3, .school-link-card p {{
        color: {text_color} !important;
        margin: 0 !important;
    }}
    
    .school-link-card p {{
        opacity: 0.8;
        margin-top: 5px !important;
    }}

    /* Анимация однократной прокрутки цветов по границе (фиолетовый -> бирюзовый) */
    @keyframes borderGlow {{
        0% {{
            border-color: {border_color};
            box-shadow: 0 0 0 rgba(0,0,0,0);
        }}
        25% {{
            border-color: #1c1b35; /* Фиолетовый */
            box-shadow: 0 0 10px rgba(28, 27, 53, 0.5);
        }}
        75% {{
            border-color: #0d2b35; /* Бирюзовый */
            box-shadow: 0 0 15px rgba(13, 43, 53, 0.7);
        }}
        100% {{
            border-color: {border_color};
            box-shadow: 0 0 5px rgba(255, 255, 255, 0.1);
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- MAIN WEBSITE CONTENT ---

# Main Title
st.title("🏫 State Institution of Education «Secondary School No. 165 of Minsk»")
st.write("---")

# Sidebar for Quick Facts & Contacts
st.sidebar.header("📌 Quick Profile")
st.sidebar.markdown("""
**📍 Address:**  
6 Gazety Zvyazda Avenue,  
Moskovsky District, Minsk, Belarus  

**📞 Reception Desk:**  
+375 17 368-99-88  

**📧 Official Email:**  
sch165@minskedu.gov.by  

**👤 Administration:**  
Principal — *Natallia Anatolievna Zelkovskaya*
""")

# Creating Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["👋 Welcome", "🏛️ Culture & Traditions", "🏆 Sports & Activities", "📅 Opening Hours"])

with tab1:
    st.header("About Our School")
    st.info("**School Motto:** Accept a child as they are; teach and raise them to be useful to society and capable of self-realization in life.")
    
    st.markdown("""
    <div class="custom-card">
        Secondary School No. 165 is a modern educational institution located in the heart of the Moskovsky district in Minsk. 
        Our school focuses on providing high-quality general education, fostering functional literacy, and encouraging students to become active, global citizens.
    </div>
    """, unsafe_allow_html=True)
    
    # Key school metrics
    col1, col2, col3 = st.columns(3)
    col1.metric(label="District", value="Moskovsky")
    col2.metric(label="Swimming Pool", value="Available 🏊‍♂️")
    col3.metric(label="Dress Code", value="Business Style 👔")

    # Интерактивная карточка-ссылка с неоновой анимацией контура
    st.markdown("""
        <a href="https://minsk.edu.by" target="_blank" class="school-link-card">
            <h3>🌐 Visit Official School Website</h3>
            <p>Click here to explore the official portal of Secondary School No. 165</p>
        </a>
    """, unsafe_allow_html=True)

with tab2:
    st.header("Cultural Heritage")
    st.subheader("🌾 Ethnographic Museum «Da rodnyh vytokau» (To Native Roots)")
    st.markdown("""
    <div class="custom-card">
        The true pride of our school is our very own ethnographic museum. Here, students learn about the rich history, 
        culture, and traditions of the Belarusian people. The museum showcases ancient household items, traditional clothing, 
        and crafts made by ancestors. It is actively used for open history classes and cultural events.
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("🎗️ Youth Organizations")
    st.write("Our students actively participate in nation-wide youth communities:")
    st.markdown("- BRPO (Belarusian Republican Pioneer Organization)")
    st.markdown("- BRSM (Belarusian Republican Youth Union)")

with tab3:
    st.header("Sports Life & Extracurriculars")
    st.markdown("""
    <div class="custom-card">
        Health and physical education are top priorities at School No. 165. We offer great facilities for students to stay fit:
        <ul>
            <li><b>🏊‍♂️ Indoor Swimming Pool:</b> Regular swimming lessons are integrated into our physical education curriculum alongside open recreational hours.</li>
            <li><b>🥋 Sports Club «Champion»:</b> Features popular training sections including Karate, Mini-Football, and Checkers. Our students frequently win regional athletic competitions.</li>
            <li><b>🎭 Creative Development:</b> Students can join elective clubs focusing on English language fluency, ballroom dancing, and arts & crafts.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.header("School Schedule & Operation")
    
    st.markdown("""

    | Working Days | Opening Hours |
    | :--- | :--- |
    | **Monday — Friday** | 07:00 AM – 08:00 PM |
    | **Saturday (6th School Day)** | 09:00 AM – 06:00 PM |
    | **Sunday** | Closed |
    """)
    
    st.warning("⚠️ **Notice for Parents:** Student grading performance and attendance tracking are managed digitally via the Schools.by platform.")

# Footer
st.write("---")
st.caption("This project was developed to showcase modern school web presentation technologies for an English language assignment.")

