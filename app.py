from pathlib import Path

import streamlit as st
from PIL import Image


# --- Path Settings ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "amir_resume.pdf"
profile_pic = current_dir / "assets" / "prof_pic.jpeg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Amir Hassan Shariatmadari"
PAGE_ICON = ":wave:"
NAME = "Amir Hassan Shariatmadari"
DESCRIPTION = """
Machine Learning and Software Engineer at IBSS Corp. 
"""
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

st.title('Hello there!')


