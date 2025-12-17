import pandas as pd
import os

def read_file(uploaded_file) -> pd.DataFrame:
    """
    Read CSV or Excel file uploaded via Streamlit or file path.
    """
    # Streamlit UploadedFile
    if hasattr(uploaded_file, "name"):
        ext = os.path.splitext(uploaded_file.name)[1].lower()
        if ext == ".csv":
            return pd.read_csv(uploaded_file)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(uploaded_file)
        else:
            raise ValueError("Unsupported file format")

    # File path (local)
    else:
        ext = os.path.splitext(uploaded_file)[1].lower()
        if ext == ".csv":
            return pd.read_csv(uploaded_file)
        elif ext in [".xlsx", ".xls"]:
            return pd.read_excel(uploaded_file)
        else:
            raise ValueError("Unsupported file format")
