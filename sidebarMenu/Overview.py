import streamlit as st
from streamlit_lottie import st_lottie
from pathlib import Path
from components.home_lottie import lottie_students, lottie_client

def show_overview():
    # =====================================================================
    # GLOBAL STYLES
    # =====================================================================
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif !important;
        }

        :root { color-scheme: light !important; }

        html, body, .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewBlockContainer"],
        main, .block-container,
        [data-testid="stHeader"] {
            background-color: #ffffff !important;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 1rem;
            padding-bottom: 1rem;
            margin: 0 auto;
        }

        @keyframes fadeInUpTitle {
            from { opacity: 0; transform: translateY(15px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        .fade-title {
            opacity: 0;
            animation: fadeInUpTitle 0.8s ease-out forwards;
        }

        .fade-sub {
            opacity: 0;
            animation: fadeInUpTitle 0.8s ease-out forwards;
            animation-delay: 0.15s;
        }

        .page-title {
            font-size: 42px;
            font-weight: 800;
            color: #1e3a8a;
            margin-bottom: 10px;
            text-align: center;
        }

        .page-subtitle {
            font-size: 18px;
            color: #475569;
            text-align: center;
            margin-bottom: 30px;
        }

        .equal-card {
            height: 100%;
            display: flex;
            flex-direction: column;
        }

        .video-frame {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
            height: 0;
            overflow: hidden;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .video-frame iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: 0;
        }
    </style>
    """, unsafe_allow_html=True)

    # =====================================================================
    # HEADER SECTION
    # =====================================================================

    st.markdown("""
        <style>
        .main-header {
        text-align: center;
        background: linear-gradient(135deg, #3b4fe4 0%, #5b6ef5 100%);
        color: #FFFFFF;
        font-size: 2.9rem;        
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
             🔎 Dashboard Overview
            <div class="header-subtitle">Data-driven insights into study habits, attendance, grades,and the factors that shape student success in Malaysia</div>
        </div>
    """, unsafe_allow_html=True)


    # =====================================================================
    # MAIN PAGE CONTENT
    # =====================================================================
    _, centerB, _ = st.columns([1, 2, 1])

    with centerB:
        st.markdown("<div style='margin-top: 2rem;'></div>", unsafe_allow_html=True)
        if lottie_students:
            try:
                st_lottie(lottie_students, height=300, key="overview_top_lottie")
            except Exception:
                st.empty()
        else:
            st.empty()

    st.markdown("""
    <div style='text-align:center; font-size:17px; color:#444; max-width:750px; margin: 0 auto;'>
        This dashboard analyses real student data to help you understand how study time, attendance,
        sleep, parental support, extracurricular activities, and more are connected to academic outcomes.
        Use the content below to explore the data, uncover patterns, and reflect on your own habits.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.write("")
    st.markdown("#### Learn About Academic Performance")

    col_video, col_info = st.columns(2)

    with col_video:
        st.markdown("""
        <div class="equal-card">
        <div class="video-frame">
            <iframe
            src="https://www.youtube.com/embed/8ZhoeSaPF-k"
            title="How to Improve Academic Performance"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
            </iframe>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div class="equal-card" style="background-color: #FFF9C4; padding: 15px; border-radius: 10px;">
        <h4>Why this video matters</h4>
        <p>
            This video walks through evidence-based strategies that consistently improve academic results.
            It highlights that:
        </p>
        <ul>
            <li>Study habits and time management are stronger predictors of grades than raw talent.</li>
            <li>Regular attendance and active participation significantly boost understanding.</li>
            <li>Sleep, nutrition, and physical activity directly affect concentration and memory retention.</li>
        </ul>
        <p style="margin-top: 12px;">
            As students, our daily choices like sleep, study habits, and class attendance shape our academic results over time. This dashboard shows that data so you can make better decisions.
        </p>
        </div>
        """, unsafe_allow_html=True)


    st.write("")
    left_lottie, right_text = st.columns([1, 2])

    with left_lottie:
        if lottie_client:
            try:
                st_lottie(lottie_client, height=260, key="client_lottie")
            except Exception:
                st.empty()
        else:
            st.empty()

    with right_text:
        st.markdown("""
        <div style='font-size:20px; font-weight:700; margin-top:10px; margin-bottom:5px;'>
            Why Academic Performance Data Matters
        </div>
        <div style='font-size:14px; color:#333;'>
            University outcomes are shaped by dozens of overlapping factors. Our dataset reveals:
            <ul>
                <li>How weekly study hours correlate with final exam grades</li>
                <li>The impact of attendance rate on overall GPA</li>
                <li>How parental education and support levels influence student results</li>
                <li>Whether extracurricular involvement helps or hurts academic scores</li>
                <li>The role of internet access and tutoring on performance gaps</li>
            </ul>
            By understanding these relationships, students can make <b>smarter, evidence-backed</b>
            decisions about how they spend their time and energy.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    box_style_red = "padding:26px; border-radius:22px; min-height:300px; display:flex; flex-direction:column; background:linear-gradient(135deg,#1e40af,#2563eb);"
    box_style_grn = "padding:26px; border-radius:22px; min-height:300px; display:flex; flex-direction:column; background:linear-gradient(135deg,#065f46,#059669);"
    box_style_blu = "padding:26px; border-radius:22px; min-height:300px; display:flex; flex-direction:column; background:linear-gradient(135deg,#7c3aed,#4f46e5);"
    inner = "background:white; padding:20px 25px; border-radius:14px; box-shadow:0px 4px 15px rgba(0,0,0,0.10); font-size:15px; flex-grow:1; display:flex; align-items:center; justify-content:center;"

    with col1:
        st.markdown(f"""
        <div style="{box_style_red}">
            <div style="text-align:center; font-size:20px; font-weight:700; color:white; margin-bottom:18px;">
                📊 DATASET SNAPSHOT
            </div>
            <div style="{inner}">
                <span style="text-align:center;">
                    <b>100 student records</b> collected across universities in Malaysia,
                    covering study habits, grades, attendance, and lifestyle factors.<br>
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="{box_style_grn}">
            <div style="text-align:center; font-size:20px; font-weight:700; color:white; margin-bottom:18px;">
                📈 KEY VARIABLES
            </div>
            <div style="{inner}">
                <span style="text-align:center;">
                    • Study hours  • Attendance rate
                    • GPA  • Parental support  • Sleep hours 
                    • Tutoring  • Extracurriculars
                    • Internet access • Motivation level<br>
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="{box_style_blu}">
            <div style="text-align:center; font-size:20px; font-weight:700; color:white; margin-bottom:18px;">
                🎯 OUR GOAL
            </div>
            <div style="{inner}">
                <span style="text-align:center;">
                    • Analyze how academic and lifestyle factors influence student performance<br>
                    • Help students understand their own study habits through data comparison<br>
                    • Provide personalized, data-driven insights for improvement<br>
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### 📋 Quick Academic Self-Assessment")

    col_a, col_b = st.columns(2)

    with col_a:
        study_hours = st.slider(
            "How many hours do you study per week (outside class)?",
            min_value=0,
            max_value=40,
            value=10,
            step=1
        )
        if study_hours < 5:
            st.warning("⚠️ Students who study fewer than 5 hours/week tend to score significantly below average. Consider scheduling dedicated study blocks.")
        elif 5 <= study_hours <= 15:
            st.info("📘 You're in the moderate range. Research shows 10–20 hours/week is associated with above-average grades for most courses.")
        else:
            st.success("✅ High study engagement! Make sure to balance this with adequate sleep and breaks to avoid burnout.")

    with col_b:
        attendance = st.selectbox(
            "How would you rate your class attendance?",
            ["Almost always (>90%)", "Usually (70–90%)", "Sometimes (50–70%)", "Rarely (<50%)"]
        )
        if attendance == "Almost always (>90%)":
            st.success("✅ Excellent! High attendance is one of the strongest predictors of academic success in our dataset.")
        elif attendance == "Usually (70–90%)":
            st.info("📘 Good attendance. Even a small improvement here can meaningfully lift your grades.")
        elif attendance == "Sometimes (50–70%)":
            st.warning("⚠️ Missing 30–50% of classes is linked to significantly lower GPA outcomes. Try to identify and remove attendance barriers.")
        else:
            st.error("🚨 Low attendance is the single strongest predictor of poor academic performance. Prioritising attendance is the highest-leverage change you can make.")
