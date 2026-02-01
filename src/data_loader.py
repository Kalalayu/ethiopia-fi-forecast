import pandas as pd
from pathlib import Path
from typing import Dict

def load_csv(path: str | Path) -> pd.DataFrame:
    """
    Load a CSV file with basic error handling.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"❌ File not found: {path}")
    try:
        df = pd.read_csv(path)
        print(f"Loaded CSV: {path} | Shape: {df.shape}")
        return df
    except pd.errors.ParserError:
        raise ValueError(f"❌ Parsing error while reading CSV: {path}")

def load_excel(path: str | Path, sheet_name: str | None = 0) -> pd.DataFrame | Dict[str, pd.DataFrame]:
    """
    Load an Excel file. 
    sheet_name=None loads all sheets and returns a dict of DataFrames.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"❌ File not found: {path}")
    try:
        df = pd.read_excel(path, sheet_name=sheet_name)
        if sheet_name is None:
            print(f"Loaded Excel with {len(df)} sheets: {path}")
        else:
            print(f"Loaded Excel sheet: {sheet_name} | Shape: {df.shape}")
        return df
    except Exception as e:
        raise ValueError(f"❌ Error reading Excel file: {path}\n{e}")

def load_unified_dataset() -> pd.DataFrame:
    """
    Load the main unified dataset CSV with required column checks.
    """
    path = Path('../data/raw/ethiopia_fi_unified_data.csv')
    df = load_csv(path)
    
    required_cols = ["record_type", "indicator_code", "observation_date"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"❌ Unified dataset missing required columns: {missing}")
    
    return df

def load_reference_codes() -> pd.DataFrame:
    """
    Load the reference codes Excel file.
    """
    path = Path('../data/raw/reference_codes.xlsx')
    return load_excel(path)

def load_additional_data_points_guide() -> Dict[str, pd.DataFrame]:
    """
    Load all sheets from the Additional Data Points Guide Excel file.
    """
    path = Path('../data/raw/Additional Data Points Guide.xlsx')
    return load_excel(path, sheet_name=None)
