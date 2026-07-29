from pathlib import Path

import streamlit as st


def load_css() -> None:
    """Load the shared CSS file for all Streamlit pages."""

    project_root = Path(__file__).resolve().parent.parent
    css_path = project_root / "styles" / "main.css"

    if not css_path.exists():
        st.warning(f"CSS file not found: {css_path}")
        return

    css = css_path.read_text(encoding="utf-8")

    st.html(f"<style>{css}</style>")