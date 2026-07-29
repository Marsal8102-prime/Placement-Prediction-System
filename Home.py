import streamlit as st
from utils.styles import load_css
import base64
from pathlib import Path

st.set_page_config(
    page_title="Placement Prediction System",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
    
)

# =========================================================
# PROJECT PATHS
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parent
CSS_PATH = PROJECT_ROOT / "styles" / "home.css"


# =========================================================
# LOAD SHARED CSS
# =========================================================

def load_css(css_path: Path) -> None:
    """Load the shared project stylesheet."""

    if not css_path.exists():
        st.error(f"CSS file not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")

load_css(PROJECT_ROOT / "styles" / "main.css")
load_css(CSS_PATH)

st.html(
    """
    <link rel="stylesheet"
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,400,0,0">
    """
)

# =========================================================
# HERO SECTION
# =========================================================

with st.container(key="home_hero"):

    hero_left, hero_right = st.columns(
        [1.25, 0.75],
        gap="large",
        vertical_alignment="center",
    )

    with hero_left:
        st.html(
            f"""
            <section class="home-hero-copy">

                <div class="home-eyebrow">
                    <span class="material-symbols-rounded home-eyebrow-icon">
                        school
                    </span>

                    STUDENT PLACEMENT ANALYSIS
                </div>

                <h1 class="home-hero-title">
                    Placement Prediction
                    <span>System</span>
                </h1>

                <p class="home-hero-description">
                    Predict placement outcomes using academic performance,
                    practical experience, aptitude scores and soft skills.
                    Explore the project, enter student information and review
                    the trained model's performance.
                </p>

            </section>
            """
        )

        if st.button(
            "Open Dashboard",
            icon=":material/arrow_forward:",
            type="primary",
            key="home_dashboard_button",
        ):
            st.switch_page("pages/Overview.py")

    with hero_right:
        st.html(
            f"""
            <div class="home-hero-visual">

                <div class="home-visual-grid"></div>
                <div class="home-visual-glow"></div>

                <div class="home-project-panel">

                    <div class="home-project-panel-icon">
                        <span class="material-symbols-rounded">
                            monitoring
                        </span> 
                    </div>

                    <div class="home-project-panel-label">
                        PLACEMENT ANALYTICS
                    </div>

                    <div class="home-project-panel-value">
                        79.45%
                    </div>

                    <div class="home-project-panel-caption">
                        Logistic Regression accuracy
                    </div>

                    <div class="home-progress-track">
                        <span></span>
                    </div>

                    <div class="home-project-panel-footer">
                        <span>Model evaluated</span>
                        <strong>Ready</strong>
                    </div>

                </div>

                <span class="home-visual-dot dot-one"></span>
                <span class="home-visual-dot dot-two"></span>
                <span class="home-visual-dot dot-three"></span>

            </div>
            """
        )


# =========================================================
# QUICK OVERVIEW
# =========================================================

st.html(
    """
    <div class="home-section-heading">
        <span>PROJECT SUMMARY</span>
        <h2>Quick Overview</h2>
        <p>
            Key information about the dataset, trained model and
            application structure.
        </p>
    </div>
    """
)

stat_1, stat_2, stat_3, stat_4 = st.columns(4, gap="medium")

statistics = [
    (
        stat_1,
        "verified",
        "79.45%",
        "Model Accuracy",
        "Logistic Regression",
    ),
    (
        stat_2,
        "database",
        "10,000",
        "Student Records",
        "Placement dataset",
    ),
    (
        stat_3,
        "memory",
        "Logistic",
        "Regression Model",
        "Binary classification",
    ),
    (
        stat_4,
        "layers",
        "3",
        "Project Modules",
        "Overview, prediction and analysis",
    ),
]

for column, icon_name, value, label, description in statistics:
    with column:
        st.html(
            f"""
            <article class="home-stat-card">

                <div class="home-stat-icon">
                    <span class="material-symbols-rounded">
                        {icon_name}
                    </span>
                </div>

                <div class="home-stat-value">{value}</div>
                <div class="home-stat-label">{label}</div>
                <div class="home-stat-description">
                    {description}
                </div>

            </article>
            """
        )

# =========================================================
# PROJECT MODULES
# =========================================================

st.html(
    """
    <div class="home-section-heading home-modules-heading">
        <span>APPLICATION MODULES</span>
        <h2>Explore the Platform</h2>
        <p>
            Open a module to understand the project, make a placement
            prediction or review model performance.
        </p>
    </div>
    """
)


overview_col, prediction_col, analysis_col = st.columns(
    3,
    gap="large",
)


# ---------------------------------------------------------
# Overview card
# ---------------------------------------------------------

with overview_col:
    with st.container(key="overview_module_card"):

        st.html(
            f"""
            <article class="home-module-content">

                <div class="home-module-top">
                   <div class="home-module-icon">
                        <span class="material-symbols-rounded">
                            dashboard
                        </span>
                    </div>

                </div>

                <h3>Overview Dashboard</h3>

                <p>
                    Explore the project introduction, objectives, workflow,
                    dataset information and the main features of the system.
                </p>

                <div class="home-module-details">
                    <span>Project workflow</span>
                    <span>Dataset details</span>
                    <span>System features</span>
                </div>

            </article>
            """
        )

        if st.button(
            "Open Overview",
            icon=":material/arrow_forward:",
            key="open_overview",
            use_container_width=True,
        ):
            st.switch_page("pages/Overview.py")


# ---------------------------------------------------------
# Prediction card
# ---------------------------------------------------------

with prediction_col:
    with st.container(key="prediction_module_card"):

        st.html(
            f"""
            <article class="home-module-content">

                <div class="home-module-top">
                    <div class="home-module-icon">
                        <span class="material-symbols-rounded">
                            track_changes
                        </span>
                    </div>

                </div>

                <h3>Placement Prediction</h3>

                <p>
                    Enter academic and skill-based student information to
                    estimate whether the student is likely to be placed.
                </p>

                <div class="home-module-details">
                    <span>Academic details</span>
                    <span>Experience and skills</span>
                    <span>Placement outcome</span>
                </div>

            </article>
            """
        )

        if st.button(
            "Start Prediction",
            icon=":material/arrow_forward:",
            key="open_prediction",
            use_container_width=True,
        ):
            st.switch_page("pages/Prediction.py")


# ---------------------------------------------------------
# Analysis card
# ---------------------------------------------------------

with analysis_col:
    with st.container(key="analysis_module_card"):

        st.html(
            f"""
            <article class="home-module-content">

                <div class="home-module-top">
                    <div class="home-module-icon">
                        <span class="material-symbols-rounded">
                            analytics
                        </span>
                    </div>
  
                </div>

                <h3>Model Analysis</h3>

                <p>
                    Review the model's accuracy, confusion matrix,
                    classification report and important placement factors.
                </p>

                <div class="home-module-details">
                    <span>Evaluation metrics</span>
                    <span>Confusion matrix</span>
                    <span>Feature importance</span>
                </div>

            </article>
            """
        )

        if st.button(
            "View Analysis",
            icon=":material/arrow_forward:",
            key="open_analysis",
            use_container_width=True,
        ):
            st.switch_page("pages/Model_Analysis.py")


# =========================================================
# WHY USE THIS SYSTEM
# =========================================================

st.html(
    """
    <div class="home-section-heading home-features-heading">
        <span>PROJECT FEATURES</span>
        <h2>Why Use This System?</h2>
        <p>
            The project combines placement prediction with understandable
            data and model insights.
        </p>
    </div>
    """
)

feature_1, feature_2, feature_3 = st.columns(3, gap="large")

features = [
    (
        feature_1,
        "track_changes",
        "Placement Prediction",
        (
            "Estimate a student's placement outcome using a trained "
            "machine-learning model."
        ),
    ),
    (
        feature_2,
        "insights",
        "Student Insights",
        (
            "Analyze academic performance, practical experience, "
            "aptitude and soft-skill information."
        ),
    ),
    (
        feature_3,
        "visibility",
        "Model Transparency",
        (
            "Understand model performance through accuracy, evaluation "
            "metrics and visual analysis."
        ),
    ),
]

for column, icon_name, title, description in features:
    with column:
        st.html(
            f"""
            <article class="home-feature-card">

                <div class="home-feature-icon">
                    <span class="material-symbols-rounded">
                        {icon_name}
                    </span>
                </div>

                <div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>

            </article>
            """
        )

# =========================================================
# TECHNOLOGY SECTION
# =========================================================

st.html(
    """
    <section class="home-technology-section">

        <div class="home-technology-copy">
            <span>TECHNOLOGIES USED</span>

            <h2>Built with Python and Machine Learning</h2>

            <p>
                This academic placement prediction project uses commonly
                adopted Python tools for data analysis, model training and
                interactive application development.
            </p>
        </div>

        <div class="home-technology-list">
            <span>Python</span>
            <span>Streamlit</span>
            <span>Scikit-learn</span>
            <span>Pandas</span>
            <span>NumPy</span>
        </div>

    </section>
    """
)


# =========================================================
# FOOTER
# =========================================================

st.html(
    """
    <footer class="home-footer">
        <p>
            Placement Prediction System
            <span></span>
            Student Machine Learning Project
        </p>
    </footer>
    """
)