import streamlit as st
import pandas as pd
from pivottablejs import pivot_ui

df = pd.read_csv("mtcars.csv")

# Convert the DataFrame to a JSON string
json_data = df.to_json(orient="records")

# Render the PivotTable using pivottablejs
pivot_ui(json_data)

