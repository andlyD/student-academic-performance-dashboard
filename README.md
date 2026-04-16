<p align="center">
  <img src="https://img.shields.io/badge/Framework-Streamlit-ff4b4b?style=flat&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Language-Python%203.10+-3776AB?style=flat&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Analytics-Plotly-3f4f75?style=flat&logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Data-Pandas-150458?style=flat&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/ML-scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white">
  <img src="https://img.shields.io/badge/Status-Academic%20Project-6366F1?style=flat">
</p>

<h1 align="center">🎓 Student Academic Performance Dashboard</h1>
<p align="center"><i>A data-driven Streamlit application that explores how study habits, social media usage, and personal challenges shape university student CGPA outcomes.</i></p>

---

## 🌟 Overview

**Student Academic Performance Dashboard** is an interactive, analytics-driven web application built for university students, educators, and researchers. It visualises survey data collected from **88 real student respondents**, delivering meaningful insights into the relationships between daily study hours, social media consumption, coursework scores, and CGPA performance.

The dashboard goes beyond static charts — it lets users **filter by demographics**, **compare their own habits against peers**, and **explore interactive 3D visualisations**, all wrapped in a clean, professional UI.

Built with:
- **Streamlit** — reactive, multi-page web application
- **Plotly** — interactive charts, scatter plots, 3D visualisations
- **Pandas & NumPy** — data engineering and statistical analysis
- **scikit-learn** — machine learning classification models
- **Custom CSS** — polished, modern design system

---

## 📸 Dashboard Preview

### 🏠 Main Dashboard
> KPI cards, 5 interactive charts, and an Explore button linking to deeper analysis.

<!-- Replace with your actual screenshots after deployment -->
<p align="center">
  <img width="1200" alt="Main Dashboard" src="https://via.placeholder.com/1200x700?text=Main+Dashboard+Screenshot">
</p>

### 📋 Overview
> A snapshot of the survey methodology, data cleaning process, and respondent demographics.

<p align="center">
  <img width="1200" alt="Overview Page" src="https://via.placeholder.com/1200x700?text=Overview+Page+Screenshot">
</p>

### 📈 Performance Analysis
> Deep-dive analytics with inline filters, comparison cards, and 5 rich visualisations.

<p align="center">
  <img width="1200" alt="Performance Analysis" src="https://via.placeholder.com/1200x700?text=Performance+Analysis+Screenshot">
</p>

### 🙋 Know Yourself
> A personalised self-assessment quiz that classifies your study profile and gives tailored recommendations.

<p align="center">
  <img width="1200" alt="Know Yourself" src="https://via.placeholder.com/1200x700?text=Know+Yourself+Screenshot">
</p>

---

## 🗂️ Main Features

### 📊 Main Dashboard
- **4 live KPI cards** — Total Respondents, Average CGPA, Avg Daily Study Hours, Avg Social Media Hours
- **5 interactive charts** — Bar, Donut, Line, Scatter, and 3D Scatter
- **Explore buttons** that deep-link directly to the corresponding analysis section
- Fully responsive layout with card-bordered chart panels

### 📋 Overview
- Animated Lottie illustrations
- Breakdown of the survey dataset — 100 raw responses → 88 cleaned respondents
- Data cleaning rationale with transparency on dropped rows

### 📈 Performance Analysis
- **Inline filters** — Gender, Level of Study, CGPA Group
- **"How Do You Compare?"** — interactive sliders to benchmark your own habits against the 88 students
- **VIZ 1** — Bar chart: Average Daily Study Hours by CGPA Group
- **VIZ 2** — Donut chart: Study Challenge Category Distribution
- **VIZ 3** — Scatter plot: Social Media Hours vs Coursework Score with trendline
- **VIZ 4** — Line chart: Average CGPA by Social Media Usage with regression overlay
- **VIZ 5** — 3D interactive scatter: Study × Social Media × Coursework
- Raw data preview with download buttons (Raw CSV + Cleaned CSV)

### 🙋 Know Yourself
- **10-question self-assessment** covering study habits, time management, and social media use
- Score-based profiling → **At Risk / On Track / High Performer**
- Gauge bar, factor breakdown chart, and personalised recommendations
- Level-specific content: study games, video resources, and external links

---

## 📂 Project Structure

```text
📁 Student Academic Performance Dashboard/
│
├── 📄 app.py                          ← Main entry point
├── 📄 requirements.txt                ← Python dependencies
│
├── 📂 sidebarMenu/
│   ├── 📄 __init__.py
│   ├── 📄 DashboardPage.py            ← Dashboard + Performance Analysis pages
│   ├── 📄 KnowYourself.py             ← Self-assessment quiz page
│   └── 📄 Overview.py                 ← Overview & survey summary page
│
├── 📂 components/
│   ├── 📄 __init__.py
│   └── 📄 home_lottie.py             ← Lottie animation loader
│
├── 📂 assets/
│   ├── 📂 animations/
│   │   ├── 🎞️ client.json
│   │   └── 🎞️ students_jumping.json
│   ├── 📂 data/
│   │   ├── 📊 Student Study Hours & Academic Performance Survey (RAW).csv
│   │   └── 📊 Student Study Hours & Academic Performance Survey  (Cleaned).csv
│   └── 📂 video/
│       └── 🎬 roslan_vid.mp4
│
└── 📂 notebooks/
    ├── 📓 Code_for_Model_Training.ipynb   ← Data cleaning pipeline from RAW → Cleaned
    ├── 📓 EDA_StudyHours_AcademicPerformance.ipynb  ← Exploratory data analysis
    └── 📓 Model_Training.ipynb            ← ML classification (9 models + SMOTE)
```

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Web Framework | Streamlit 1.x |
| Visualisation | Plotly (Graph Objects + Express) |
| Data Engineering | Pandas, NumPy |
| Machine Learning | scikit-learn, imbalanced-learn |
| Animations | streamlit-lottie |
| Styling | Custom CSS (DM Sans, DM Mono) |
| Language | Python 3.10+ |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/student-academic-performance-dashboard.git
cd student-academic-performance-dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

### Requirements

```
streamlit==1.51.0
streamlit-lottie==0.0.5
pandas==2.3.3
numpy==2.3.4
plotly==6.3.1
```

---

## 📊 Dataset

| Property | Value |
|---|---|
| Source | Original survey — Google Forms |
| Raw Responses | 100 |
| Cleaned Responses | 88 (12 removed) |
| Features | 36 columns after encoding |
| Target Variable | CGPA (Low / Mid / High) |
| Collection Method | University student self-report |

**Rows removed during cleaning:**
- 4 rows — Gender: "Prefer not to say" (binary encoding not applicable)
- 3 rows — Study Method: "Others" (cannot be one-hot encoded)
- 5 rows — Study Challenge: blank, `-`, or `……` (no usable data)

---

## 🧪 Machine Learning (Notebooks)

The `notebooks/` folder contains a full ML pipeline separate from the Streamlit app:

1. **`Code_for_Model_Training.ipynb`** — loads RAW CSV, drops 12 invalid rows, maps free-text responses to categories, one-hot encodes all categorical features, and exports the Cleaned CSV
2. **`EDA_StudyHours_AcademicPerformance.ipynb`** — 5 interactive Plotly visualisations exploring CGPA, study hours, social media, and study challenges
3. **`Model_Training.ipynb`** — trains and evaluates 9 classification models using `RandomOverSampler` to handle class imbalance, with 10-fold stratified cross-validation and feature importance analysis

**Models evaluated:**
Logistic Regression · Decision Tree · SVM · KNN · Gaussian Naive Bayes · Random Forest · Gradient Boosting · AdaBoost · Neural Network (MLP)

---

## 🔑 Key Findings

| Finding | Insight |
|---|---|
| 📚 Study & CGPA | High achievers study **3.5+ hrs/day** — nearly double Low-CGPA students |
| 📱 Social Media | Students spending **5+ hrs/day** on social media have the lowest average CGPA |
| 🎯 Top Challenge | **Social Media Distraction** (22 students) is the #1 reported barrier |
| 💡 Quick Win | Cutting screen time to **< 1 hr/day** correlates with noticeably higher CGPA |

---

## 👥 Team

Developed by:

| Name | Role |
|---|---|
| **Andly Danny Anafiah** | Dashboard Development, Data Cleaning, ML Pipeline |
| **Bayu Fatwa Negara bin Alias** | Data Analysis, Visualisation, EDA |
| **Muhammad Roslan bin Abbas** | Survey Design, Overview Page, Content |

---

## 📝 License & Academic Disclaimer

This project was developed for **educational and academic purposes** as part of a university data visualisation assignment (XBDS3104N — Data Visualisation & Dashboard Design, January 2026).

The survey data was collected voluntarily from real students and is used solely for academic analysis. No personally identifiable information is stored or displayed.

---

<p align="center">Made with ❤️ using Streamlit · Plotly · Python</p>
