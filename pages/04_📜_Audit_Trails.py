import streamlit as st
import pandas as pd
import sys
import os

# --- CONNECT TO MODULES ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules import database
from utils import ui

# 1. SETUP
st.set_page_config(page_title="Audit Trails", layout="wide")
ui.setup_styling()

st.title("📜 System Audit Trails")

# 2. FETCH REAL DATA
try:
    logs = database.fetch_logs()
except Exception as e:
    st.error(f"Database Error: {e}")
    logs = []

# 3. METRICS SECTION (Real Calculations)
if logs:
    df_logs = pd.DataFrame(logs)
    
    # Calculate Real Stats
    total_logs = len(df_logs)
    
    # Count unique roles (e.g. "Manager", "Analyst") to show real activity
    if 'user_role' in df_logs.columns:
        active_users = df_logs['user_role'].nunique()
    else:
        active_users = 1 
        
    # Get last time
    if 'timestamp' in df_logs.columns and not df_logs.empty:
        # Convert to datetime if it's a string
        df_logs['timestamp'] = pd.to_datetime(df_logs['timestamp'])
        last_active = df_logs['timestamp'].max().strftime("%H:%M")
    else:
        last_active = "--:--"

    # Display Cards
    col1, col2, col3 = st.columns(3)
    with col1:
        ui.card("Total Events", f"{total_logs}", "System Actions", "📝")
    with col2:
        ui.card("Active Roles", f"{active_users}", "Unique Accessors", "👥")
    with col3:
        ui.card("Last Sync", f"{last_active}", "UTC Time", "🕒")

    st.divider()
    
    # 4. SEARCH & TABLE
    search_term = st.text_input("🔍 Search Logs", placeholder="Type action or user...")
    
    # Search Logic
    if search_term:
        mask = df_logs.astype(str).apply(lambda x: x.str.contains(search_term, case=False)).any(axis=1)
        df_display = df_logs[mask]
    else:
        df_display = df_logs
        
    # Show Table
    st.dataframe(
        df_display, 
        use_container_width=True,
        hide_index=True,
        column_config={
            "created_at": "Timestamp",
            "action": "Activity",
            "user_role": "User Role"
        }
    )

else:
    st.info("No logs found in the database yet.")