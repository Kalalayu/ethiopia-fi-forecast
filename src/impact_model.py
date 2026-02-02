import pandas as pd
import numpy as np

# Load & Prepare Observation Data
def get_indicator_series(
    df: pd.DataFrame,
    indicator_code: str,
    record_type: str = "observation"
) -> pd.Series:
    """
    Extract a clean time series for a given indicator.
    Returns a pandas Series indexed by year.
    """
    series = (
        df[
            (df["indicator_code"] == indicator_code) &
            (df["record_type"] == record_type)
        ]
        .sort_values("year")
        .set_index("year")["value_numeric"]
    )

    return series

# Define Event Effects
def define_event_effects() -> dict:
    """
    Defines estimated annual effects of major events on indicators.
    Values are percentage-point impacts applied cumulatively.
    """
    return {
        "Telebirr Launch (2021)": {
            "year": 2021,
            "effects": {
                "ACC_MM_ACCOUNT": 1.2,
                "USG_DIGITAL_PAYMENT": 1.0
            }
        },
        "Safaricom Entry (2022)": {
            "year": 2022,
            "effects": {
                "ACC_MM_ACCOUNT": 0.8,
                "USG_DIGITAL_PAYMENT": 0.6
            }
        },
        "M-Pesa Launch (2023)": {
            "year": 2023,
            "effects": {
                "ACC_MM_ACCOUNT": 1.0,
                "USG_DIGITAL_PAYMENT": 1.2
            }
        }
    }
# Apply Event Impacts
def apply_event_impacts(
    baseline: pd.Series,
    events: dict
) -> pd.Series:
    """
    Applies cumulative, additive event impacts to a baseline series.
    """
    modeled = baseline.copy()

    for event in events.values():
        event_year = event["year"]

        for year in modeled.index:
            if year >= event_year:
                for effect in event["effects"].values():
                    modeled.loc[year] += effect

    return modeled
# Build Event–Indicator Association Matrix
def build_event_indicator_matrix(events: dict) -> pd.DataFrame:
    """
    Creates an Event–Indicator association matrix (pp effects).
    """
    matrix = {}

    for event_name, event in events.items():
        matrix[event_name] = event["effects"]

    return pd.DataFrame(matrix).T.fillna(0)
