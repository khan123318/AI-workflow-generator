# pages/History_Logs.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

import streamlit as st
import pandas as pd
from database import fetch_logs_df

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

# Page configuration
st.set_page_config(page_title="History Logs", layout="wide")
st.title("History Logs")

# Fetch logs from backend
logs_df = fetch_logs_df()

# Check if there are any logs
if logs_df.empty:
    st.info("No logs yet.")
else:
    # Convert timestamp to datetime and sort
    logs_df["created_at"] = pd.to_datetime(logs_df["created_at"])
    logs_df = logs_df.sort_values("created_at", ascending=False)

    # Optional: Filter by user
    user_filter = st.selectbox("Filter by user", options=["All"] + logs_df["user"].unique().tolist())
    
    if user_filter != "All":
        filtered_df = logs_df[logs_df["user"] == user_filter]
    else:
        filtered_df = logs_df

    # Display only the filtered table
    st.dataframe(
        filtered_df[["user", "action", "created_at"]],
        use_container_width=True
    )
