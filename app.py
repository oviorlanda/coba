import streamlit as st

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(layout="wide", page_title="Optical Communication Laboratory")

# ======================
# CUSTOM CSS
# ======================
st.markdown("""
<style>
/* Remove default padding */
.block-container {
    padding-top: 0rem;
    padding-bottom: 2rem;
}

/* HEADER */
.header {
    background: linear-gradient(135deg, #1f7ae0, #4fa3ff);
    padding: 30px 60px;
    border-bottom-left-radius: 60px;
    border-bottom-right-radius: 60px;
}

/* NAVBAR */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* MENU */
.menu a {
    margin-left: 30px;
    font-weight: 600;
    color: white;
    text-decoration: none;
}

.menu a:hover {
    color: #ffdd57;
}

/* SECTION TITLE */
.section-title {
    margin-top: 50px;
    font-size: 32px;
    font-weight: 700;
}

/* CARD */
.card {
    background: white;
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

body {
    background-color: #f4f7fc;
}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<div class="header">
    <div class="navbar">
        <div>
            <img src="ocl_logo.png.jpeg" width="90">
        </div>
        <div class="menu">
            <a href="#home">About Us</a>
            <a href="#team">Our Teams</a>
            <a href="#activity">Our Activity</a>
            <a href="#info">Informations</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================
# CONTENT
# ======================
st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown("""
<div style="padding:60px;">
    <p style="color:#cc3b3b; font-weight:600;">MODULE</p>
    <h2 class="section-title">Our Module</h2>
</div>
""", unsafe_allow_html=True)

# MODULE CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h4>Optical Fiber</h4>
        <p>Basic optical fiber transmission module.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h4>WDM System</h4>
        <p>Wavelength Division Multiplexing experiment.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h4>Optical Network</h4>
        <p>Optical access & backbone network module.</p>
    </div>
    """, unsafe_allow_html=True)
