# import streamlit as st
# import pandas as pd
# import time
# from utils import ui 

# # 1. Config
# st.set_page_config(page_title="InsightNexus AI", layout="wide", page_icon="🔮")

# # 2. Inject Styling
# ui.setup_styling()

# # 3. SPLASH SCREEN (Only runs once per session)
# if "splash_shown" not in st.session_state:
#     ui.splash_screen()
#     st.session_state.splash_shown = True

# # 4. HEADER
# with st.container():
#     st.markdown("<h1 style='text-align: center; color: #6c5ce7;'>InsightNexus AI Hub</h1>", unsafe_allow_html=True)
#     st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #636e72;'>Your Central Command for Enterprise Intelligence</p>", unsafe_allow_html=True)

# st.divider()

# # 5. MAIN NAVIGATION HUB
# col1, col2 = st.columns(2, gap="large")

# with col1:
#     st.markdown("### 📤 Upload Dataset")
    
#     # Init State
#     if "df" not in st.session_state:
#         st.session_state.df = None
#         st.session_state.file_name = None

#     uploaded_file = st.file_uploader(
#         "Drop your CSV System Logs here", 
#         type=["csv"], 
#         help="Supports files up to 2GB. Large files auto-sampled."
#     )

#     if uploaded_file:
#         try:
#             if uploaded_file.size > 200 * 1024 * 1024:
#                 st.warning("⚠️ Large file. Sampling 10k rows for speed.")
#                 df = pd.read_csv(uploaded_file, nrows=10000)
#             else:
#                 df = pd.read_csv(uploaded_file)

#             st.session_state.df = df
#             st.session_state.file_name = uploaded_file.name
            
#             st.balloons() # Playful effect on success
#             st.success(f"✅ {len(df):,} Records Ingested Successfully!")
            
#         except Exception as e:
#             st.error(f"Ingestion Failed: {e}")

# with col2:
#     st.markdown("### 🚀 Navigate to Modules")
    
#     # Navigation Cards (Using st.container for grouping)
#     with st.container():
#         st.info("Where would you like to go?")
        
#         # Grid of buttons
#         c1, c2 = st.columns(2)
#         with c1:
#             if st.button("📈 Manager Insights", use_container_width=True):
#                 st.switch_page("pages/02_📈_Manager_Insights.py")
#         with c2:
#             if st.button("🔬 Analyst Lab", use_container_width=True):
#                 st.switch_page("pages/03_🔬_Analyst_Lab.py")
                
#         if st.button("📜 View Audit Trails", use_container_width=True):
#             st.switch_page("pages/04_📜_Audit_Trails.py")

# # 6. FOOTER INFO
# st.divider()
# st.markdown("""
# <div style='text-align: center; color: #b2bec3; font-size: 0.8rem;'>
#     🔒 Secure Environment | v2.5.0 | Powered by InsightNexus Engine
# </div>
# """, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import time
from utils import ui 
from streamlit_lottie import st_lottie

# 1. Config
st.set_page_config(page_title="Prism Intelligence", layout="wide", page_icon="🔮")
ui.setup_styling()

# 2. Hero Section with Lottie
col_text, col_anim = st.columns([1.5, 1], gap="large")

with col_text:
    st.markdown("""
        <h1 style='font-size: 3.5rem; font-weight: 800; background: -webkit-linear-gradient(45deg, #6c5ce7, #00b894); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            Prism Intelligence
        </h1>
        <p style='font-size: 1.2rem; color: #636e72; line-height: 1.6;'>
            The <b>Autonomous Enterprise Engine</b>. 
            Upload raw system logs and watch our AI turn chaos into clear, actionable strategy in seconds.
        </p>
    """, unsafe_allow_html=True)
    
    # Init State
    if "df" not in st.session_state:
        st.session_state.df = None
        st.session_state.file_name = None

    uploaded_file = st.file_uploader("📂 Upload Enterprise Data (CSV)", type=["csv"])

with col_anim:
    # Load High-Quality Lottie Animation (AI Brain/Robot)
    lottie_ai = ui.load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")
    if lottie_ai:
        st_lottie(lottie_ai, height=300, key="ai_anim")
    else:
        st.image("https://cdn-icons-png.flaticon.com/512/2585/2585188.png", width=200)

st.divider()

# 3. Processing Logic
if uploaded_file:
    try:
        if uploaded_file.size > 200 * 1024 * 1024:
            st.warning("⚠️ Large file detected. Auto-sampling 10k rows.")
            df = pd.read_csv(uploaded_file, nrows=10000)
        else:
            df = pd.read_csv(uploaded_file)

        st.session_state.df = df
        st.session_state.file_name = uploaded_file.name
        
        st.success(f"✅ Data Ingested: {len(df):,} records ready for analysis.")
        
        # Navigation Hub
        st.markdown("### 🚀 Launch Module")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("📈 Manager Insights", use_container_width=True):
                st.switch_page("pages/02_📈_Manager_Insights.py")
        with c2:
            if st.button("🔬 Analyst Lab", use_container_width=True):
                st.switch_page("pages/03_🔬_Analyst_Lab.py")
        with c3:
            if st.button("📜 Audit Trails", use_container_width=True):
                st.switch_page("pages/04_📜_Audit_Trails.py")

    except Exception as e:
        st.error(f"Ingestion Error: {e}")