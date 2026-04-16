import streamlit as st
import streamlit.components.v1 as components
import os

from sidebarMenu.Overview import show_overview
from sidebarMenu.KnowYourself import main as show_know_yourself
from sidebarMenu.DashboardPage import render_dashboard, render_performance_analysis

# ══════════════════════════════════════════════════════════════════════════════
# PAGE CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Academic Performance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
# SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

# ══════════════════════════════════════════════════════════════════════════════
# GLOBAL STYLES (FIXED)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* Hide default menu */
#MainMenu, footer { visibility: hidden; }

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] > .main {
    background: #f6f7fb !important;
}

/* ───────── SIDEBAR FIX (CRITICAL) ───────── */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #4b1fcf 0%, #3d18b4 100%) !important;
}

/* Sidebar width */
[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 265px !important;
    max-width: 265px !important;
}

[data-testid="stSidebar"][aria-expanded="false"] {
    min-width: 82px !important;
    max-width: 82px !important;
}

/* FORCE ALL SIDEBAR TEXT WHITE */
[data-testid="stSidebar"],
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] button,
[data-testid="stSidebar"] button * {
    color: #FFFFFF !important;
}

/* Remove default nav */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* NAV BUTTONS */
[data-testid="stSidebar"] button {
    width: 100% !important;
    border-radius: 12px !important;
    padding: 0.8rem 1rem !important;
    background: rgba(255,255,255,0.15) !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    margin-bottom: 0.4rem !important;
    transition: 0.2s ease !important;
}

/* Hover */
[data-testid="stSidebar"] button:hover {
    background: rgba(255,255,255,0.3) !important;
    transform: translateX(3px);
}

/* Active button */
[data-testid="stSidebar"] button.nav-btn-active {
    background: #FFFFFF !important;
}

[data-testid="stSidebar"] button.nav-btn-active * {
    color: #2e167e !important;
    font-weight: 700 !important;
}

/* CONTENT WIDTH */
.block-container {
    max-width: 1200px !important;
    margin: auto !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    st.markdown('<div style="font-size:0.75rem; opacity:0.7;">MAIN MENU</div>', unsafe_allow_html=True)

    nav_items = [
        ("🏠 Main Dashboard", "Dashboard"),
        ("🔎 Overview", "Overview"),
        ("💻 Performance Analysis", "Performance Analysis"),
        ("🙋 Know Yourself", "Know Yourself"),
    ]

    for label, page in nav_items:
        if st.button(label):
            st.session_state.current_page = page
            st.rerun()

    # Highlight active button (JS)
    components.html(f"""
    <script>
    const buttons = window.parent.document.querySelectorAll('[data-testid="stSidebar"] button');
    buttons.forEach(btn => {{
        btn.classList.remove('nav-btn-active');
        if (btn.innerText.includes("{st.session_state.current_page}")) {{
            btn.classList.add('nav-btn-active');
        }}
    }});
    </script>
    """, height=0)

# ══════════════════════════════════════════════════════════════════════════════
# MAIN CONTENT
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.current_page == "Dashboard":
    render_dashboard()

elif st.session_state.current_page == "Overview":
    show_overview()

elif st.session_state.current_page == "Performance Analysis":
    render_performance_analysis()

elif st.session_state.current_page == "Know Yourself":
    show_know_yourself()

else:
    st.error("Page not found")
