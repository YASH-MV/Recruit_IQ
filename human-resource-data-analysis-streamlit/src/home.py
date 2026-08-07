"""Home page with navigation to Interview Session and HR Analytics"""

import streamlit as st
import base64
from pathlib import Path


def _img_to_base64(path: str) -> str:
    """Read an image file and return a base64 data URI, or empty string if missing."""
    p = Path(path)
    if not p.exists():
        return ""
    ext = p.suffix.lstrip(".")
    data = base64.b64encode(p.read_bytes()).decode()
    return f"data:image/{ext};base64,{data}"


def render_home():
    """Render home page with logo, banner, and two large navigation cards"""

    banner_uri = _img_to_base64("assets/hr-banner.png")
    logo_uri = _img_to_base64("assets/logo.png")

    st.markdown("""
    <style>
        .top-banner {
            width: 100%;
            max-height: 220px;
            object-fit: cover;
            border-radius: 14px;
            margin-bottom: 28px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25);
        }

        .home-header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            margin-bottom: 8px;
        }

        .home-header img {
            width: 64px;
            height: 64px;
            border-radius: 50%;
            object-fit: cover;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
        }

        .home-header h1 {
            font-size: 42px;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .home-subtitle {
            text-align: center;
            font-size: 17px;
            color: #999;
            margin-bottom: 36px;
        }

        .nav-card {
            height: 100%;
            padding: 36px 32px;
            border-radius: 15px;
            border: 2px solid transparent;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
            background: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            text-align: center;
            min-height: 380px;
        }

        .nav-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
        }

        .nav-card.interview { border-top: 5px solid #667eea; }
        .nav-card.analytics { border-top: 5px solid #4ECDC4; }

        .card-icon { font-size: 60px; margin-bottom: 16px; }

        .card-title {
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 12px;
            color: #333;
        }
        .nav-card.interview .card-title { color: #667eea; }
        .nav-card.analytics .card-title { color: #4ECDC4; }

        .card-description {
            font-size: 15px;
            color: #666;
            line-height: 1.55;
            margin-bottom: 18px;
            min-height: 70px;
        }

        .card-features {
            list-style: none;
            padding: 0;
            margin: 0;
            font-size: 13.5px;
            color: #888;
            width: 100%;
            border-top: 1px solid #eee;
            padding-top: 14px;
        }
        .card-features li { margin: 6px 0; }

        /* Style the real Streamlit buttons under each card to match the theme */
        div[data-testid="column"]:nth-of-type(1) button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
            color: white !important;
            border: none !important;
            font-weight: 600 !important;
        }
        div[data-testid="column"]:nth-of-type(2) button {
            background: linear-gradient(135deg, #4ECDC4 0%, #44A99E 100%) !important;
            color: white !important;
            border: none !important;
            font-weight: 600 !important;
        }
        div[data-testid="stButton"] button {
            border-radius: 8px !important;
            padding: 10px 0 !important;
            transition: all 0.25s ease !important;
        }
        div[data-testid="stButton"] button:hover {
            transform: scale(1.03);
            box-shadow: 0 6px 18px rgba(0,0,0,0.25);
        }
    </style>
    """, unsafe_allow_html=True)

    # Banner image (only rendered if the file exists)
    if banner_uri:
        st.markdown(f'<img src="{banner_uri}" class="top-banner" />', unsafe_allow_html=True)

    # Header with logo + title
    logo_html = f'<img src="{logo_uri}" />' if logo_uri else ""
    st.markdown(f"""
    <div class="home-header">
        {logo_html}
        <h1>HR Management System</h1>
    </div>
    <p class="home-subtitle">Select a module to get started</p>
    """, unsafe_allow_html=True)

    # Two navigation cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="nav-card interview">
            <div class="card-icon">👨‍💼</div>
            <div class="card-title">Interview Session</div>
            <div class="card-description">
                Conduct and manage employee interviews with AI-powered insights and recommendations.
            </div>
            <ul class="card-features">
                <li>✓ Real-time interview guidance</li>
                <li>✓ AI-powered insights</li>
                <li>✓ Performance scoring</li>
                <li>✓ Candidate assessment</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button(
            "📋 Go to Interview Session",
            key="btn_interview",
            use_container_width=True,
            help="Navigate to Interview Session module"
        ):
            st.session_state['page'] = 'interview'
            st.rerun()

    with col2:
        st.markdown("""
        <div class="nav-card analytics">
            <div class="card-icon">📊</div>
            <div class="card-title">HR Analytics</div>
            <div class="card-description">
                Comprehensive HR analytics with detailed insights into employee data, trends, and attrition prediction.
            </div>
            <ul class="card-features">
                <li>✓ Executive summary</li>
                <li>✓ Capacity analysis</li>
                <li>✓ Attrition insights</li>
                <li>✓ ML predictions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        if st.button(
            "📈 Go to HR Analytics",
            key="btn_analytics",
            use_container_width=True,
            help="Navigate to HR Analytics module"
        ):
            st.session_state['page'] = 'analytics'
            st.rerun()

    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #999; font-size: 13px; padding: 10px;">
        <p>HR Management System v1.0 | Choose a module to begin</p>
    </div>
    """, unsafe_allow_html=True)