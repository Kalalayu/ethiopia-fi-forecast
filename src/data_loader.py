import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Load a CSV file with basic error handling.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ File not found: {path}")
    except pd.errors.ParserError:
        raise ValueError(f"❌ Parsing error while reading: {path}")

def load_enriched_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path)

    required_cols = ["record_type", "indicator_code", "observation_date"]
    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
