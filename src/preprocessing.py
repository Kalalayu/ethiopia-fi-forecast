import pandas as pd


def prepare_observations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter observations and extract year from observation_date.
    """
    obs = df[df["record_type"] == "observation"].copy()

    obs["year"] = pd.to_datetime(
        obs["observation_date"], errors="coerce"
    ).dt.year

    obs = obs.dropna(subset=["year", "value_numeric"])
    return obs


def filter_indicator(obs: pd.DataFrame, indicator_code: str) -> pd.DataFrame:
    """
    Filter observation dataframe by indicator_code.
    """
    subset = obs[obs["indicator_code"] == indicator_code].copy()
    return subset.sort_values("year")


def calculate_growth(df: pd.DataFrame, value_col="value_numeric") -> pd.DataFrame:
    """
    Calculate year-over-year growth in percentage points.
    """
    df = df.copy()
    df["growth_pp"] = df[value_col].diff()
    return df
