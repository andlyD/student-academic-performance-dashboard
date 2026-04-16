import streamlit as st
import streamlit.components.v1 as components

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
# GLOBAL STYLES (SCOPED FIX)
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] > .main {
    background: #f6f7fb !important;
}

/* SIDEBAR BACKGROUND */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebar"] > div:first-child {
    background: linear-gradient(180deg, #4b1fcf 0%, #3d18b4 100%) !important;
}

/* SIDEBAR WIDTH */
[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 265px !important;
}
[data-testid="stSidebar"][aria-expanded="false"] {
    min-width: 82px !important;
}

/* ONLY STYLE SIDEBAR BUTTONS (IMPORTANT FIX) */
section[data-testid="stSidebar"] div.stButton > button {
    width: 100% !important;
    border-radius: 12px !important;
    padding: 0.8rem 1rem !important;
    background: rgba(255,255,255,0.15) !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    margin-bottom: 0.4rem !important;
    color: white !important;
    transition: 0.2s ease !important;
}

/* TEXT INSIDE SIDEBAR BUTTON */
section[data-testid="stSidebar"] div.stButton > button * {
    color: white !important;
}

/* HOVER */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: rgba(255,255,255,0.3) !important;
    transform: translateX(3px);
}

/* ACTIVE */
section[data-testid="stSidebar"] div.stButton > button.nav-btn-active {
    background: white !important;
}

section[data-testid="stSidebar"] div.stButton > button.nav-btn-active * {
    color: #2e167e !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    st.markdown("### Main Menu")

    nav_items = [
        ("🏠 Main Dashboard", "Dashboard"),
        ("🔎 Overview", "Overview"),
        ("💻 Performance Analysis", "Performance Analysis"),
        ("🙋 Know Yourself", "Know Yourself"),
    ]

    for label, page in nav_items:
        if st.button(label, key=page):
            st.session_state.current_page = page
            st.rerun()

    # ACTIVE BUTTON SCRIPT (FIXED MATCHING)
    components.html(f"""
    <script>
    const buttons = window.parent.document.querySelectorAll(
        'section[data-testid="stSidebar"] div.stButton > button'
    );

    buttons.forEach(btn => {{
        btn.classList.remove('nav-btn-active');
        if (btn.innerText.trim().includes("{st.session_state.current_page}")) {{
            btn.classList.add('nav-btn-active');
        }}
    }});
    </script>
    """, height=0)

    # ═══════════════════════════════════
    # YOUR TEAM FOOTER (RESTORED)
    # ═══════════════════════════════════
    st.markdown("""
    <div style="
        margin-top:20px;
        padding:12px;
        border-radius:12px;
        background:rgba(255,255,255,0.1);
        color:white;
        font-size:13px;
    ">
    <b>👨‍💻 Dashboard Developers</b><br><br>
    Andly Danny Anafiah<br>
    <span style="opacity:0.7;">0137461</span><br><br>
    Bayu Fatwa Negara Alias<br>
    <span style="opacity:0.7;">0137466</span><br><br>
    Muhamad Roslan Abbas<br>
    <span style="opacity:0.7;">0137513</span>
    </div>
    """, unsafe_allow_html=True)

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
