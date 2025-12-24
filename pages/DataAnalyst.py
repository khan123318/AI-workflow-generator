import streamlit as st
import sys
import os
import plotly.express as px
import pandas as pd

# --- CONNECTING TO Waheeba's CODE (SRC) ---
# This line allows us to import from the 'src' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# NOW we can import the Lead's files
from src.analyzer import DataAnalyzer
from src.data_processor import DataProcessor

st.title("🔬 Analyst Workbench")

"""
if "df" not in st.session_state or st.session_state.df is None:
    st.warning("⚠️ Please upload data on the Home Page first.")
else:
    st.write("✅ Data Received from Home Page.")
    
    # TODO: Teammate B - Add your cleaning logic here using DataProcessor
    st.info("🛠️ This page is under construction. Features to add: Data Cleaning, Deep Statistics.")
"""

# --- Path to default CSV ---
default_csv_path = r"D:\Aiza\AI-Workflow-Generator\sample_sales.csv"

# --- Load default CSV ---
def load_default_csv(path):
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        st.error(f"Error loading default CSV: {e}")
        return pd.DataFrame()

# --- Determine which data to use ---
if "df" in st.session_state and st.session_state.df is not None:
    df = st.session_state.df
    st.write("✅ Data received from Home Page.")
else:
    df = load_default_csv(default_csv_path)
    if df.empty:
        st.warning("⚠️ Default dataset could not be loaded. Please upload data on the Home Page.")

# --- Function to show Plotly chart ---
def show_sales_chart(data):
    # Attempt to automatically detect a numeric column for y-axis
    numeric_cols = data.select_dtypes(include='number').columns.tolist()
    if not numeric_cols:
        st.warning("No numeric columns found to plot.")
        return
    
    # Use first numeric column for y-axis
    fig = px.line(
        data,
        x=data.columns[0],  # assume first column is X (Date or similar)
        y=numeric_cols[0],
        title=f"{numeric_cols[0]} Over Time",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Display the chart ---
if not df.empty:
    show_sales_chart(df)
