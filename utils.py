from pathlib import Path
import streamlit as st
from PIL import Image

def get_paths():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    return {
        "css": current_dir / "styles" / "main.css",
        "resume": current_dir / "assets" / "amir_resume.pdf",
        "profile_pic": current_dir / "assets" / "prof_pic.jpeg",
    }

# --- Load utility functions --- 

def load_pdf(path):
    with open(path, "rb") as f:
        return f.read()

def load_css(path):
    with open(path) as f:
        return f.read()

def load_image(path):
    return Image.open(path)

# --- Main content utility functions ---

def write_streamlit_section(section_name, content):
    """
    Utility function to write Streamlit section content.
    Detects if content is raw text or a markdown file path.
    """
    st.write('\n')
    st.subheader(section_name)

    # If it's a Path object or string ending in .md that exists
    if isinstance(content, (str, Path)) and str(content).endswith(".md") and Path(content).exists():
        markdown_text = Path(content).read_text(encoding='utf-8')
        st.markdown(markdown_text, unsafe_allow_html=True)
    else:
        st.write(content)
    
