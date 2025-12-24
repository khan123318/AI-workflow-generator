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
default_csv_path = r"D:\Aiza\ai_report_generator\superstore_data.csv"

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

# modules/visuals.py
import plotly.express as px
import pandas as pd



# -----------------------------
# Analyst Portal Charts
# -----------------------------

def multi_line_chart(df: pd.DataFrame, x_col: str, y_cols: list, title="Multi-Line Chart"):
    """
    Line chart comparing multiple metrics
    """
    fig = px.line(df, x=x_col, y=y_cols, title=title)
    fig.update_layout(hovermode="x unified")
    return fig

def box_outlier_chart(df: pd.DataFrame, y_col: str, title="Outlier Detection"):
    """
    Box plot for detecting outliers
    """
    fig = px.box(df, y=y_col, title=title, points="all")
    return fig

def heatmap_correlation(df: pd.DataFrame, title="Correlation Heatmap"):
    """
    Correlation matrix heatmap
    """
    corr = df.corr()
    fig = px.imshow(
        corr, text_auto=True, color_continuous_scale="RdBu_r", title=title
    )
    return fig

def scatter_anomaly_highlight(df: pd.DataFrame, x_col: str, y_col: str, anomaly_col: str, title="Anomaly Detection"):
    """
    Scatter chart highlighting anomalies for Analyst portal
    """
    fig = px.scatter(
        df, x=x_col, y=y_col, color=anomaly_col.astype(str),
        title=title,
        color_discrete_map={"0": "blue", "1": "red"},
        hover_data=df.columns
    )
    fig.update_layout(hovermode="closest")
    return fig


# --- Display the chart ---
if not df.empty:
    show_sales_chart(df)

