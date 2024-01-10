import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from pivottablejs import pivot_ui
import tempfile

# Streamlit widget to upload a file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)

    # Use a temporary file to capture the pivot table HTML
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmpfile:
        pivot_ui(df, outfile_path=tmpfile.name)
        with open(tmpfile.name, "r") as f:
            pivot_html = f.read()

    # Render the HTML in the Streamlit app
    components.html(pivot_html, width=1500, height=1500)
