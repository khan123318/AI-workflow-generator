import streamlit as st
import pandas as pd
import time
from utils import ui 

# 1. Config & Styling
st.set_page_config(page_title="Enterprise AI Hub", layout="wide", page_icon="🚀")

# --- 🚀 SPLASH SCREEN LOGIC ---
if "splash_seen" not in st.session_state:
    st.session_state.splash_seen = False

if not st.session_state.splash_seen:
    splash = st.empty()
    with splash.container():
        st.markdown(
            """
            <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 70vh;">
                <img src="https://cdn-icons-png.flaticon.com/512/2585/2585188.png" width="100" style="margin-bottom: 20px;">
                <h1 style="font-size: 3.5rem; font-weight: 800; color: #18181b; margin: 0;">AI Nexus</h1>
                <p style="font-size: 1.2rem; color: #71717a; margin-top: 10px;">Initializing Enterprise Core...</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    time.sleep(2.5) # Wait 2.5 seconds
    splash.empty()  # Remove Splash
    st.session_state.splash_seen = True

# 2. Main App Styling
ui.setup_styling()

# 3. Hero Section
with st.container():
    st.title("Enterprise AI Nexus")
    st.markdown("""
        <p style='font-size: 1.25rem; color: #52525b; max-width: 600px; line-height: 1.6;'>
            Transform raw data into <b>Strategic Intelligence</b>. 
            Upload your system logs to activate the autonomous agent workflow.
        </p>
    """, unsafe_allow_html=True)

st.divider()

# 4. Main Action Area
col_upload, col_status = st.columns([2, 1], gap="large")

with col_upload:
    st.subheader("📂 Ingest Data")
    
    if "df" not in st.session_state:
        st.session_state.df = None
        st.session_state.file_name = None

    def reset_state():
        st.session_state.df = None

    uploaded_file = st.file_uploader(
        "Upload CSV System Logs", 
        type=["csv"], 
        on_change=reset_state,
        help="Optimized for files up to 200MB. Larger files will be auto-sampled."
    )

with col_status:
    st.subheader("🖥️ System Health")
    ui.card("AI Engine", "Online", "Model: Phi-3 / Qwen", "🟢")
    
# 5. Processing Logic
if uploaded_file:
    try:
        # File Handling
        if uploaded_file.size > 200 * 1024 * 1024:
            st.warning("⚠️ Large file detected. Auto-sampling 10k rows.")
            df = pd.read_csv(uploaded_file, nrows=10000)
        else:
            df = pd.read_csv(uploaded_file)

        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        
        st.success(f"✅ Successfully ingested {len(df):,} records.")
        
        # --- NAVIGATION SECTION ---
        st.divider()
        st.markdown("### 🎯 Where would you like to go?")

        col_nav1, col_nav2 = st.columns(2)

        with col_nav1:
            with st.container(border=True):
                st.markdown("#### 👔 Manager Portal")
                st.caption("For Executives & Strategy")
                st.write("• High-level Revenue Trends")
                st.write("• AI Strategic Advice")
                # Links to the NEW file structure
                st.page_link("pages/1_📈_Manager_Portal.py", label="Go to Manager Dashboard", icon="📈")

        with col_nav2:
            with st.container(border=True):
                st.markdown("#### 🔬 Analyst Workbench")
                st.caption("For Data Engineers")
                st.write("• Data Cleaning Pipeline")
                st.write("• Statistical Deep Dives")
                # Links to the NEW file structure
                st.page_link("pages/2_🔬_Analyst_Workbench.py", label="Go to Analyst Workbench", icon="🧪")

    except Exception as e:
        st.error(f"Ingestion Error: {e}")