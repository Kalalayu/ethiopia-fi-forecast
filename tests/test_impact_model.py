import pandas as pd
from src.impact_model import (
    get_indicator_series,
    build_event_indicator_matrix,
    define_event_effects
)

def test_define_event_effects():
    events = define_event_effects()
    assert isinstance(events, dict)
    assert len(events) > 0

def test_event_indicator_matrix():
    events = define_event_effects()
    matrix = build_event_indicator_matrix(events)
    assert not matrix.empty

def test_get_indicator_series():
    df = pd.DataFrame({
        "indicator_code": ["ACC_OWNERSHIP", "ACC_OWNERSHIP"],
        "record_type": ["observation", "observation"],
        "year": [2020, 2021],
        "value_numeric": [40, 45]
    })

    series = get_indicator_series(df, "ACC_OWNERSHIP")
    assert len(series) == 2
