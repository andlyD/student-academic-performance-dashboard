import streamlit as st
import streamlit.components.v1 as components
import os
from sidebarMenu.Overview import show_overview
from sidebarMenu.KnowYourself import main as show_know_yourself
from sidebarMenu.DashboardPage import render_dashboard, render_performance_analysis, explore_button, CGPA_COLORS, CGPA_ORDER
from components.home_lottie import lottie_students, lottie_client

# ══════════════════════════════════════════════════════════════════════════════
#  PAGE CONFIG
# ══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Academic Performance Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════════════════════════
if "current_page" not in st.session_state:
    st.session_state.current_page = "Dashboard"

if "_nav_target" in st.session_state:
    st.session_state.current_page = st.session_state.pop("_nav_target")

if "_scroll_anchor" not in st.session_state:
    st.session_state._scroll_anchor = None

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES
# ══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

/* ── Base & Background ── */
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
#MainMenu, footer { visibility: hidden; }

body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewBlockContainer"] {
    background: #FFFFFF !important;
}

[data-testid="stAppViewContainer"] > .main {
    background: #f6f7fb !important;
}

header, [data-testid="stHeader"] {
    visibility: visible !important;
    background: transparent !important;
    height: 0 !important;
}

/* ── Sidebar Toggle Button ── */
[data-testid="collapsedControl"] {
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 99999 !important;
    display: block !important;
}

[data-testid="collapsedControl"] button {
    width: 42px !important;
    height: 42px !important;
    border-radius: 12px !important;
    border: none !important;
    background: #4b1fcf !important;
    color: #ffffff !important;
    box-shadow: 0 6px 18px rgba(75,31,207,0.30) !important;
}

[data-testid="collapsedControl"] button:hover {
    background: #3d18b4 !important;
}

/* ── Sidebar Container ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #4b1fcf 0%, #3d18b4 100%) !important;
    border-right: none !important;
    box-shadow: 10px 0 28px rgba(75,31,207,0.16) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 1rem 0.85rem !important;
}

[data-testid="stSidebar"][aria-expanded="true"] {
    min-width: 265px !important;
    max-width: 265px !important;
}

[data-testid="stSidebar"][aria-expanded="false"] {
    min-width: 0px !important;
    max-width: 0px !important;
}

/* ── Force ALL sidebar text white ── */
[data-testid="stSidebar"],
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stMarkdown {
    color: #FFFFFF !important;
}

/* ── Hide default Streamlit sidebar nav ── */
[data-testid="stSidebarNav"],
section[data-testid="stSidebar"] div[data-testid="stSidebarNavItems"] {
    display: none !important;
}

/* ── Sidebar Section Label ── */
.sidebar-section-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: rgba(255,255,255,0.66) !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin: 0.55rem 0 0.65rem 0.3rem;
}

/* ── Sidebar Nav Buttons — UNSELECTED ── */
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    width: 100% !important;
    min-height: 48px !important;
    padding: 0.82rem 1rem !important;
    border-radius: 14px !important;
    font-size: 0.93rem !important;
    font-weight: 600 !important;
    color: #FFFFFF !important;
    background: rgba(255,255,255,0.15) !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    box-shadow: none !important;
    cursor: pointer !important;
    text-align: left !important;
    margin-bottom: 0.38rem !important;
    transition: all 0.2s ease !important;
}

/* Force text white on all children of unselected buttons */
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] p,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] span,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] div,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] * {
    color: #FFFFFF !important;
}

[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
    background: rgba(255,255,255,0.28) !important;
    color: #FFFFFF !important;
    transform: translateX(3px) !important;
}

/* ── Sidebar Nav Buttons — ACTIVE/SELECTED ── */
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active {
    background: #FFFFFF !important;
    color: #2e167e !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.14) !important;
    transform: translateX(2px) !important;
    border: none !important;
}

[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active p,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active span,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active div,
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active * {
    color: #2e167e !important;
}

/* ── Block container ── */
.block-container {
    max-width: 1200px !important;
    margin: 0 auto !important;
    padding-top: 1.15rem !important;
    padding-bottom: 1.5rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── Sidebar Footer ── */
.jobie-sidebar-footer {
    margin-top: 1.35rem;
    padding: 0.95rem 0.9rem;
    border-radius: 16px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.08);
}
.jobie-sidebar-footer-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-bottom: 0.3rem;
}
.jobie-sidebar-footer-text {
    font-size: 0.77rem;
    line-height: 1.55;
    color: rgba(255,255,255,0.76) !important;
}

/* ── KPI Stat Cards ── */
.stat-card {
    border-radius: 14px;
    padding: 1.25rem 1.5rem;
    border: 1px solid rgba(0,0,0,.05);
    box-shadow: 0 4px 12px rgba(0,0,0,.08);
    transition: box-shadow .3s, transform .3s;
    color: white !important;
}
.stat-card:hover { box-shadow: 0 8px 24px rgba(0,0,0,.15); transform: translateY(-4px); }
.stat-icon   { font-size: 1.5rem; margin-bottom: .5rem; }
.stat-value  { font-size: 1.75rem; font-weight: 700; color: white !important; line-height: 1.2; font-family: 'DM Mono', monospace; }
.stat-label  { font-size: .8rem; color: rgba(255,255,255,.9) !important; font-weight: 500; margin-top: 2px; text-transform: uppercase; letter-spacing: .06em; }
.stat-accent { width: 32px; height: 3px; border-radius: 2px; margin-top: .75rem; background: rgba(255,255,255,.5) !important; }

/* ── Chart Cards ── */
[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid rgba(0,0,0,.14) !important;
    border-radius: 12px !important;
    padding: 1rem 1rem .75rem !important;
    background: #FFFFFF !important;
    box-shadow: 0 2px 8px rgba(0,0,0,.05) !important;
    margin-bottom: .25rem !important;
}
.chart-card-title {
    font-size: .97rem;
    font-weight: 600;
    color: #1E293B;
    margin-bottom: 4px;
    letter-spacing: -.01em;
}

/* ── Explore Buttons (main content only) ── */
[data-testid="stMain"] div[data-testid="stButton"] > button,
[data-testid="stMain"] [data-testid="stBaseButton-secondary"] {
    background: linear-gradient(135deg, #6366F1 0%, #818CF8 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    padding: .42rem 0 !important;
    font-size: .82rem !important;
    font-weight: 600 !important;
    letter-spacing: .05em !important;
    width: 100% !important;
    box-shadow: 0 2px 8px rgba(99,102,241,.28) !important;
    transition: all .2s !important;
}
[data-testid="stMain"] div[data-testid="stButton"] > button:hover,
[data-testid="stMain"] [data-testid="stBaseButton-secondary"]:hover {
    background: linear-gradient(135deg, #4F46E5 0%, #6366F1 100%) !important;
    box-shadow: 0 4px 16px rgba(99,102,241,.42) !important;
    transform: translateY(-1px) !important;
}

/* ── Typography ── */
.page-title    { font-size: 1.5rem; font-weight: 700; color: #1E293B; margin-bottom: .2rem; letter-spacing: -.01em; }
.page-subtitle { font-size: .88rem; color: #64748B; margin-bottom: 1.5rem; font-weight: 400; }
.page-divider  { height: 1px; background: #F1F5F9; margin: .5rem 0 1rem; }
.chart-row-divider { height: 1px; background: #E2E8F0; margin: 1rem 0; }

/* ── Coming Soon ── */
.coming-soon { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 6rem 2rem; text-align: center; }
.coming-soon-icon { font-size: 3.5rem; margin-bottom: 1rem; }
.coming-soon h2 { font-size: 1.5rem; color: #334155; margin-bottom: .5rem; font-weight: 600; }
.coming-soon p  { font-size: .95rem; color: #94A3B8; max-width: 420px; line-height: 1.7; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
#  SIDEBAR NAVIGATION
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:

    st.markdown(
        '<div class="sidebar-section-label">Main Menu</div>',
        unsafe_allow_html=True
    )

    _NAV = [
        ("🏠", "Main Dashboard", "Dashboard"),
        ("🔎", "Overview", "Overview"),
        ("💻", "Performance Analysis", "Performance Analysis"),
        ("🙋", "Know Yourself", "Know Yourself"),
    ]

    for icon, label, page_key in _NAV:
        if st.button(f"{icon}  {label}", key=f"nav_btn_{page_key}", use_container_width=True):
            st.session_state.current_page = page_key
            st.rerun()

    _label_map = {
        "Dashboard":            "Main Dashboard",
        "Overview":             "Overview",
        "Performance Analysis": "Performance Analysis",
        "Know Yourself":        "Know Yourself",
    }

    active_label = _label_map.get(st.session_state.current_page, st.session_state.current_page)

    components.html(f"""
    <script>
    (function applyActiveNav() {{
        var sidebar = window.parent.document.querySelector('[data-testid="stSidebar"]');
        if (!sidebar) {{ setTimeout(applyActiveNav, 120); return; }}
        var buttons = sidebar.querySelectorAll('[data-testid="stBaseButton-secondary"]');
        if (!buttons.length) {{ setTimeout(applyActiveNav, 120); return; }}
        buttons.forEach(function(btn) {{
            btn.classList.remove('nav-btn-active');
            if (btn.textContent.trim().indexOf("{active_label}") !== -1) {{
                btn.classList.add('nav-btn-active');
            }}
        }});
    }})();
    </script>
    """, height=0, scrolling=False)

    # ── Footer ──
    components.html("""
    <style>
        body { margin: 0; padding: 0; background: transparent; }
        .footer-wrap {
            padding: 1rem 0.9rem;
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.05));
            border: 1px solid rgba(255,255,255,0.25);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .footer-title {
            font-size: 0.68rem;
            font-weight: 800;
            color: rgba(255,255,255,0.6);
            letter-spacing: 0.15em;
            text-transform: uppercase;
            margin-bottom: 0.8rem;
            font-family: sans-serif;
            text-align: center;
        }
        .dev-card {
            background: rgba(255,255,255,0.10);
            border-radius: 10px;
            padding: 0.55rem 0.85rem;
            margin-bottom: 0.45rem;
            border-left: 3px solid rgba(255,255,255,0.35);
        }
        .dev-card:last-child { margin-bottom: 0; }
        .dev-name {
            font-size: 0.80rem;
            font-weight: 700;
            color: #FFFFFF;
            font-family: sans-serif;
            line-height: 1.3;
        }
        .dev-id {
            font-size: 0.66rem;
            color: rgba(255,255,255,0.50);
            margin-top: 2px;
            font-family: sans-serif;
            letter-spacing: 0.03em;
        }
    </style>
    <div class="footer-wrap">
        <div class="footer-title">👨‍💻 Dashboard Developers</div>
        <div class="dev-card">
            <div class="dev-name">Andly Danny Anafiah</div>
            <div class="dev-id">Student ID: 0137461</div>
        </div>
        <div class="dev-card">
            <div class="dev-name">Bayu Fatwa Negara Alias</div>
            <div class="dev-id">Student ID: 0137466</div>
        </div>
        <div class="dev-card">
            <div class="dev-name">Muhamad Roslan Abbas</div>
            <div class="dev-id">Student ID: 0137513</div>
        </div>
    </div>
    """, height=230)

# ══════════════════════════════════════════════════════════════════════════════
#  MAIN PAGE RENDERING
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
