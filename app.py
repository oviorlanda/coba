import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Optical Communication Laboratory",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
body {
    background-color: #0b132b;
}

.main {
    background-color: #0b132b;
    color: white;
}

/* Top navigation buttons */
div.stButton > button {
    background-color: #1c77ff;
    color: white;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
    border: none;
}

div.stButton > button:hover {
    background-color: #4fa3ff;
    color: black;
}

/* Card style */
.card {
    background-color: rgba(28, 119, 255, 0.15);
    padding: 25px;
    border-radius: 15px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# LOGO + TITLE
# ======================
col_logo, col_title = st.columns([1, 6])
with col_logo:
    st.image("ocl_logo.png.jpeg", width=130)
with col_title:
    st.markdown("""
    <h1 style='color:#4fa3ff;'>Optical Communication Laboratory</h1>
    <h4 style='color:#b3c7ff;'>Telkom University Bandung</h4>
    """, unsafe_allow_html=True)

st.markdown("---")

# ======================
# TOP NAVIGATION
# ======================
nav = st.columns(5)

with nav[0]:
    home = st.button("HOME")
with nav[1]:
    about = st.button("ABOUT US")
with nav[2]:
    team = st.button("OUR TEAM")
with nav[3]:
    activity = st.button("OUR ACTIVITY")
with nav[4]:
    info = st.button("INFORMATIONS")

# ======================
# PAGE CONTENT
# ======================
if home:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Welcome to OCL")
    st.write("""
    Optical Communication Laboratory (OCL) focuses on education,
    research, and innovation in optical fiber communication systems.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif about:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("About Us")
    st.write("""
    OCL is an academic laboratory under Telkom University
    that supports learning and research in photonics
    and optical communication.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif team:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Our Team")
    st.write("""
    Our team consists of lecturers, laboratory assistants,
    and students passionate about optical communication.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif activity:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Our Activity")
    st.write("""
    - Practicum sessions  
    - Research projects  
    - Academic discussions  
    - Optical system simulations
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif info:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Informations")
    st.write("""
    📌 Laboratory schedules  
    📌 Announcements  
    📌 Research updates
    """)
    st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.header("Welcome to Optical Communication Laboratory")
    st.write("Please select a menu above to explore.")
    st.markdown("</div>", unsafe_allow_html=True)

