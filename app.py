import streamlit as st
from utils import get_paths, load_pdf, load_css, load_image


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Amir Hassan Shariatmadari"
PAGE_ICON = ":wave:"
NAME = "Amir Hassan Shariatmadari"
DESCRIPTION = """Machine Learning and Software Engineer at IBSS Corp."""

EMAIL = "amirhassanshariatmadari@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com"
    }

PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}

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

