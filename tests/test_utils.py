import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from PIL import Image
from unittest.mock import patch, mock_open
from utils import get_paths, load_pdf, load_css, load_image, write_streamlit_section


def test_get_paths():
    """
    Test that `get_paths()` returns a dictionary with keys
    for CSS, resume, and profile picture file paths.
    
    This test does not check for file existence—only that the
    keys are correctly present.
    """
    paths = get_paths()
    assert "css" in paths
    assert "resume" in paths
    assert "profile_pic" in paths


# --- Test load functions ---

def test_load_pdf():
    """
    Test that `load_pdf()` reads binary PDF data correctly.

    Mocks the `open()` function to return fake PDF bytes,
    then verifies:
    - The returned data matches the expected fake content.
    - The file is opened once in binary mode.
    """
    fake_data = b"FAKE PDF CONTENT"
    with patch("builtins.open", mock_open(read_data=fake_data)) as mock_file:
        data = load_pdf("some/path/resume.pdf")
        assert data == fake_data
        mock_file.assert_called_once_with("some/path/resume.pdf", "rb")


def test_load_css():
    """
    Test that `load_css()` reads and returns the content of a CSS file.

    Mocks `open()` to return a simple CSS string,
    then checks:
    - The string contains expected CSS content.
    - The file is opened once in text mode.
    """
    css_data = "body { background: white; }"
    with patch("builtins.open", mock_open(read_data=css_data)) as mock_file:
        css = load_css("some/path/main.css")
        assert "background" in css
        mock_file.assert_called_once_with("some/path/main.css")


def test_load_image():
    """
    Test that `load_image()` opens and returns an image correctly.

    Mocks `PIL.Image.open()` to return a dummy image,
    then verifies:
    - The returned image has the correct size.
    - Image.open is called with the expected path.
    """
    dummy_image = Image.new("RGB", (50, 50))
    with patch("PIL.Image.open", return_value=dummy_image) as mock_img_open:
        img = load_image("some/path/image.jpg")
        assert img.size == (50, 50)
        mock_img_open.assert_called_once_with("some/path/image.jpg")


# --- Test write content functions ---

def test_write_streamlit_section():
    """
    Test that `write_streamlit_section()` writes a section with a subheader.

    Mocks `st.write()` and `st.subheader()` to verify:
    - The section name is correctly formatted.
    - The content is written as markdown.
    """
    with patch("streamlit.write") as mock_write, patch("streamlit.subheader") as mock_subheader:
        section_name = "Test Section"
        content = "This is some test content."
        write_streamlit_section(section_name, content)
        
        mock_subheader.assert_called_once_with(section_name)
        mock_write.assert_called_with(content)