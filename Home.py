import json
import streamlit as st
from utils import get_paths, load_pdf, load_css, load_image, write_streamlit_section

# Load settings from a JSON file
with open("assets/content.json", "r") as f:    
    content = json.load(f)


# --- GENERAL SETTINGS ---

general = content.get("GENERAL", {})
PAGE_TITLE = general.get("PAGE_TITLE", "")
PAGE_ICON = general.get("PAGE_ICON", "")
NAME = general.get("NAME", "")
DESCRIPTION = general.get("DESCRIPTION", "")
EMAIL = general.get("EMAIL", "")


def home_page():
    # Load CSS, assets, and render your hero section
    paths = get_paths()
    css = load_css(paths['css'])
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

    # Load PDF file
    resume_pdf = load_pdf(paths['resume'])

    # Load profile picture 
    profile_pic = load_image(paths['profile_pic'])

    # --- HERO SECTION ---
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label=" 📄 Download Resume",
            data=resume_pdf,
            file_name=paths['resume'].name,
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)

    main_content = content.get("MAIN_CONTENT", {})

    write_streamlit_section("👋 About Me", main_content.get("ABOUT_ME", ""), anchor_id="about")
    write_streamlit_section("🎓 Education", main_content.get("EDUCATION", ""), anchor_id="education")
    write_streamlit_section("💼 Experience", main_content.get("EXPERIENCE", ""), anchor_id="experience")
    write_streamlit_section("📚 Publications", main_content.get("PUBLICATIONS", ""), anchor_id="publications")
    write_streamlit_section("🛠️ Skills", main_content.get("SKILLS", ""), anchor_id="skills")


home = st.Page(home_page, title="Home", icon="🏠", default=True)
test_page = st.Page("pages/test_1.py", title="Test Page", icon="🧰")

st.set_page_config(
    page_title="My Portfolio",
    page_icon="🌐",
    initial_sidebar_state="expanded",
)

# Hotfix: Uncomment the next line to enable navigation with multiple pages
# pg = st.navigation([home, test_page], position="sidebar", expanded=True)

pg = st.navigation([home], position="sidebar", expanded=True)

pg.run()
