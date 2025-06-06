import streamlit as st
from utils import get_paths, load_pdf, load_css, load_image, write_streamlit_section


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Amir Hassan Shariatmadari"
PAGE_ICON = ":wave:"
NAME = "Amir Hassan Shariatmadari"
DESCRIPTION = """Machine Learning and Software Engineer at IBSS Corp."""

EMAIL = "amirhassanshariatmadari@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com", 
    "Google Scholar": "https://scholar.google.com",
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


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EDUCATION SECTION ---
write_streamlit_section(
    "🎓 Education",
    """
    - **Bachelor of Science in Computer Science** at University of Technology (2017 - 2021)
        - Focused on software engineering and machine learning.
        - Graduated with honors.
    - **Master of Science in Artificial Intelligence** at Institute of Advanced Studies (2021 - 2023)
        - Specialized in deep learning and natural language processing.
        - Conducted research on AI ethics and bias.
    """
)

# --- EXPERIENCE SECTION --- 
write_streamlit_section(
    "💼 Experience",
    """
    - **Machine Learning Engineer** at IBSS Corp. (2023 - Present)
        - Developed and deployed machine learning models for various applications.
        - Collaborated with cross-functional teams to integrate AI solutions.
    - **Software Engineer** at Tech Solutions (2021 - 2023)
        - Designed and implemented software solutions for client projects.
        - Improved system performance and user experience through optimization.
    """
)

# Publications section
write_streamlit_section(
    "📚 Publications",
    """
    - **"Advanced Machine Learning Techniques"** - Published in AI Journal, 2022.
    - **"Software Development Best Practices"** - Featured in Tech Magazine, 2021.
    """
)

