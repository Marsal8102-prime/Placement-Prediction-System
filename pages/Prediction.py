from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from utils.styles import load_css

load_css()

with st.sidebar:
    st.markdown("### :material/article_person:  Placement System")
    st.caption("Student Placement Prediction")
    st.divider()

st.html('<div class="page-title-spacer" aria-hidden="true"></div>')
st.title("Placement Prediction")

st.write(
    "Enter the student's academic and skill-related details "
    "to predict the likely placement outcome."
)

st.divider()


# ---------------------------------------------------------
# Locate and load model files
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_PATH = PROJECT_ROOT / "placement_model.pkl"
SCALER_PATH = PROJECT_ROOT / "scaler.pkl"


@st.cache_resource
def load_model_files():
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


try:
    model, scaler = load_model_files()

except FileNotFoundError:
    st.error(
        "The model or scaler file was not found. "
        "Make sure placement_model.pkl and scaler.pkl "
        "are inside the main project folder."
    )
    st.stop()

except Exception as error:
    st.error(f"Unable to load the model files: {error}")
    st.stop()


# ---------------------------------------------------------
# Student input form
# ---------------------------------------------------------
with st.form("prediction_form"):

    st.subheader("Academic Details")

    col1, col2 = st.columns(2)

    with col1:
        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=7.5,
            step=0.1
        )

        ssc_marks = st.number_input(
            "SSC Marks (%)",
            min_value=0,
            max_value=100,
            value=75,
            step=1
        )

    with col2:
        aptitude_score = st.number_input(
            "Aptitude Test Score",
            min_value=0,
            max_value=100,
            value=75,
            step=1
        )

        hsc_marks = st.number_input(
            "HSC Marks (%)",
            min_value=0,
            max_value=100,
            value=75,
            step=1
        )


    st.subheader("Experience and Skills")

    col3, col4 = st.columns(2)

    with col3:
        internships = st.number_input(
            "Number of Internships",
            min_value=0,
            max_value=10,
            value=1,
            step=1
        )

        projects = st.number_input(
            "Number of Projects",
            min_value=0,
            max_value=20,
            value=2,
            step=1
        )

        workshops = st.number_input(
            "Workshops / Certifications",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

    with col4:
        soft_skills = st.slider(
            "Soft Skills Rating",
            min_value=1.0,
            max_value=5.0,
            value=3.5,
            step=0.1
        )

        extracurricular = st.selectbox(
            "Extracurricular Activities",
            options=["No", "Yes"]
        )

        placement_training = st.selectbox(
            "Placement Training",
            options=["No", "Yes"]
        )


    submitted = st.form_submit_button(
        "Predict Placement",
        use_container_width=True,
        type="primary"
    )


# ---------------------------------------------------------
# Make prediction
# ---------------------------------------------------------
if submitted:

    extracurricular_value = 1 if extracurricular == "Yes" else 0
    placement_training_value = 1 if placement_training == "Yes" else 0

    student_data = pd.DataFrame(
        [[
            cgpa,
            internships,
            projects,
            workshops,
            aptitude_score,
            soft_skills,
            extracurricular_value,
            placement_training_value,
            ssc_marks,
            hsc_marks
        ]],
        columns=[
            "CGPA",
            "Internships",
            "Projects",
            "Workshops/Certifications",
            "AptitudeTestScore",
            "SoftSkillsRating",
            "ExtracurricularActivities",
            "PlacementTraining",
            "SSC_Marks",
            "HSC_Marks"
        ]
    )

    try:
        student_scaled = scaler.transform(student_data)

        prediction = model.predict(student_scaled)[0]
        probability = model.predict_proba(student_scaled)[0]

        not_placed_probability = probability[0] * 100
        placed_probability = probability[1] * 100

        st.divider()
        st.subheader("Prediction Result")

        if prediction == 1:
            st.success("The student is likely to be placed.")
            st.metric(
                "Placement Probability",
                f"{placed_probability:.2f}%"
            )

        else:
            st.warning("The student is likely to be not placed.")
            st.metric(
                "Not-Placement Probability",
                f"{not_placed_probability:.2f}%"
            )

        st.write("Probability breakdown")

        result_table = pd.DataFrame(
            {
                "Outcome": ["Not Placed", "Placed"],
                "Probability": [
                    f"{not_placed_probability:.2f}%",
                    f"{placed_probability:.2f}%"
                ]
            }
        )

        st.dataframe(
            result_table,
            hide_index=True,
            width='stretch'
        )

        st.progress(
            min(100, max(0, int(round(placed_probability))))
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")


st.divider()

st.caption(
    "This system provides an educational prediction based on the "
    "trained machine-learning model. It should not be used as an "
    "official recruitment decision."
)