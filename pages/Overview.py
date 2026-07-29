import streamlit as st
from utils.styles import load_css
import base64
import mimetypes
from pathlib import Path
load_css()

# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

CSS_PATH = PROJECT_ROOT / "styles" / "main.css"
LOGO_PATH = PROJECT_ROOT / "assets" / "logo.png"


# ---------------------------------------------------------
# Helper functions
# ---------------------------------------------------------
def load_css(css_path: Path) -> None:
    """Load the shared CSS file."""

    if not css_path.exists():
        st.error(f"CSS file not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


def get_image_data_uri(image_path: Path) -> str:
    """Convert an image into a browser-compatible Base64 data URI."""

    if not image_path.exists():
        return ""

    mime_type, _ = mimetypes.guess_type(image_path.name)
    mime_type = mime_type or "image/png"

    encoded_image = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{encoded_image}"


# ---------------------------------------------------------
# Load CSS and logo
# ---------------------------------------------------------
load_css(CSS_PATH)

logo_data_uri = get_image_data_uri(LOGO_PATH)


# ---------------------------------------------------------
# Hero section
# ---------------------------------------------------------
with st.container(key="overview_hero"):

    left_column, right_column = st.columns(
        [1.15, 0.85],
        gap="large",
        vertical_alignment="center",
    )

    # -----------------------------------------------------
    # Left section
    # -----------------------------------------------------
    with left_column:

        st.html(
            """
            <div class="hero-copy">
                <div class="hero-eyebrow">
                    <span class="hero-eyebrow-dot"></span>
                    <span>STUDENT PLACEMENT ANALYSIS</span>
                </div>

                <h1 class="hero-title">
                    Placement Prediction
                    <span>System</span>
                </h1>

                <p class="hero-description">
                    Analyze academic performance, practical experience,
                    aptitude scores and soft skills to estimate a
                    student’s placement outcome.
                </p>
            </div>
            """
        )

        if st.button(
            "Predict Placement",
            type="primary",
            icon=":material/arrow_forward:",
            key="hero_prediction_button",
        ):
            st.switch_page("pages/Prediction.py")

    # -----------------------------------------------------
    # Right section
    # -----------------------------------------------------
    with right_column:

        if logo_data_uri:
            logo_html = f"""
            <div class="hero-logo-area">

                <div class="hero-logo-grid"></div>

                <div class="hero-logo-orbit hero-logo-orbit-one"></div>
                <div class="hero-logo-orbit hero-logo-orbit-two"></div>

                <div class="hero-logo-glow"></div>

                <div class="hero-logo-float">
                    <div class="hero-logo-tilt">
                        <img
                            src="{logo_data_uri}"
                            class="hero-logo-image"
                            alt="Placement Prediction System logo"
                        >
                    </div>
                </div>

                <span class="hero-floating-particle particle-one"></span>
                <span class="hero-floating-particle particle-two"></span>
                <span class="hero-floating-particle particle-three"></span>

            </div>
            """

            st.html(logo_html)

        else:
            st.error("Logo not found at assets/logo.png")

with st.sidebar:
    st.markdown("### :material/article_person:  Placement System")
    st.caption("Student Placement Prediction")
    st.divider()
    
st.title("Placement Prediction System")

st.subheader("Student Placement Analysis Dashboard")

st.write(
    """
    This application analyzes students' academic performance,
    practical experience, aptitude scores, and soft skills to
    estimate their placement outcome using machine learning.
    """
)

st.divider()

# Dashboard metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Model Accuracy",
        value="79.45%"
    )

with col2:
    st.metric(
        label="Dataset Records",
        value="10,000"
    )

with col3:
    st.metric(
        label="Placed Students",
        value="4,197"
    )

with col4:
    st.metric(
        label="Not Placed",
        value="5,803"
    )


st.divider()

st.subheader("Project Overview")

st.write(
    """
    The system uses a Logistic Regression model to predict whether
    a student is likely to be placed.

    The model considers academic marks, internships, projects,
    certifications, aptitude performance, soft skills, extracurricular
    activities, and placement training.
    """
)

st.info(
    "Best-performing model: Logistic Regression with 79.45% test accuracy."
)