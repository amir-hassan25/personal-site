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

# Load css and style streamlit markdwon 
css = load_css(paths['css'])
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
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


main_content = content.get("MAIN_CONTENT", {})

# --- ABOUT ME SECTION ---
about_me = main_content.get("ABOUT_ME", "")
write_streamlit_section(
    "👋 About Me",
    about_me
)

# --- EDUCATION SECTION ---

education = main_content.get("EDUCATION", "")
write_streamlit_section(
    "🎓 Education",
    education
)

# --- EXPERIENCE SECTION --- 
experience = main_content.get("EXPERIENCE", "")
write_streamlit_section(
    "💼 Experience",
    experience
)

# --- PUBLICATIONS SECTION ---
publications = main_content.get("PUBLICATIONS", "")
write_streamlit_section(
    "📚 Publications",
    publications
)

# --- SKILLS SECTION ---
skills = main_content.get("SKILLS", "")
write_streamlit_section(
    "🛠️ Skills",
    skills
)

