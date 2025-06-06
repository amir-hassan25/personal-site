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



st.set_page_config(
    page_title=PAGE_TITLE, 
    page_icon=PAGE_ICON
    )

# --- LOAD CSS, RESUME PDF & PROFIL PIC ---
paths = get_paths()

# Load css, enable scrolling, and style streamlit markdwon 
css = load_css(paths['css'])

# Use HTML and Javascript to enable scrolling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Readex+Pro:wght@300;400;500;600;700&display=swap');

.navbar {
    display: flex;
    justify-content: space-around;
    background-color: transparent;
    padding: 10px 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    font-family: 'Readex Pro', sans-serif;
}

.navbar a {
    text-decoration: none;
    font-weight: 600;
    padding: 8px 12px;
    border-radius: 5px;
    transition: background-color 0.2s ease-in-out;
}

/* Light mode styles */
@media (prefers-color-scheme: light) {
    .navbar a {
        color: black !important;
    }

    .navbar a:hover {
        background-color: #e0e0e0;
        color: #d33682 !important;
    }
}

/* Dark mode styles */
@media (prefers-color-scheme: dark) {
    .navbar a {
        color: white !important;
    }

    .navbar a:hover {
        background-color: #444444;
        color: #d33682 !important;
    }
}
</style>

<div class="navbar">
    <a href="#about">👋 About</a>
    <a href="#education">🎓 Education</a>
    <a href="#experience">💼 Experience</a>
    <a href="#publications">📚 Publications</a>
    <a href="#skills">🛠️ Skills</a>
</div>
""", unsafe_allow_html=True)
st.markdown("<style>{}</style>".format(css), unsafe_allow_html=True)

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


# --- SOCIAL LINKS ---
SOCIAL_MEDIA = content.get("SOCIAL_MEDIA", {})
st.sidebar.markdown("### Exeternal Links")
for platform, link in SOCIAL_MEDIA.items():
    st.sidebar.markdown(f"- [{platform}]({link})")

main_content = content.get("MAIN_CONTENT", {})


write_streamlit_section("👋 About Me", main_content.get("ABOUT_ME", ""), anchor_id="about")
write_streamlit_section("🎓 Education", main_content.get("EDUCATION", ""), anchor_id="education")
write_streamlit_section("💼 Experience", main_content.get("EXPERIENCE", ""), anchor_id="experience")
write_streamlit_section("📚 Publications", main_content.get("PUBLICATIONS", ""), anchor_id="publications")
write_streamlit_section("🛠️ Skills", main_content.get("SKILLS", ""), anchor_id="skills")





