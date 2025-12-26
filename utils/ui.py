import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie

def load_lottie_url(url: str):
    """
    Loads a Lottie animation from a URL.
    """
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def setup_styling():
    """
    Injects the 'Prism Intelligence' Design System.
    Features: Custom Font (Outfit), Skeleton Loaders, Gradient Sidebar.
    """
    st.markdown("""
    <style>
        /* 1. CUSTOM FONT: OUTFIT */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        html, body, [class*="css"], font, button, input {
            font-family: 'Outfit', sans-serif !important; 
            color: #2d3436;
        }
        
        /* 2. SKELETON LOADER ANIMATION (The Shimmer) */
        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }
        .skeleton {
            animation: shimmer 2s infinite linear;
            background: linear-gradient(to right, #f0f0f0 4%, #e0e0e0 25%, #f0f0f0 36%);
            background-size: 1000px 100%;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        .skeleton-text { height: 20px; width: 100%; }
        .skeleton-card { height: 150px; width: 100%; }
        .skeleton-title { height: 30px; width: 60%; margin-bottom: 15px; }

        /* 3. SIDEBAR GRADIENT */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
            border-right: 1px solid #dee2e6;
        }

        /* 4. BUTTONS - POPPY & COLORFUL */
        .stButton > button {
            background: linear-gradient(45deg, #6c5ce7, #a29bfe);
            color: white !important;
            border: none;
            border-radius: 12px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(108, 92, 231, 0.2);
        }
        .stButton > button:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 10px 20px rgba(108, 92, 231, 0.4);
        }

        /* 5. GLASSMORPHISM CARDS */
        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.05);
            transition: transform 0.2s;
        }
        div[data-testid="stMetric"]:hover {
            transform: translateY(-5px);
            border-color: #6c5ce7;
        }
    </style>
    """, unsafe_allow_html=True)

def render_skeleton_loader():
    """
    Renders a fake 'shimmering' UI while AI is thinking.
    """
    st.markdown("""
        <div class="skeleton skeleton-title"></div>
        <div class="skeleton skeleton-text"></div>
        <div class="skeleton skeleton-text"></div>
        <div class="skeleton skeleton-text" style="width: 80%;"></div>
    """, unsafe_allow_html=True)

def card(title, value, sub_text, icon="📊", help_text=None):
    """
    Renders a 'Prism' Metric Card.
    """
    tooltip_html = f"""<span title="{help_text}" style="cursor: help; color: #a29bfe; font-size: 0.8rem; margin-left: 5px;">(ℹ️)</span>""" if help_text else ""

    html_code = f"""
    <div style="background: white; border-radius: 20px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid #f0f0f0; margin-bottom: 20px; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -20px; right: -20px; width: 100px; height: 100px; background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%); opacity: 0.1; border-radius: 50%;"></div>
        <div style="display: flex; justify-content: space-between; align-items: flex-start; position: relative; z-index: 1;">
            <div>
                <span style="font-size: 0.85rem; font-weight: 600; color: #b2bec3; text-transform: uppercase; letter-spacing: 1px;">
                    {title} {tooltip_html}
                </span>
                <div style="font-size: 2.2rem; font-weight: 800; color: #2d3436; margin: 8px 0;">
                    {value}
                </div>
                <div style="font-size: 0.9rem; color: #00b894; font-weight: 600; display: flex; align-items: center; gap: 5px;">
                    <span>↑</span> {sub_text}
                </div>
            </div>
            <div style="background: linear-gradient(135deg, #a29bfe 0%, #6c5ce7 100%); color: white; width: 48px; height: 48px; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; box-shadow: 0 8px 16px rgba(108, 92, 231, 0.2);">
                {icon}
            </div>
        </div>
    </div>
    """
    st.markdown(html_code, unsafe_allow_html=True)

def text_card(title, content):
    """
    Renders a text card with a glowing accent border.
    """
    st.markdown(f"""
    <div style="background: white; border-radius: 15px; padding: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.03); border-left: 5px solid #6c5ce7; margin-bottom: 20px;">
        <h3 style="margin: 0 0 10px 0; font-size: 1.1rem; color: #2d3436; display: flex; align-items: center; gap: 8px;">
            <span style="font-size: 1.4rem;">✨</span> {title}
        </h3>
    """, unsafe_allow_html=True)
    st.markdown(content)
    st.markdown("</div>", unsafe_allow_html=True)