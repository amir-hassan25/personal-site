import importlib.util
import sys
from pathlib import Path

def test_app_runs_without_crashing():
    """
    Smoke test: Verifies that the Streamlit app runs without syntax or runtime errors.
    """
    script_path = Path(__file__).resolve().parents[1] / "Home.py"
    spec = importlib.util.spec_from_file_location("app", script_path)
    app_module = importlib.util.module_from_spec(spec)
    sys.modules["app"] = app_module

    try:
        spec.loader.exec_module(app_module)
    except Exception as e:
        assert False, f"Streamlit app failed to run: {e}"