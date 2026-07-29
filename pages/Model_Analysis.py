import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from utils.styles import load_css
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

MAIN_CSS_PATH = PROJECT_ROOT / "styles" / "main.css"


def load_css(css_path: Path) -> None:
    """Load a CSS stylesheet into the current Streamlit page."""

    if not css_path.exists():
        st.error(f"CSS file not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")
    st.html(f"<style>{css}</style>")


load_css(MAIN_CSS_PATH)

with st.sidebar:
    st.markdown("## :material/school:  Placement System")
    st.caption("Student Placement Prediction")
    st.divider()
    
st.html('<div class="page-title-spacer" aria-hidden="true"></div>')
st.title("Model Analysis")

st.write(
    "This page compares the machine-learning models trained for "
    "student placement prediction."
)

st.divider()


# ---------------------------------------------------------
# Model comparison
# ---------------------------------------------------------
st.subheader("Model Comparison")

model_results = pd.DataFrame(
    {
        "Model": [
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],
        "Accuracy": [
            79.45,
            72.65,
            78.10
        ],
        "Placed Precision": [
            74,
            66,
            75
        ],
        "Placed Recall": [
            77,
            69,
            71
        ],
        "Placed F1-Score": [
            76,
            68,
            73
        ]
    }
)

st.dataframe(
    model_results,
    hide_index=True,
    use_container_width=True
)

best_model = model_results.loc[
    model_results["Accuracy"].idxmax()
]

st.success(
    f"Best-performing model: {best_model['Model']} "
    f"with {best_model['Accuracy']:.2f}% accuracy."
)


# ---------------------------------------------------------
# Accuracy chart
# ---------------------------------------------------------
st.subheader("Accuracy Comparison")

figure, axis = plt.subplots(figsize=(8, 4))

axis.bar(
    model_results["Model"],
    model_results["Accuracy"]
)

axis.set_ylabel("Accuracy (%)")
axis.set_ylim(0, 100)
axis.set_title("Model Accuracy Comparison")

for index, accuracy in enumerate(model_results["Accuracy"]):
    axis.text(
        index,
        accuracy + 1,
        f"{accuracy:.2f}%",
        ha="center"
    )

plt.xticks(rotation=10)
plt.tight_layout()

st.pyplot(figure, use_container_width=True)


# ---------------------------------------------------------
# Logistic Regression evaluation
# ---------------------------------------------------------
st.divider()
st.subheader("Logistic Regression Evaluation")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "79.45%")

with col2:
    st.metric("Placed Precision", "74%")

with col3:
    st.metric("Placed Recall", "77%")

with col4:
    st.metric("Placed F1-Score", "76%")


st.write("Confusion Matrix")

confusion_matrix_data = pd.DataFrame(
    [
        [954, 218],
        [193, 635]
    ],
    index=[
        "Actual Not Placed",
        "Actual Placed"
    ],
    columns=[
        "Predicted Not Placed",
        "Predicted Placed"
    ]
)

st.dataframe(
    confusion_matrix_data,
    use_container_width=True
)

st.info(
    """
    The model correctly predicted 954 not-placed students and
    635 placed students. It incorrectly predicted 218 not-placed
    students as placed and 193 placed students as not placed.
    """
)


# ---------------------------------------------------------
# Classification report summary
# ---------------------------------------------------------
st.subheader("Classification Report")

classification_report = pd.DataFrame(
    {
        "Class": [
            "Not Placed",
            "Placed",
            "Macro Average",
            "Weighted Average"
        ],
        "Precision": [
            0.83,
            0.74,
            0.79,
            0.80
        ],
        "Recall": [
            0.81,
            0.77,
            0.79,
            0.79
        ],
        "F1-Score": [
            0.82,
            0.76,
            0.79,
            0.79
        ],
        "Support": [
            1172,
            828,
            2000,
            2000
        ]
    }
)

st.dataframe(
    classification_report,
    hide_index=True,
    use_container_width=True
)


# ---------------------------------------------------------
# Feature importance
# ---------------------------------------------------------
st.divider()
st.subheader("Random Forest Feature Importance")

feature_importance = pd.DataFrame(
    {
        "Feature": [
            "HSC_Marks",
            "AptitudeTestScore",
            "SSC_Marks",
            "CGPA",
            "SoftSkillsRating",
            "Projects",
            "ExtracurricularActivities",
            "Workshops/Certifications",
            "Internships",
            "PlacementTraining"
        ],
        "Importance": [
            0.211044,
            0.178484,
            0.133290,
            0.120347,
            0.094343,
            0.073408,
            0.072964,
            0.058424,
            0.033324,
            0.024372
        ]
    }
)

st.dataframe(
    feature_importance,
    hide_index=True,
    use_container_width=True
)

importance_figure, importance_axis = plt.subplots(
    figsize=(9, 5)
)

importance_axis.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)

importance_axis.invert_yaxis()
importance_axis.set_xlabel("Importance")
importance_axis.set_title("Feature Importance")

plt.tight_layout()

st.pyplot(importance_figure, use_container_width=True)

st.info(
    """
    HSC marks and aptitude-test scores were the most influential
    features in the Random Forest model. Placement training and
    internships had comparatively lower importance in this dataset.
    """
)


# ---------------------------------------------------------
# Final conclusion
# ---------------------------------------------------------
st.divider()
st.subheader("Conclusion")

st.write(
    """
    Logistic Regression was selected as the final prediction model
    because it achieved the highest test accuracy and the best
    placed-class recall and F1-score among the tested models.

    Random Forest provided useful feature-importance information,
    while the unrestricted Decision Tree showed weaker test
    performance.
    """
)