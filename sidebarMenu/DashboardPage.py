import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os

# ══════════════════════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════════════════════
CGPA_COLORS = {
    'High (3.50-4.00)': '#4D96FF',
    'Mid (3.00-3.49)':  '#FFD93D',
    'Low (2.00-3.00)':  '#FF6B6B',
}
CGPA_ORDER  = ['Low (2.00-3.00)', 'Mid (3.00-3.49)', 'High (3.50-4.00)']
NAV_ITEMS   = [
    ("📊", "Dashboard"),
    ("📋", "Overview"),
    ("📈", "Performance Analysis"),
    ("🙋", "Know Yourself"),
]

# ══════════════════════════════════════════════════════════════════════════════
#  GLOBAL STYLES
# ══════════════════════════════════════════════════════════════════════════════
def inject_global_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    #MainMenu, footer { visibility: hidden; }

    header, [data-testid="stHeader"] {
        visibility: visible !important;
        background: transparent !important;
        height: 0 !important;
    }

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
        box-shadow: 0 6px 18px rgba(75, 31, 207, 0.30) !important;
    }

    [data-testid="collapsedControl"] button:hover {
        background: #3d18b4 !important;
    }


    /* ══════════════════════════════════════════════════════
    JOBIE-STYLE COLLAPSIBLE SIDEBAR
    ══════════════════════════════════════════════════════ */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4b1fcf 0%, #3d18b4 100%) !important;
        border-right: none !important;
        box-shadow: 10px 0 28px rgba(75, 31, 207, 0.16) !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding: 1rem 0.85rem 1rem 0.85rem !important;
    }

    /* Expanded sidebar width */
    [data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 265px !important;
        max-width: 265px !important;
    }

    /* Keep collapsed sidebar logically present */
    [data-testid="stSidebar"][aria-expanded="false"] {
        min-width: 82px !important;
        max-width: 82px !important;
    }

    /* Main page auto-resizes */
    [data-testid="stAppViewContainer"] > .main {
        background: #f6f7fb !important;
    }

    .block-container {
        max-width: 100% !important;
        padding-top: 1.15rem !important;
        padding-bottom: 1.5rem !important;
    }

    /* Make the toggle arrow always visible */
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
        box-shadow: 0 6px 18px rgba(75, 31, 207, 0.30) !important;
    }

    [data-testid="collapsedControl"] button:hover {
        background: #3d18b4 !important;
    }

    /* Text color */
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] .stMarkdown {
        color: #FFFFFF !important;
    }

    /* Hide default Streamlit page nav leftovers */
    [data-testid="stSidebarNav"],
    section[data-testid="stSidebar"] div[data-testid="stSidebarNavItems"] {
        display: none !important;
    }

    /* Brand block */
    .jobie-brand {
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 0.95rem 1rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 1.15rem;
        min-height: 72px;
    }

    .jobie-brand-logo {
        width: 42px;
        height: 42px;
        border-radius: 14px;
        background: #FFFFFF;
        color: #4b1fcf !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.05rem;
        font-weight: 800;
        flex-shrink: 0;
    }

    .jobie-brand-text {
        line-height: 1.15;
    }

    .jobie-brand-title {
        font-size: 1rem;
        font-weight: 700;
        color: #FFFFFF !important;
    }

    .jobie-brand-subtitle {
        font-size: 0.72rem;
        color: rgba(255,255,255,0.72) !important;
        margin-top: 0.18rem;
    }

    .sidebar-section-label {
        font-size: 0.72rem;
        font-weight: 700;
        color: rgba(255,255,255,0.66) !important;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin: 0.55rem 0 0.65rem 0.3rem;
    }

    /* Sidebar nav buttons only */
    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] {
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        min-height: 48px !important;
        padding: 0.82rem 1rem !important;
        border-radius: 14px !important;
        font-size: 0.93rem !important;
        font-weight: 500 !important;
        color: rgba(255,255,255,0.92) !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        cursor: pointer !important;
        text-align: left !important;
        margin-bottom: 0.38rem !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover {
        background: rgba(255,255,255,0.12) !important;
        color: #FFFFFF !important;
        transform: translateX(3px) !important;
    }

    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active {
        background: #FFFFFF !important;
        color: #2e167e !important;
        font-weight: 700 !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.14) !important;
        transform: translateX(2px) !important;
    }

    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active p,
    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active span,
    [data-testid="stSidebar"] [data-testid="stBaseButton-secondary"].nav-btn-active div {
        color: #2e167e !important;
    }

    /* Footer */
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
    /* ══════════════════════════════════════════════════════
    KPI STAT CARDS
    ══════════════════════════════════════════════════════ */
    .stat-card {
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        border: 1px solid rgba(0,0,0,.05);
        box-shadow: 0 4px 12px rgba(0,0,0,.08);
        transition: box-shadow .3s, transform .3s;
        color: white !important;
    }

    .stat-card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,.15);
        transform: translateY(-4px);
    }

    .stat-icon { font-size: 1.5rem; margin-bottom: .5rem; }
    .stat-value { font-size: 1.75rem; font-weight: 700; color: white !important; line-height: 1.2; font-family: 'DM Mono', monospace; }
    .stat-label { font-size: .8rem; color: rgba(255,255,255,.9) !important; font-weight: 500; margin-top: 2px; text-transform: uppercase; letter-spacing: .06em; }
    .stat-accent { width: 32px; height: 3px; border-radius: 2px; margin-top: .75rem; background: rgba(255,255,255,.5) !important; }

    /* ══════════════════════════════════════════════════════
    CHART CARD
    ══════════════════════════════════════════════════════ */
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

    /* ══════════════════════════════════════════════════════
    EXPLORE BUTTON  (main content area only — NOT sidebar)
    ══════════════════════════════════════════════════════ */
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
    .page-title { font-size: 1.5rem; font-weight: 700; color: #1E293B; margin-bottom: .2rem; letter-spacing: -.01em; }
    .page-subtitle { font-size: .88rem; color: #64748B; margin-bottom: 1.5rem; font-weight: 400; }
    .page-divider { height: 1px; background: #F1F5F9; margin: .5rem 0 1rem; }
    .chart-row-divider { height: 1px; background: #E2E8F0; margin: 1rem 0; }

    /* ── Coming soon ── */
    .coming-soon { display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 6rem 2rem; text-align: center; }
    .coming-soon-icon { font-size: 3.5rem; margin-bottom: 1rem; }
    .coming-soon h2 { font-size: 1.5rem; color: #334155; margin-bottom: .5rem; font-weight: 600; }
    .coming-soon p { font-size: .95rem; color: #94A3B8; max-width: 420px; line-height: 1.7; }
    </style>
    """, unsafe_allow_html=True)
    
# ══════════════════════════════════════════════════════════════════════════════
#  DATA LOADER
# ══════════════════════════════════════════════════════════════════════════════
@st.cache_data
def load_data():
    script_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(script_dir, "assets", "data", "Student Study Hours & Academic Performance Survey (Cleaned).csv")
    df = pd.read_csv(path)

    df['cgpa_label']         = df['cgpa'].map({3.75:'High (3.50-4.00)', 3.25:'Mid (3.00-3.49)', 2.75:'Low (2.00-3.00)'})
    df['study_hours_label']  = df['study_hours_daily'].map({0.5:'< 1 hour', 1.5:'1-2 hours', 3.5:'3-4 hours', 5.0:'5+ hours'})
    df['social_media_label'] = df['social_media_hours'].map({0.5:'< 1 hour', 1.5:'1-2 hours', 3.5:'3-4 hours', 5.0:'5+ hours'})
    df['exam_hours_label']   = df['study_hours_exam'].map({1:'< 3 hours', 3:'3-4 hours', 6:'5-7 hours', 8:'8+ hours'})
    return df



# ══════════════════════════════════════════════════════════════════════════════
#  (Performance Analysis page)
# ══════════════════════════════════════════════════════════════════════════════

@st.cache_data
def pa_load_data():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root_dir, "assets", "data", "Student Study Hours & Academic Performance Survey (Cleaned).csv")
    df = pd.read_csv(path)

    df['cgpa_label']         = df['cgpa'].map({3.75: 'High (3.50–4.00)', 3.25: 'Mid (3.00–3.49)', 2.75: 'Low (2.00–3.00)'})
    df['study_hours_label']  = df['study_hours_daily'].map({0.5: '< 1 hour', 1.5: '1–2 hours', 3.5: '3–4 hours', 5.0: '5+ hours'})
    df['social_media_label'] = df['social_media_hours'].map({0.5: '< 1 hour', 1.5: '1–2 hours', 3.5: '3–4 hours', 5.0: '5+ hours'})
    df['exam_hours_label']   = df['study_hours_exam'].map({1: '< 3 hours', 3: '3–4 hours', 6: '5–7 hours', 8: '8+ hours'})
    return df


@st.cache_data
def pa_load_raw_data():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(root_dir, "assets", "data", "Student Study Hours & Academic Performance Survey (RAW).csv")
    try:
        return pd.read_csv(path)
    except Exception:
        return None


PA_CGPA_COLORS = {
    'High (3.50–4.00)': '#4D96FF',
    'Mid (3.00–3.49)':  '#FFD93D',
    'Low (2.00–3.00)':  '#FF6B6B',
}
PA_CGPA_ORDER = ['Low (2.00–3.00)', 'Mid (3.00–3.49)', 'High (3.50–4.00)']



def render_study_hours_page():
    inject_global_styles() 
    df = pa_load_data()

    # ── Global styles ────────────────────────────────────────────────────────
    st.markdown("""
        <style>
        .main-header {
            text-align: center;
            background: linear-gradient(135deg, #3b4fe4 0%, #5b6ef5 100%);
            color: #FFFFFF;
            font-size: 3rem;
            font-weight: 900;
            width: 100%;            /* ← change this for width */
            margin: 2 auto 3rem;   /* ← replaces margin-bottom, keeps card centered */
            padding: 0.9rem 2rem;  /* ← top/bottom controls height */
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(21, 101, 192, 0.35);
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            letter-spacing: 1px;
        }
        .header-subtitle {
            font-size: 1.2rem;
            font-weight: 400;
            margin-top: 0rem;
            color: #BBDEFB;
            letter-spacing: 2px;
        }
        .section-header {
            color: #1A237E;
            font-size: 1.8rem;
            font-weight: bold;
            margin-top: 3rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #1A237E;
        }
        .finding-header {
            color: #1A237E;
            font-size: 1.5rem;
            font-weight: bold;
            margin-top: 2rem;
            margin-bottom: 1rem;
            border-left: 5px solid #1565C0;
            padding-left: 1rem;
        }
        .insight-box {
            background-color: #E3F2FD;
            border-left: 4px solid #1565C0;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 4px;
        }
        .text-block {
            background-color: #F5F5F5;
            padding: 1.5rem;
            border-radius: 8px;
            height: 100%;
        }
        .text-block h4 {
            color: #1A237E;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        .text-block ul {
            list-style-type: none;
            padding-left: 0;
        }
        .text-block li { margin-bottom: 0.8rem; line-height: 1.6; }
        .key-takeaway {
            background-color: #FFF3E0;
            border-left: 4px solid #FF9800;
            padding: 1rem;
            margin-top: 1rem;
            border-radius: 4px;
            font-weight: bold;
        }
        .compare-card {
            background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
            border-radius: 16px;
            padding: 1.5rem 2rem;
            text-align: center;
            box-shadow: 0 4px 15px rgba(21,101,192,0.15);
            border: 2px solid #1565C0;
        }
        .compare-value { font-size: 2.2rem; font-weight: 900; color: #1A237E; }
        .compare-label { font-size: 0.95rem; color: #37474F; margin-top: 0.3rem; font-weight: 500; }
        .compare-sub   { font-size: 0.8rem; color: #616161; margin-top: 0.2rem; }
        </style>
    """, unsafe_allow_html=True)
    

    # ── Page Header ──────────────────────────────────────────────────────────
    st.markdown('''
        <div class="main-header">
            💻 Performance Analysis
            <div class="header-subtitle">What Drives Student Success? The Data Tells the Story.</div>
        </div>
    ''', unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # INTERACTIVE SECTION — "How Do You Compare?"
    # ════════════════════════════════════════════════════════════════════════
    # ── Inline Filters ───────────────────────────────────────────────────────
    st.markdown("<div style='margin-bottom: 1.2rem;'></div>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #0F172A, #1E293B);
                border-radius: 14px;
                padding: 1rem 1.5rem;
                margin-bottom: 1rem;
                box-shadow: 0 4px 16px rgba(15,23,42,0.2);
                display: flex;
                align-items: center;
                gap: 0.75rem;
            ">
                <div style="
                    background: #F59E0B;
                    border-radius: 8px;
                    padding: 0.45rem 0.65rem;
                    font-size: 1rem;
                    line-height: 1;
                ">🔽</div>
                <div>
                    <div style="font-size:1rem; font-weight:700; color:#FFFFFF; letter-spacing:0.04em;">
                        Filter Data
                    </div>
                    <div style="font-size:0.75rem; color:rgba(255,255,255,0.55); margin-top:0.1rem;">
                        Narrow down results by gender, study level, or CGPA group
                    </div>
                </div>
                <div style="margin-left:auto; background:rgba(245,158,11,0.15); border-radius:8px;
                            padding:0.3rem 0.7rem; font-size:0.72rem; color:#F59E0B; font-weight:600;">
                    88 respondents
                </div>
            </div>
        """, unsafe_allow_html=True)

        f_col1, f_col2, f_col3 = st.columns([2, 2, 3.5])

        with f_col1:
            selected_gender = st.selectbox(
                "👤 Gender",
                options=["All", "Male", "Female"],
                index=0
            )
        with f_col2:
            # Hardcoded to match actual data column names exactly
            all_levels = [
                "Foundation",
                "Diploma",
                "Bachelor's Degree",
                "Master's Degree",
                "Doctor of Philosophy (PhD)",
            ]
            # Only show levels that actually exist as columns in the data
            available_levels = [
                lvl for lvl in all_levels
                if f"Current Level of Studies_{lvl}" in df.columns
            ]
            level_options = ["All"] + available_levels
            selected_level = st.selectbox(
                "🎓 Level of Study",
                options=level_options,
                index=0
            )
        with f_col3:
            selected_cgpa = st.multiselect(
                "📊 CGPA Group",
                options=["High (3.50–4.00)", "Mid (3.00–3.49)", "Low (2.00–3.00)"],
                default=["High (3.50–4.00)", "Mid (3.00–3.49)", "Low (2.00–3.00)"]
            )

    # Apply filters
    if selected_gender != "All":
        df = df[df["Gender_Male"] == (1 if selected_gender == "Male" else 0)]
    if selected_level != "All":
        col = f"Current Level of Studies_{selected_level}"
        if col in df.columns:
            df = df[df[col] == 1]
    if selected_cgpa:
        df = df[df["cgpa_label"].isin(selected_cgpa)]
    if df.empty:
        st.warning("⚠️ No data matches your current filters. Please adjust the filters above.")
        st.stop()

    st.markdown('<div class="section-header">🔍 How Do You Compare?</div>', unsafe_allow_html=True)
    st.markdown(
        '<p style="color:#424242;font-size:1.05rem;margin-bottom:1rem;">'
        'Select your daily habits below and see how you stack up against the <b>88 surveyed students</b>.</p>',
        unsafe_allow_html=True
    )

    col_input1, col_input2 = st.columns(2)

    study_options  = {'< 1 hour': 0.5, '1–2 hours': 1.5, '3–4 hours': 3.5, '5+ hours': 5.0}
    social_options = {'< 1 hour': 0.5, '1–2 hours': 1.5, '3–4 hours': 3.5, '5+ hours': 5.0}

    with col_input1:
        user_study = st.select_slider(
            "📚 How many hours do you study per day?",
            options=list(study_options.keys()),
            value='1–2 hours'
        )
    with col_input2:
        user_social = st.select_slider(
            "📱 How many hours do you spend on social media per day?",
            options=list(social_options.keys()),
            value='3–4 hours'
        )

    user_study_val  = study_options[user_study]
    user_social_val = social_options[user_social]

    # Compute comparison stats
    pct_study_more  = (df['study_hours_daily'] <= user_study_val).mean() * 100
    pct_social_less = (df['social_media_hours'] >= user_social_val).mean() * 100

    # Average CGPA of students matching these selections
    similar = df[(df['study_hours_daily'] == user_study_val) & (df['social_media_hours'] == user_social_val)]
    same_study = df[df['study_hours_daily'] == user_study_val]

    avg_cgpa_similar    = similar['cgpa'].mean() if len(similar) > 0 else None
    avg_cgpa_same_study = same_study['cgpa'].mean() if len(same_study) > 0 else None

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
            <div class="compare-card">
                <div class="compare-value">{pct_study_more:.0f}%</div>
                <div class="compare-label">of students study ≤ your level</div>
                <div class="compare-sub">You selected: {user_study}</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="compare-card">
                <div class="compare-value">{pct_social_less:.0f}%</div>
                <div class="compare-label">use ≥ your social media time</div>
                <div class="compare-sub">You selected: {user_social}</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        if avg_cgpa_same_study is not None:
            st.markdown(f"""
                <div class="compare-card">
                    <div class="compare-value">{avg_cgpa_same_study:.2f}</div>
                    <div class="compare-label">Avg CGPA at your study level</div>
                    <div class="compare-sub">{len(same_study)} students study {user_study}</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="compare-card">
                    <div class="compare-value">—</div>
                    <div class="compare-label">No data at this study level</div>
                </div>
            """, unsafe_allow_html=True)

    with c4:
        if avg_cgpa_similar is not None:
            st.markdown(f"""
                <div class="compare-card">
                    <div class="compare-value">{avg_cgpa_similar:.2f}</div>
                    <div class="compare-label">Avg CGPA for your exact profile</div>
                    <div class="compare-sub">{len(similar)} students match both selections</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="compare-card">
                    <div class="compare-value">—</div>
                    <div class="compare-label">No exact match in data</div>
                    <div class="compare-sub">Try a different combination</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Data Preview — loads RAW data ────────────────────────────────────────
    with st.expander("📊 Data Preview — Raw Survey Responses (click to expand)"):
        raw_df = pa_load_raw_data()
        if raw_df is not None:
            st.dataframe(raw_df.head(10), use_container_width=True)
            st.write(f"**Total raw responses:** {len(raw_df)}")
            st.write(f"**Columns:** {list(raw_df.columns)}")
            col_dl1, col_dl2 = st.columns(2)
            with col_dl1:
                st.download_button(
                    label="⬇️ Download Raw Data (.csv)",
                    data=raw_df.to_csv(index=False).encode("utf-8"),
                    file_name="Student_Survey_RAW.csv",
                    mime="text/csv"
                )
            with col_dl2:
                clean_df = pa_load_data()
                st.download_button(
                    label="⬇️ Download Cleaned Data (.csv)",
                    data=clean_df.to_csv(index=False).encode("utf-8"),
                    file_name="Student_Survey_Cleaned.csv",
                    mime="text/csv"
                )
        else:
            st.warning("Raw data file not found in the current directory.")

    # ════════════════════════════════════════════════════════════════════════
    # VIZ 1 ▸ Bar Chart — Average Daily Study Hours by CGPA
    # ════════════════════════════════════════════════════════════════════════
    st.markdown('<div id="pa-study-hours"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⭐ Do High Achievers Really Study More?</div>', unsafe_allow_html=True)

    col_chart, col_text = st.columns([3, 2], vertical_alignment="center")

    with col_chart:
        avg_hours = df.groupby('cgpa_label')['study_hours_daily'].mean().reindex(PA_CGPA_ORDER)
        counts    = df['cgpa_label'].value_counts().reindex(PA_CGPA_ORDER)

        fig_bar = go.Figure()
        for cat, val, n in zip(PA_CGPA_ORDER, avg_hours, counts):
            fig_bar.add_trace(go.Bar(
                x=[cat], y=[val],
                marker=dict(color=PA_CGPA_COLORS[cat], line=dict(color='white', width=2)),
                text=[f'<b>{val:.2f} hrs</b><br>n={n}'],
                textposition='outside',
                textfont=dict(size=14, family='Arial Black'),
                hovertemplate=(
                    '<b>%{x}</b><br>'
                    f'Avg Study Hours: {val:.2f} hrs<br>'
                    f'Students: {n}<br>'
                    '<extra></extra>'
                ),
                name=cat, showlegend=True
            ))

        fig_bar.update_layout(
            title=dict(
                text='<b>📚 Average Daily Study Hours by CGPA Category</b>',
                x=0.5, xanchor='center',
                font=dict(size=20, color='#1A237E', family='Arial Black')
            ),
            xaxis=dict(
                title=dict(text='<b>CGPA Category</b>', font=dict(size=15, color='#1A237E')),
                showgrid=False, tickfont=dict(size=13, color='#2C3E50')
            ),
            yaxis=dict(
                title=dict(text='<b>Average Daily Study Hours</b>', font=dict(size=15, color='#1A237E')),
                showgrid=True, gridcolor='rgba(200,200,200,0.3)',
                tickfont=dict(size=12, color='#2C3E50'),
                range=[0, (avg_hours.max() if avg_hours.notna().any() else 1) * 1.35]
            ),
            plot_bgcolor='rgba(240,248,255,0.5)',
            paper_bgcolor='white',
            hovermode='x unified',
            hoverlabel=dict(bgcolor='white', font_size=13, font_family='Arial'),
            legend=dict(
                orientation='h', yanchor='bottom', y=1.0, xanchor='right', x=0.7,
                bgcolor='rgba(255,255,255,0.8)', bordercolor='#1A237E', borderwidth=2
            ),
            height=520, bargap=0.3
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_text:
        st.markdown("""
        <div class="text-block">
        <h4>WHAT THE DATA REVEALS</h4>
        <p style="line-height:1.8;color:#424242;">
        Students with higher CGPAs consistently dedicate more hours to daily study,
        showing a clear positive relationship between study time and academic achievement.
        </p>
        <h4 style="margin-top:1.5rem;">KEY FINDINGS</h4>
        <ul>
            <li>• <b>High CGPA (3.50–4.00):</b> Study the most per day on average</li>
            <li>• <b>Mid CGPA (3.00–3.49):</b> Moderate daily study commitment</li>
            <li>• <b>Low CGPA (2.00–3.00):</b> Fewest average study hours daily</li>
        </ul>
        <h4 style="margin-top:1.5rem;">WHY IT MATTERS</h4>
        <p style="line-height:1.8;color:#424242;">
        Consistent daily study builds long-term retention far better than last-minute cramming.
        Even adding 30 minutes per day can shift academic outcomes over a semester.
        </p>
        <div class="key-takeaway">
        💡 <b>Key Takeaway:</b><br>
        More daily study leads to a better CGPA, and consistency is more effective than intensity.
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="insight-box">💡 <b>Key Insight:</b> The gap in average daily study hours between High and Low CGPA groups highlights that incremental, daily effort compounds into significant academic differences over time.</div>', unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # VIZ 2 ▸ Donut — Study Challenge Categories
    # ════════════════════════════════════════════════════════════════════════
    st.markdown('<div id="pa-study-challenges"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⭐ What Stops Students from Studying Effectively?</div>', unsafe_allow_html=True)

    col_t2, col_c2 = st.columns([3, 3], vertical_alignment="center")

    with col_t2:
        st.markdown("""
        <div class="text-block">
        <h4>WHAT THE DATA REVEALS</h4>
        <p style="line-height:1.8;color:#424242;">
        Students face a variety of study challenges that hinder academic performance.
        Understanding the most common obstacles helps target the right support.
        </p>
        <h4 style="margin-top:1.5rem;">TOP CHALLENGES</h4>
        <ul>
            <li>• <b>Distractions:</b> Social media, phone notifications, and environment</li>
            <li>• <b>Motivation:</b> Difficulty staying engaged with coursework</li>
            <li>• <b>Time Management:</b> Balancing study with other commitments</li>
            <li>• <b>Comprehension:</b> Struggling to understand difficult material</li>
        </ul>
        <h4 style="margin-top:1.5rem;">WHY IT MATTERS</h4>
        <p style="line-height:1.8;color:#424242;">
        Identifying your personal challenge category is the first step to finding the right strategy.
        Different challenges need different solutions.
        </p>
        <div class="key-takeaway">
        💡 <b>Key Takeaway:</b><br>
        Awareness of your study barrier is half the battle. Address the root cause, not the symptom.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col_c2:
        challenge_cols   = [c for c in df.columns if c.startswith('Study Challenge Category_')]
        challenge_counts = df[challenge_cols].sum().sort_values(ascending=False)
        challenge_labels = [c.replace('Study Challenge Category_', '') for c in challenge_counts.index]

        no_challenge = (df[challenge_cols].sum(axis=1) == 0).sum()
        if no_challenge > 0:
            challenge_counts['Academic Workload'] = no_challenge
            challenge_counts = challenge_counts.sort_values(ascending=False)
            challenge_labels = [c.replace('Study Challenge Category_', '') for c in challenge_counts.index]

        pie_colors = ['#4D96FF', '#FFD93D', '#6BCB77', '#FF6B9D', '#9D84B7', '#FF5722', '#00BCD4', '#E91E63']

        fig_pie = go.Figure(data=[go.Pie(
            labels=challenge_labels,
            values=challenge_counts.values,
            hole=0.45,
            marker=dict(colors=pie_colors[:len(challenge_labels)], line=dict(color='white', width=3)),
            textinfo='percent',
            textfont=dict(size=12, family='Arial'),
            hovertemplate='<b>%{label}</b><br>Students: %{value}<br>Percentage: %{percent}<extra></extra>',
            pull=[0.05 if i == 0 else 0 for i in range(len(challenge_labels))],
            rotation=140
        )])

        fig_pie.add_annotation(
            text=f'<b>{int(challenge_counts.sum())}</b><br><span style="font-size:14px">Responses</span>',
            x=0.5, y=0.5,
            font=dict(size=20, color='#1A237E', family='Arial Black'),
            showarrow=False
        )

        fig_pie.update_layout(
            title=dict(
                text='<b>🎯 Study Challenge Category Distribution</b>',
                x=0.5, xanchor='center',
                font=dict(size=20, color='#1A237E', family='Arial Black')
            ),
            font=dict(size=13, family='Arial'),
            showlegend=True,
            legend=dict(
                orientation='v', yanchor='middle', y=0.5,
                xanchor='left', x=1.02,
                font=dict(size=12),
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='#1A237E', borderwidth=1
            ),
            paper_bgcolor='white',
            height=520,
            hoverlabel=dict(bgcolor='white', font_size=13, font_family='Arial'),
            margin=dict(t=80, b=20, l=30, r=180)
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    st.markdown('<div class="insight-box">💡 <b>Key Insight:</b> Most students face multiple overlapping challenges. Tackling the top challenge first creates a positive ripple effect on the others.</div>', unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # VIZ 3 ▸ Scatter — Social Media Hours vs Coursework Score
    # ════════════════════════════════════════════════════════════════════════
    st.markdown('<div id="pa-social-coursework"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⭐ Is Social Media Hurting Your Grades?</div>', unsafe_allow_html=True)
    st.markdown('<div class="finding-header">📱 Social Media vs Coursework Performance</div>', unsafe_allow_html=True)

    col_s3, col_t3 = st.columns([3, 2], vertical_alignment="center")

    with col_s3:
        np.random.seed(42)
        plot_df = df[['social_media_hours', 'coursework_score', 'cgpa_label', 'study_hours_daily']].copy()
        plot_df['sm_j']  = plot_df['social_media_hours'] + np.random.normal(0, 0.1, len(plot_df))
        plot_df['cw_j']  = plot_df['coursework_score']   + np.random.normal(0, 1.2, len(plot_df))

        fig_scatter = go.Figure()
        for label in PA_CGPA_ORDER:
            sub = plot_df[plot_df['cgpa_label'] == label]
            fig_scatter.add_trace(go.Scatter(
                x=sub['sm_j'], y=sub['cw_j'],
                mode='markers',
                marker=dict(color=PA_CGPA_COLORS[label], size=11,
                            line=dict(color='white', width=1.5), opacity=0.75),
                name=label,
                hovertemplate=(
                    f'<b>CGPA: {label}</b><br>'
                    'Social Media: %{customdata[0]:.1f} hrs/day<br>'
                    'Coursework: %{customdata[1]}%<br>'
                    'Study Hours: %{customdata[2]:.1f} hrs/day<br>'
                    '<extra></extra>'
                ),
                customdata=sub[['social_media_hours', 'coursework_score', 'study_hours_daily']].values
            ))

        z = np.polyfit(df['social_media_hours'], df['coursework_score'], 1)
        p = np.poly1d(z)
        x_line = np.linspace(df['social_media_hours'].min() - 0.3, df['social_media_hours'].max() + 0.3, 100)
        fig_scatter.add_trace(go.Scatter(
            x=x_line, y=p(x_line),
            mode='lines',
            line=dict(color='rgba(220,50,50,0.45)', width=3, dash='dash'),
            name=f'Trend (slope: {z[0]:.2f})',
            hoverinfo='skip'
        ))

        fig_scatter.update_layout(
            title=dict(
                text='<b>📱 Social Media Hours vs Coursework Score</b>',
                x=0.5, xanchor='center',
                font=dict(size=20, color='#1A237E', family='Arial Black')
            ),
            xaxis=dict(
                title=dict(text='<b>Social Media Hours per Day</b>', font=dict(size=15, color='#1A237E')),
                showgrid=True, gridcolor='rgba(200,200,200,0.3)',
                tickvals=[0.5, 1.5, 3.5, 5.0],
                ticktext=['< 1 hr', '1–2 hrs', '3–4 hrs', '5+ hrs'],
                tickfont=dict(size=12, color='#2C3E50')
            ),
            yaxis=dict(
                title=dict(text='<b>Coursework Score (%)</b>', font=dict(size=15, color='#1A237E')),
                showgrid=True, gridcolor='rgba(200,200,200,0.3)',
                tickfont=dict(size=12, color='#2C3E50')
            ),
            plot_bgcolor='rgba(240,248,255,0.5)',
            paper_bgcolor='white',
            hovermode='closest',
            hoverlabel=dict(bgcolor='white', font_size=13, font_family='Arial'),
            legend=dict(
                orientation='h', yanchor='top', y=-0.15, xanchor='center', x=0.5,
                bgcolor='rgba(255,255,255,0.9)', bordercolor='#1A237E', borderwidth=2,
                font=dict(size=13)
            ),
            height=580, margin=dict(t=80, b=100)
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col_t3:
        st.markdown("""
        <div class="text-block">
        <h4>WHAT THE DATA REVEALS</h4>
        <p style="line-height:1.8;color:#424242;">
        There is a downward trend in coursework scores as social media usage increases.
        High-CGPA students cluster in the lower social-media, higher-score region.
        </p>
        <h4 style="margin-top:1.5rem;">KEY FINDINGS</h4>
        <ul>
            <li>• <b>Low social media (&lt; 1 hr):</b> Highest average coursework scores</li>
            <li>• <b>High social media (5+ hrs):</b> Noticeably lower coursework outcomes</li>
            <li>• <b>High CGPA students</b> dominate the low-screen-time zone</li>
        </ul>
        <h4 style="margin-top:1.5rem;">WHY IT MATTERS</h4>
        <p style="line-height:1.8;color:#424242;">
        Every hour on social media competes directly with study time.
        Even passive scrolling reduces cognitive capacity for deep learning.
        </p>
        <div class="key-takeaway">
        💡 <b>Key Takeaway:</b><br>
        Reducing daily social media use to under 2 hours may help improve your coursework score.
        </div>
        </div>
        """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # VIZ 4 ▸ Line — Average CGPA by Social Media Usage
    # ════════════════════════════════════════════════════════════════════════
    st.markdown('<div id="pa-cgpa-social-media"></div>', unsafe_allow_html=True)
    st.markdown('<div class="finding-header">📉 Does more screen time lead to lower CGPA?</div>', unsafe_allow_html=True)

    col_t4, col_s4 = st.columns([2, 3], vertical_alignment="center")

    with col_t4:
        st.markdown("""
        <div class="text-block">
        <h4>WHAT THE DATA REVEALS</h4>
        <p style="line-height:1.8;color:#424242;">
        Average CGPA tends to drop steadily as daily social media hours increase, showing a consistent pattern across all CGPA groups.
        </p>
        <h4 style="margin-top:1.5rem;">THE GRADIENT</h4>
        <ul>
            <li>• <b>&lt; 1 hr/day:</b> Highest average CGPA recorded</li>
            <li>• <b>1–2 hrs/day:</b> Slight dip — still manageable</li>
            <li>• <b>3–4 hrs/day:</b> Noticeable decline begins</li>
            <li>• <b>5+ hrs/day:</b> Lowest average CGPA in the dataset</li>
        </ul>
        <div class="key-takeaway">
        💡 <b>Key Takeaway:</b><br>
        Set a daily screen-time limit. Even cutting from 3 hrs to 1 hr could bump your CGPA noticeably.
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col_s4:
        sm_labels  = ['< 1 hour', '1–2 hours', '3–4 hours', '5+ hours']
        sm_numeric = [0.5, 1.5, 3.5, 5.0]

        avg_cgpa  = df.groupby('social_media_hours')['cgpa'].mean().reindex(sm_numeric).fillna(0)
        count_sm  = df.groupby('social_media_hours')['cgpa'].count().reindex(sm_numeric).fillna(0).astype(int)
        std_cgpa  = df.groupby('social_media_hours')['cgpa'].std().reindex(sm_numeric).fillna(0)

        fig_line = go.Figure()

        # Confidence band
        fig_line.add_trace(go.Scatter(
            x=sm_labels + sm_labels[::-1],
            y=list(avg_cgpa.values + std_cgpa.values) + list((avg_cgpa.values - std_cgpa.values)[::-1]),
            fill='toself', fillcolor='rgba(77,150,255,0.12)',
            line=dict(color='rgba(255,255,255,0)'),
            name='± 1 Std Dev', hoverinfo='skip'
        ))

        fig_line.add_trace(go.Scatter(
            x=sm_labels, y=avg_cgpa.values,
            mode='lines+markers+text',
            line=dict(color='#1565C0', width=4),
            marker=dict(size=16, color='#1565C0', line=dict(color='white', width=3)),
            text=[f'<b>{v:.2f}</b><br>(n={int(n)})' for v, n in zip(avg_cgpa.values, count_sm.values)],
            textposition='top center',
            textfont=dict(size=12, family='Arial Black', color='#1A237E'),
            name='Average CGPA',
            hovertemplate='<b>%{x}</b><br>Avg CGPA: %{y:.2f}<extra></extra>'
        ))

        fig_line.update_layout(
            title=dict(
                text='<b>📉 Average CGPA by Social Media Usage Hours</b>',
                x=0.5, xanchor='center',
                font=dict(size=20, color='#1A237E', family='Arial Black')
            ),
            xaxis=dict(
                title=dict(text='<b>Social Media Hours per Day</b>', font=dict(size=15, color='#1A237E')),
                showgrid=True, gridcolor='rgba(200,200,200,0.3)',
                tickfont=dict(size=13, color='#2C3E50')
            ),
            yaxis=dict(
                title=dict(text='<b>Average CGPA</b>', font=dict(size=15, color='#1A237E')),
                showgrid=True, gridcolor='rgba(200,200,200,0.3)',
                tickfont=dict(size=12, color='#2C3E50'),
                range=[2.4, 4.1]
            ),
            plot_bgcolor='rgba(240,248,255,0.5)',
            paper_bgcolor='white',
            hovermode='x unified',
            hoverlabel=dict(bgcolor='white', font_size=13, font_family='Arial'),
            legend=dict(
                orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1,
                bgcolor='rgba(255,255,255,0.8)', bordercolor='#1A237E', borderwidth=2
            ),
            height=520
        )
        # Regression trendline
        if avg_cgpa.any():
            z_line = np.polyfit(sm_numeric, avg_cgpa.values, 1)
            p_line = np.poly1d(z_line)
            y_trend = [p_line(x) for x in sm_numeric]
            fig_line.add_trace(go.Scatter(
                x=sm_labels,
                y=y_trend,
                mode='lines',
                line=dict(color='rgba(220,50,50,0.55)', width=2, dash='dot'),
                name=f'Trend (slope: {z_line[0]:.3f})',
                hoverinfo='skip'
            ))

        st.plotly_chart(fig_line, use_container_width=True, key="chart_line")
        
    st.markdown('<div class="insight-box">💡 <b>Key Insight:</b> The CGPA drop from &lt; 1 hr to 5+ hrs of social media per day is statistically meaningful. Managing screen time is one of the most actionable levers students have.</div>', unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # VIZ 5 ▸ 3-D Scatter (expander) — Study × Social Media × Coursework
    # ════════════════════════════════════════════════════════════════════════
    st.markdown('<div id="pa-3d-view"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">⭐ 3D View: The Full Academic Picture</div>', unsafe_allow_html=True)

    with st.expander("🔍 Click here to explore the 3D Interactive Scatter Plot (**Optional for data enthusiasts!**)", expanded=False):
        st.markdown("""
            <div style="background-color:#E3F2FD;padding:1rem;border-radius:8px;margin-bottom:1.5rem;">
                <p style="color:#1A237E;font-weight:bold;font-size:1.1rem;margin-bottom:0.5rem;">
                    🌐 What is this 3D plot showing?
                </p>
                <p style="color:#424242;line-height:1.6;">
                    Each dot is a student. The three axes show <b>daily study hours</b>,
                    <b>social media hours</b>, and <b>coursework score</b>.
                    Rotate and zoom to see how CGPA groups separate in 3D space — 
                    it reveals patterns that flat 2D charts cannot.
                </p>
            </div>
        """, unsafe_allow_html=True)

        np.random.seed(42)
        s3d = df[['study_hours_daily', 'social_media_hours', 'coursework_score',
                  'cgpa_label', 'cgpa', 'time_management', 'note_taking']].copy()
        s3d['x'] = s3d['study_hours_daily']  + np.random.normal(0, 0.15, len(df))
        s3d['y'] = s3d['social_media_hours'] + np.random.normal(0, 0.15, len(df))
        s3d['z'] = s3d['coursework_score']   + np.random.normal(0, 1.5,  len(df))

        symbols = ['diamond', 'square', 'circle']
        fig_3d = go.Figure()

        for label, sym in zip(PA_CGPA_ORDER, symbols):
            sub = s3d[s3d['cgpa_label'] == label]
            fig_3d.add_trace(go.Scatter3d(
                x=sub['x'], y=sub['y'], z=sub['z'],
                mode='markers',
                marker=dict(color=PA_CGPA_COLORS[label], size=7, symbol=sym,
                            line=dict(color='white', width=1), opacity=0.85),
                name=label,
                hovertemplate=(
                    f'<b>{label}</b><br>'
                    'Daily Study: %{customdata[0]:.1f} hrs<br>'
                    'Social Media: %{customdata[1]:.1f} hrs<br>'
                    'Coursework: %{customdata[2]}%<br>'
                    'Time Mgmt: %{customdata[3]}<br>'
                    'Note Taking: %{customdata[4]}<br>'
                    '<extra></extra>'
                ),
                customdata=sub[['study_hours_daily', 'social_media_hours',
                                'coursework_score', 'time_management', 'note_taking']].values
            ))

        axis_style = dict(
            backgroundcolor='rgba(230,240,250,0.8)',
            gridcolor='rgba(26,35,78,0.25)', gridwidth=2,
            showline=True, linecolor='#1A237E', linewidth=2,
            mirror=True, showbackground=True
        )

        fig_3d.update_layout(
            title=dict(
                text='<b>🌐 3D View: Study Hours × Social Media × Coursework</b><br>'
                     '<sub>Rotate • Zoom • Click Points • Explore!</sub>',
                x=0.5, xanchor='center',
                font=dict(size=20, color='#1A237E', family='Arial Black')
            ),
            scene=dict(
                xaxis=dict(title='Daily Study Hours', **axis_style),
                yaxis=dict(title='Social Media Hours', **axis_style),
                zaxis=dict(title='Coursework Score (%)', **axis_style),
                camera=dict(eye=dict(x=1.8, y=1.8, z=1.5))
            ),
            paper_bgcolor='white',
            legend=dict(
                title=dict(text='<b>CGPA Category</b>', font=dict(size=13)),
                orientation='h', yanchor='bottom', y=0.9,
                xanchor='center', x=0.5,
                bgcolor='rgba(255,255,255,0.9)', bordercolor='#1A237E', borderwidth=2,
                font=dict(size=13)
            ),
            height=720,
            hoverlabel=dict(bgcolor='white', font_size=12, font_family='Arial'),
            margin=dict(t=100, b=20)
        )

        
        st.plotly_chart(fig_3d, use_container_width=True)

        st.markdown('<div class="insight-box">💡 <b>Critical Insight:</b> High-CGPA students (blue) cluster in the high study / low social-media zone, while Low-CGPA students (red) occupy the opposite corner. The 3D view makes this separation unmistakable.</div>', unsafe_allow_html=True)

    # ── Footer ───────────────────────────────────────────────────────────────
    st.markdown("---")
    st.markdown("""
    <div style="background:linear-gradient(135deg,#1A237E,#283593); border-radius:16px;
                padding:1.5rem 2rem; margin-top:1rem; color:white;">
        <div style="font-size:1.2rem; font-weight:900; margin-bottom:1rem;">🔑 Key Findings Summary</div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:0.75rem;">
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:0.85rem 1rem;">
                <div style="font-size:0.85rem; font-weight:700; margin-bottom:0.3rem;">📚 Study & CGPA</div>
                <div style="font-size:0.78rem; line-height:1.6; opacity:0.90;">
                    High achievers study <b>3.5+ hrs/day</b> — nearly double low-CGPA students.
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:0.85rem 1rem;">
                <div style="font-size:0.85rem; font-weight:700; margin-bottom:0.3rem;">📱 Social Media</div>
                <div style="font-size:0.78rem; line-height:1.6; opacity:0.90;">
                    <b>5+ hrs/day</b> on social media links to the lowest CGPA in our dataset.
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:0.85rem 1rem;">
                <div style="font-size:0.85rem; font-weight:700; margin-bottom:0.3rem;">🎯 Top Challenge</div>
                <div style="font-size:0.78rem; line-height:1.6; opacity:0.90;">
                    <b>Procrastination</b> is the #1 barrier — followed by distraction and low motivation.
                </div>
            </div>
            <div style="background:rgba(255,255,255,0.1); border-radius:10px; padding:0.85rem 1rem;">
                <div style="font-size:0.85rem; font-weight:700; margin-bottom:0.3rem;">💡 Quick Win</div>
                <div style="font-size:0.78rem; line-height:1.6; opacity:0.90;">
                    Cut screen time to <b>&lt;1 hr/day</b> and add 30 min of study — CGPA improves.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Sidebar navigation is handled entirely by app.py


# ══════════════════════════════════════════════════════════════════════════════
#  HELPER — Explore button
# ══════════════════════════════════════════════════════════════════════════════
# Mapping: explore button key → anchor id in Performance Analysis page
_EXPLORE_ANCHORS = {
    'explore_bar':     'pa-study-hours',
    'explore_pie':     'pa-study-challenges',
    'explore_line':    'pa-cgpa-social-media',
    'explore_scatter': 'pa-social-coursework',
    'explore_3d':      'pa-3d-view',
}

def explore_button(key: str, target_page: str):
    if st.button("🔍  Explore", key=key, use_container_width=True):
        st.session_state["_nav_target"]    = target_page
        st.session_state["_scroll_anchor"] = _EXPLORE_ANCHORS.get(key)
        st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
#  PAGE: DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
def render_dashboard():
    inject_global_styles()
    df = load_data()

    st.markdown("""
        <style>
        .main-header {
        text-align: center;
        background: linear-gradient(135deg, #3b4fe4 0%, #5b6ef5 100%);
        color: #FFFFFF;
        font-size: 2.7rem;        
        font-weight: 900;
        width: 100%;
        margin: 0 0 1rem 0;       
        padding: 0.9rem 1rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(21, 101, 192, 0.35);
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        letter-spacing: 0px;
    }
        .header-subtitle {
            font-size: 1.2rem;
            font-weight: 400;
            margin-top: 0rem;
            color: #BBDEFB;
            letter-spacing: 1.2px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="main-header">
             Study Hours and Academic Performance Dashboard
            <div class="header-subtitle">Exploring how study hours, social media usage, and common student challenges influence CGPA performance, based on clean and reliable survey data collected from real students.</div>
        </div>
    """, unsafe_allow_html=True)

    # ── KPI cards ─────────────────────────────────────────────────────────────
    total      = len(df)
    avg_cgpa   = df['cgpa'].mean()
    avg_study  = df['study_hours_daily'].mean()
    avg_social = df['social_media_hours'].mean()

    st.markdown(f"""
            <div style="
                background: #FFFFFF;
                border-radius: 16px;
                border: 1px solid rgba(0,0,0,0.07);
                padding: 1.9rem 2rem;
                margin-bottom: 1rem;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            ">
                <div style="font-size: 1.2rem; font-weight: 700; color: #7F77DD; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.75rem;">
                    ✅ Found through clean dataset
                </div>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                    <div style="background:linear-gradient(135deg,#663399,#4B2480); border-radius:14px; padding:1rem 1.2rem; color:white;">
                        <div style="font-size:1.3rem; margin-bottom:0.4rem;">👥</div>
                        <div style="font-size:1.6rem; font-weight:800; line-height:1;">{total}</div>
                        <div style="font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-top:4px; opacity:0.9;">Total Respondents</div>
                        <div style="width:28px; height:2px; border-radius:2px; background:rgba(255,255,255,0.45); margin-top:0.6rem;"></div>
                        <div style="font-size:0.65rem; opacity:0.75; margin-top:4px;">After removing 12 invalid responses from 100 collected</div>
                    </div>
                    <div style="background:linear-gradient(135deg,#10B981,#059669); border-radius:14px; padding:1rem 1.2rem; color:white;">
                        <div style="font-size:1.3rem; margin-bottom:0.4rem;">🎓</div>
                        <div style="font-size:1.6rem; font-weight:800; line-height:1;">{avg_cgpa:.2f}</div>
                        <div style="font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-top:4px; opacity:0.9;">Average CGPA</div>
                        <div style="width:28px; height:2px; border-radius:2px; background:rgba(255,255,255,0.45); margin-top:0.6rem;"></div>
                        <div style="font-size:0.65rem; opacity:0.75; margin-top:4px;">Across all CGPA groups in cleaned dataset</div>
                    </div>
                    <div style="background:linear-gradient(135deg,#F59E0B,#D97706); border-radius:14px; padding:1rem 1.2rem; color:white;">
                        <div style="font-size:1.3rem; margin-bottom:0.4rem;">🕓</div>
                        <div style="font-size:1.6rem; font-weight:800; line-height:1;">{avg_study:.1f} hrs</div>
                        <div style="font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-top:4px; opacity:0.9;">Avg Daily Study</div>
                        <div style="width:28px; height:2px; border-radius:2px; background:rgba(255,255,255,0.45); margin-top:0.6rem;"></div>
                        <div style="font-size:0.65rem; opacity:0.75; margin-top:4px;">Most students study 1–2 hrs/day</div>
                    </div>
                    <div style="background:linear-gradient(135deg,#EF4444,#DC2626); border-radius:14px; padding:1rem 1.2rem; color:white;">
                        <div style="font-size:1.3rem; margin-bottom:0.4rem;">📱</div>
                        <div style="font-size:1.6rem; font-weight:800; line-height:1;">{avg_social:.1f} hrs</div>
                        <div style="font-size:0.7rem; font-weight:600; text-transform:uppercase; letter-spacing:0.06em; margin-top:4px; opacity:0.9;">Avg Social Media</div>
                        <div style="width:28px; height:2px; border-radius:2px; background:rgba(255,255,255,0.45); margin-top:0.6rem;"></div>
                        <div style="font-size:0.65rem; opacity:0.75; margin-top:4px;">Nearly 2× more than daily study time</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    
    st.markdown("""
    <div style="
        background: #FFFFFF;
        border-radius: 16px;
        border: 1px solid rgba(0,0,0,0.07);
        padding: 1.25rem 2rem;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    ">
        <div style="font-size: 1.2rem; font-weight: 700; color: #7F77DD; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 0.75rem;">
            📈 Visualisations from our clean data
        </div>
        <div style="font-size: 0.88rem; color: #475569; line-height: 1.6;">
            Here are the charts and insights we built from the dataset. Each one uncovers a different angle of how students study, struggle, and perform.
        </div>
    </div>
""", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════════
    TOP_H = 330
    r1c1, r1c2, r1c3 = st.columns(3, gap="medium")

    # Chart 1 — Study Hours by CGPA ───────────────────────────────────────────
    with r1c1:
        with st.container(border=True):
            st.markdown('<div class="chart-card-title">📚 Study Hours by CGPA</div>', unsafe_allow_html=True)
            avg_hours = df.groupby('cgpa_label')['study_hours_daily'].mean().reindex(CGPA_ORDER)
            counts    = df['cgpa_label'].value_counts().reindex(CGPA_ORDER)
            fig_bar   = go.Figure()
            for cat, val, n in zip(CGPA_ORDER, avg_hours, counts):
                fig_bar.add_trace(go.Bar(
                    x=[cat], y=[val],
                    marker=dict(color=CGPA_COLORS[cat], line=dict(color='white', width=2)),
                    text=[f'<b>{val:.2f}h</b>'], textposition='outside',
                    textfont=dict(size=11, family='DM Sans'),
                    hovertemplate=f'<b>%{{x}}</b><br>Avg Study: {val:.2f} hrs<br>n = {n}<extra></extra>',
                    name=cat,
                ))
            fig_bar.update_layout(
                xaxis=dict(title=dict(text='<b>CGPA Category</b>', font=dict(size=10,color='#1A237E')),
                           showgrid=False, tickfont=dict(size=9,color='#2C3E50'), tickangle=-10),
                yaxis=dict(title=dict(text='<b>Avg Study Hours</b>', font=dict(size=10,color='#1A237E')),
                           showgrid=True, gridwidth=1.5, gridcolor='rgba(100,100,100,0.5)',
                           tickfont=dict(size=9,color='#2C3E50'), range=[0, float(avg_hours.max())*1.3]),
                plot_bgcolor='rgba(250,250,250,0.5)', paper_bgcolor='rgba(0,0,0,0)',
                hovermode='x unified', hoverlabel=dict(bgcolor='white',font_size=11),
                showlegend=False, height=TOP_H, bargap=0.35, margin=dict(t=20,b=38,l=25,r=10)
            )
            st.plotly_chart(fig_bar, use_container_width=True, key="chart_bar")
            explore_button("explore_bar", "Performance Analysis")

    # Chart 2 — Study Challenges ───────────────────────────────────────────────
    with r1c2:
        with st.container(border=True):
            st.markdown('<div class="chart-card-title">🎯 Study Challenges</div>', unsafe_allow_html=True)
            challenge_cols   = [c for c in df.columns if c.startswith('Study Challenge Category_')]
            challenge_counts = df[challenge_cols].sum().sort_values(ascending=False)
            challenge_labels = [c.replace('Study Challenge Category_', '') for c in challenge_counts.index]
            no_challenge = (df[challenge_cols].sum(axis=1) == 0).sum()
            if no_challenge > 0:
                challenge_counts['Academic Workload'] = no_challenge
                challenge_counts = challenge_counts.sort_values(ascending=False)
                challenge_labels = [c.replace('Study Challenge Category_', '') for c in challenge_counts.index]
            pie_colors = ['#4D96FF','#FFD93D','#6BCB77','#FF6B9D','#9D84B7','#FF5722','#00BCD4','#E91E63']
            fig_pie = go.Figure(data=[go.Pie(
                labels=challenge_labels, values=challenge_counts.values, hole=0.44,
                marker=dict(colors=pie_colors[:len(challenge_labels)], line=dict(color='white',width=2)),
                textinfo='percent', textfont=dict(size=8,family='DM Sans'),
                hovertemplate='<b>%{label}</b><br>Students: %{value}<br>%{percent}<extra></extra>',
                pull=[0.04 if i == 0 else 0 for i in range(len(challenge_labels))], rotation=140
            )])
            fig_pie.add_annotation(
                text=f'<b>{int(challenge_counts.sum())}</b><br><span style="font-size:9px">Total</span>',
                x=0.5, y=0.5, font=dict(size=14,color='#1A237E',family='DM Sans'), showarrow=False
            )
            fig_pie.update_layout(
                showlegend=True,
                legend=dict(orientation='v',yanchor='middle',y=0.5,xanchor='left',x=1.01,
                            font=dict(size=8),bgcolor='rgba(255,255,255,0.85)',
                            bordercolor='#E2E8F0',borderwidth=1),
                paper_bgcolor='rgba(0,0,0,0)', height=TOP_H,
                hoverlabel=dict(bgcolor='white',font_size=11),
                margin=dict(t=20,b=18,l=10,r=105)
            )
            st.plotly_chart(fig_pie, use_container_width=True, key="chart_pie")
            explore_button("explore_pie", "Performance Analysis")

    # Chart 3 — CGPA vs Social Media ──────────────────────────────────────────
    with r1c3:
        with st.container(border=True):
            st.markdown('<div class="chart-card-title">📉 CGPA vs Social Media</div>', unsafe_allow_html=True)
            sm_labels  = ['< 1 hr','1-2 hrs','3-4 hrs','5+ hrs']
            sm_numeric = [0.5, 1.5, 3.5, 5.0]
            avg_cgpa_line = df.groupby('social_media_hours')['cgpa'].mean().reindex(sm_numeric).fillna(0)
            std_cgpa      = df.groupby('social_media_hours')['cgpa'].std().reindex(sm_numeric).fillna(0)
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(
                x=sm_labels+sm_labels[::-1],
                y=list(avg_cgpa_line.values+std_cgpa.values)+list((avg_cgpa_line.values-std_cgpa.values)[::-1]),
                fill='toself', fillcolor='rgba(77,150,255,0.12)',
                line=dict(color='rgba(255,255,255,0)'), name='± 1 SD', hoverinfo='skip'
            ))
            fig_line.add_trace(go.Scatter(
                x=sm_labels, y=avg_cgpa_line.values,
                mode='lines+markers+text', line=dict(color='#1565C0',width=3),
                marker=dict(size=10,color='#1565C0',line=dict(color='white',width=2)),
                text=[f'<b>{v:.2f}</b>' for v in avg_cgpa_line.values],
                textposition='top center', textfont=dict(size=9,family='DM Sans',color='#1A237E'),
                name='Avg CGPA', hovertemplate='<b>%{x}</b><br>Avg CGPA: %{y:.2f}<extra></extra>'
            ))
            fig_line.update_layout(
                xaxis=dict(title=dict(text='<b>Social Media hrs/day</b>',font=dict(size=10,color='#1A237E')),
                           showgrid=True,gridwidth=1.5,gridcolor='rgba(100,100,100,0.5)',
                           tickfont=dict(size=9,color='#2C3E50')),
                yaxis=dict(title=dict(text='<b>Avg CGPA</b>',font=dict(size=10,color='#1A237E')),
                           showgrid=True,gridwidth=1.5,gridcolor='rgba(100,100,100,0.5)',
                           tickfont=dict(size=9,color='#2C3E50'),range=[2.4,4.25]),
                plot_bgcolor='rgba(250,250,250,0.5)',paper_bgcolor='rgba(0,0,0,0)',
                hovermode='x unified',hoverlabel=dict(bgcolor='white',font_size=11),
                legend=dict(orientation='h',yanchor='top',y=0.99,xanchor='center',x=0.5,
                            bgcolor='rgba(255,255,255,0.85)',bordercolor='#E2E8F0',borderwidth=1,font=dict(size=9)),
                height=TOP_H, margin=dict(t=20,b=38,l=10,r=10)
            )
            
            # Regression trendline
            if avg_cgpa_line.any():
                z_line = np.polyfit(sm_numeric, avg_cgpa_line.values, 1)
                p_line = np.poly1d(z_line)
                y_trend = [p_line(x) for x in sm_numeric]
                fig_line.add_trace(go.Scatter(
                    x=sm_labels,
                    y=y_trend,
                    mode='lines',
                    line=dict(color='rgba(220,50,50,0.55)', width=2, dash='dot'),
                    name=f'Trend (slope: {z_line[0]:.3f})',
                    hoverinfo='skip'
                ))

            st.plotly_chart(fig_line, use_container_width=True, key="chart_line")
            explore_button("explore_line", "Performance Analysis")

    st.markdown("<div class='chart-row-divider'></div>", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════════════
    BOT_H = 420
    r2c1, r2c2 = st.columns(2, gap="medium")

    # Chart 4 — Scatter ───────────────────────────────────────────────────────
    with r2c1:
        with st.container(border=True):
            st.markdown('<div class="chart-card-title">📱 Social Media vs Coursework Score</div>', unsafe_allow_html=True)
            np.random.seed(42)
            plot_df = df[['social_media_hours','coursework_score','cgpa_label','study_hours_daily']].copy()
            plot_df['sm_j'] = plot_df['social_media_hours'] + np.random.normal(0,0.1,len(plot_df))
            plot_df['cw_j'] = plot_df['coursework_score']   + np.random.normal(0,1.2,len(plot_df))
            fig_scatter = go.Figure()
            for lbl in CGPA_ORDER:
                sub = plot_df[plot_df['cgpa_label']==lbl]
                fig_scatter.add_trace(go.Scatter(
                    x=sub['sm_j'], y=sub['cw_j'], mode='markers',
                    marker=dict(color=CGPA_COLORS[lbl],size=9,line=dict(color='white',width=1.5),opacity=0.75),
                    name=lbl,
                    hovertemplate=(f'<b>{lbl}</b><br>Social Media: %{{customdata[0]:.1f}} hrs/day<br>'
                                   'Coursework: %{customdata[1]}%<br>Study Hours: %{customdata[2]:.1f} hrs/day<extra></extra>'),
                    customdata=sub[['social_media_hours','coursework_score','study_hours_daily']].values
                ))
            z = np.polyfit(df['social_media_hours'], df['coursework_score'], 1)
            p_fit = np.poly1d(z)
            x_rng = np.linspace(df['social_media_hours'].min()-0.3, df['social_media_hours'].max()+0.3, 100)
            fig_scatter.add_trace(go.Scatter(
                x=x_rng, y=p_fit(x_rng), mode='lines',
                line=dict(color='rgba(220,50,50,0.45)',width=2.5,dash='dash'),
                name=f'Trend (slope: {z[0]:.2f})', hoverinfo='skip'
            ))
            fig_scatter.update_layout(
                xaxis=dict(title=dict(text='<b>Social Media Hours/Day</b>',font=dict(size=11,color='#1A237E')),
                           showgrid=True,gridwidth=1.5,gridcolor='rgba(100,100,100,0.5)',
                           tickvals=[0.5,1.5,3.5,5.0],ticktext=['< 1 hr','1-2 hrs','3-4 hrs','5+ hrs'],
                           tickfont=dict(size=10,color='#2C3E50')),
                yaxis=dict(title=dict(text='<b>Coursework Score (%)</b>',font=dict(size=11,color='#1A237E')),
                           showgrid=True,gridwidth=1.5,gridcolor='rgba(100,100,100,0.5)',
                           tickfont=dict(size=10,color='#2C3E50')),
                plot_bgcolor='rgba(250,250,250,0.5)',paper_bgcolor='rgba(0,0,0,0)',
                hovermode='closest',hoverlabel=dict(bgcolor='white',font_size=11),
                legend=dict(orientation='h',yanchor='bottom',y=-0.40,xanchor='center',x=0.5,
                            bgcolor='rgba(255,255,255,0.9)',bordercolor='#E2E8F0',borderwidth=1,font=dict(size=10)),
                height=BOT_H, margin=dict(t=15,b=10,l=60,r=15)
            )
            st.plotly_chart(fig_scatter, use_container_width=True, key="chart_scatter")
            explore_button("explore_scatter", "Performance Analysis")

    # Chart 5 — 3D ─────────────────────────────────────────────────────────────
    with r2c2:
        with st.container(border=True):
            st.markdown('<div class="chart-card-title">🌐 Study × Social Media × Coursework (Optional for data enthusiasts!)</div>', unsafe_allow_html=True)
            np.random.seed(42)
            s3d = df[['study_hours_daily','social_media_hours','coursework_score',
                       'cgpa_label','cgpa','time_management','note_taking']].copy()
            s3d['x'] = s3d['study_hours_daily']  + np.random.normal(0,0.15,len(df))
            s3d['y'] = s3d['social_media_hours']  + np.random.normal(0,0.15,len(df))
            s3d['z'] = s3d['coursework_score']    + np.random.normal(0,1.5,len(df))
            symbols  = ['diamond','square','circle']
            fig_3d   = go.Figure()
            for lbl, sym in zip(CGPA_ORDER, symbols):
                sub = s3d[s3d['cgpa_label']==lbl]
                fig_3d.add_trace(go.Scatter3d(
                    x=sub['x'], y=sub['y'], z=sub['z'], mode='markers',
                    marker=dict(color=CGPA_COLORS[lbl],size=6,symbol=sym,
                                line=dict(color='white',width=0.8),opacity=0.85),
                    name=lbl,
                    hovertemplate=(f'<b>{lbl}</b><br>Daily Study: %{{customdata[0]:.1f}} hrs<br>'
                                   'Social Media: %{customdata[1]:.1f} hrs<br>Coursework: %{customdata[2]}%<br>'
                                   'Time Mgmt: %{customdata[3]}<br>Note Taking: %{customdata[4]}<extra></extra>'),
                    customdata=sub[['study_hours_daily','social_media_hours',
                                    'coursework_score','time_management','note_taking']].values
                ))
            ax = dict(backgroundcolor='rgba(230,240,250,0.8)',gridcolor='rgba(100,100,100,0.5)',
                      gridwidth=1.5,showline=True,linecolor='#1A237E',linewidth=1,
                      mirror=True,showbackground=True)
            fig_3d.update_layout(
                scene=dict(
                    xaxis=dict(title=dict(text='Study Hrs',   font=dict(size=9)), **ax),
                    yaxis=dict(title=dict(text='Social Media',font=dict(size=9)), **ax),
                    zaxis=dict(title=dict(text='Coursework %',font=dict(size=9)), **ax),
                    camera=dict(eye=dict(x=1.65,y=1.65,z=1.1))
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                legend=dict(title=dict(text='<b>CGPA</b>',font=dict(size=10,color='#1A237E')),
                            orientation='v',yanchor='top',y=0.97,xanchor='right',x=0.99,
                            bgcolor='rgba(255,255,255,0.92)',bordercolor='#C8D6E8',borderwidth=1,font=dict(size=10)),
                height=BOT_H, hoverlabel=dict(bgcolor='white',font_size=11),
                margin=dict(t=20,b=10,l=0,r=0)
            )
            st.plotly_chart(fig_3d, use_container_width=True, key="chart_3d")
            explore_button("explore_3d", "Performance Analysis")


# ══════════════════════════════════════════════════════════════════════════════
#  PLACEHOLDER PAGES
# ══════════════════════════════════════════════════════════════════════════════
def render_overview():
    st.markdown("""
        <div class="page-title">Overview</div>
        <div class="page-subtitle">Survey Summary & Data Snapshot</div>
        <div class="page-divider"></div>
        <div class="coming-soon">
            <div class="coming-soon-icon">🚧</div>
            <h2>Coming Soon</h2>
            <p>This section will contain a full overview of the survey dataset, including demographic breakdown, data quality summary, and key distributions.</p>
        </div>""", unsafe_allow_html=True)

def render_performance_analysis():
    """Wrapper — delegates to render_study_hours_page() and scrolls to anchor."""
    render_study_hours_page()
    # After the page renders, fire JS scroll if an anchor was requested
    anchor = st.session_state.get("_scroll_anchor")
    if anchor:
        st.session_state["_scroll_anchor"] = None  # consume it
        scroll_js = f"""
        <script>
        (function() {{
            function scrollTo() {{
                var el = window.parent.document.getElementById('{anchor}');
                if (el) {{
                    el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }} else {{
                    setTimeout(scrollTo, 150);
                }}
            }}
            setTimeout(scrollTo, 300);
        }})();
        </script>
        """
        components.html(scroll_js, height=0)

def render_know_yourself():
    st.markdown("""
        <div class="page-title">Know Yourself</div>
        <div class="page-subtitle">Personalised Insights & Self-Assessment</div>
        <div class="page-divider"></div>
        <div class="coming-soon">
            <div class="coming-soon-icon">🙋</div>
            <h2>Coming Soon</h2>
            <p>This interactive section will let you input your own study and lifestyle habits to see personalised recommendations and where you stand against your peers.</p>
        </div>""", unsafe_allow_html=True)