import streamlit as st
import os

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="Optical Communication Laboratory",
    layout="wide"
)

# ======================
# SESSION STATE
# ======================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ======================
# FORCE FULL NAVY THEME
# ======================
st.markdown("""
<style>

/* ===== ROOT ===== */
html, body, [class*="css"]  {
    background-color: #081a33 !important;
}

/* Main app */
.stApp {
    background-color: #081a33 !important;
}

/* Main content container */
.main, .block-container {
    background-color: #081a33 !important;
    color: #e6ecff;
}

/* Remove white gaps */
.block-container {
    padding-top: 0rem;
}

/* HEADER */
.header {
    background: linear-gradient(135deg, #0a2a5e, #103c8f);
    padding: 30px 60px;
    border-bottom-left-radius: 70px;
    border-bottom-right-radius: 70px;
}

/* NAV BUTTON */
button[kind="secondary"] {
    background: transparent !important;
    color: #ffffff !important;
    border: none !important;
    font-size: 16px;
    font-weight: 600;
}

button[kind="secondary"]:hover {
    color: #4fa3ff !important;
}

/* CARD */
.card {
    background: #0e2a55;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 12px 30px rgba(0,0,0,.35);
}

/* TITLES */
.section-title {
    font-size: 34px;
    font-weight: 700;
    color: #ffffff;
}

.subtitle {
    color: #ff6b6b;
    font-weight: 700;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER + NAVBAR
# ======================
st.markdown('<div class="header">', unsafe_allow_html=True)

col_logo, col_nav = st.columns([2, 6])

with col_logo:
    if os.path.exists("ocl_logo.png.jpeg"):
        st.image("ocl_logo.png.jpeg", width=80)

with col_nav:
    n1, n2, n3, n4 = st.columns(4)
    with n1:
        if st.button("About Us"):
            st.session_state.page = "about"
    with n2:
        if st.button("Our Teams"):
            st.session_state.page = "team"
    with n3:
        if st.button("Our Activity"):
            st.session_state.page = "activity"
    with n4:
        if st.button("Informations"):
            st.session_state.page = "info"

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
if st.session_state.page == "home":
    st.markdown("""
    <div style="padding:40px;">
        <p class="subtitle">MODULE</p>
        <h2 class="section-title">Our Module</h2>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
            <h4>Optical Fiber</h4>
            <p>Basic optical fiber transmission module.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <h4>WDM System</h4>
            <p>Wavelength Division Multiplexing experiment.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
            <h4>Optical Network</h4>
            <p>Optical access & backbone network module.</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.page == "about":
    st.header("About Us")
    st.write("Optical Communication Laboratory focuses on education and research in optical & photonic systems.")

elif st.session_state.page == "team":
    st.header("Our Teams")
    st.write("Lecturers, assistants, and researchers of OCL.")

elif st.session_state.page == "activity":
    st.header("Our Activity")
    st.write("Practicum, research, and academic activities.")

elif st.session_state.page == "info":
    st.header("Informations")
    st.write("Schedules, announcements, and updates.")
