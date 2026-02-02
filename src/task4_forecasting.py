"""
Task 4: Forecasting Access and Usage (2025–2027)

This module provides:
- Data preparation
- Trend-based baseline forecasting
- Event-augmented scenario forecasting
- Visualization utilities
- CSV export helpers
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from typing import Dict


# =====================================================
# 1. Data Loading
# =====================================================

def load_datasets(
    enriched_path: str,
    impact_matrix_path: str
):
    """
    Load enriched indicator data and event–indicator impact matrix.
    """
    df = pd.read_csv(enriched_path)
    impact_matrix = pd.read_csv(impact_matrix_path, index_col=0).fillna(0)
    return df, impact_matrix


# =====================================================
# 2. Time Series Preparation
# =====================================================

def prepare_series(
    df: pd.DataFrame,
    indicator_code: str
) -> pd.DataFrame:
    """
    Prepare clean yearly time series for a given indicator.
    """
    series = df[df["indicator_code"] == indicator_code][
        ["fiscal_year", "value_numeric"]
    ].copy()

    series["fiscal_year"] = pd.to_numeric(series["fiscal_year"], errors="coerce")
    series = series.dropna(subset=["fiscal_year", "value_numeric"])
    series = series.sort_values("fiscal_year")

    return series


# =====================================================
# 3. Trend Forecasting
# =====================================================

def fit_trend_model(series: pd.DataFrame) -> LinearRegression:
    """
    Fit linear trend model on sparse annual data.
    """
    X = series["fiscal_year"].values.reshape(-1, 1)
    y = series["value_numeric"].values
    model = LinearRegression()
    model.fit(X, y)
    return model


def forecast_trend(
    model: LinearRegression,
    years: list
) -> pd.Series:
    """
    Generate baseline trend forecast.
    """
    X_future = np.array(years).reshape(-1, 1)
    return pd.Series(model.predict(X_future), index=years)


# =====================================================
# 4. Event-Augmented Forecasting
# =====================================================

def apply_event_impacts_scaled(
    baseline: pd.Series,
    impact_matrix: pd.DataFrame,
    event_weights: Dict[str, float],
    indicator_code: str,
    scale_factor: float = 0.1
) -> pd.Series:
    """
    Apply scaled event impacts to baseline forecast.
    """
    adjustment = pd.Series(0.0, index=baseline.index)

    for event_id, weight in event_weights.items():
        if (
            event_id in impact_matrix.index
            and indicator_code in impact_matrix.columns
        ):
            impact = impact_matrix.loc[event_id, indicator_code]
            adjustment += impact * weight * scale_factor * baseline.max()

    return baseline + adjustment


# =====================================================
# 5. Scenario Generation
# =====================================================

def build_scenarios(
    baseline: pd.Series,
    impact_matrix: pd.DataFrame,
    indicator_code: str,
    scenarios: Dict[str, Dict[str, float]],
    scale_factor: float = 0.1
) -> pd.DataFrame:
    """
    Generate scenario forecasts (base / optimistic / pessimistic).
    """
    df_forecast = pd.DataFrame({
        "year": baseline.index,
        "baseline": baseline.values
    })

    for name, weights in scenarios.items():
        df_forecast[name] = apply_event_impacts_scaled(
            baseline,
            impact_matrix,
            weights,
            indicator_code,
            scale_factor
        ).values

    return df_forecast


# =====================================================
# 6. Visualization
# =====================================================

def plot_forecasts_bar(
    df: pd.DataFrame,
    title: str,
    ylabel: str
):
    """
    Bar chart visualization for scenario forecasts.
    """
    df_plot = df.melt(id_vars="year", var_name="Scenario", value_name="Value")

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x="year",
        y="Value",
        hue="Scenario",
        data=df_plot
    )
    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.grid(axis="y", alpha=0.3)
    plt.legend(title="Scenario")
    plt.tight_layout()
    plt.show()


def plot_forecasts_line(
    df: pd.DataFrame,
    title: str,
    ylabel: str
):
    """
    Line chart visualization for scenario forecasts.
    """
    plt.figure(figsize=(9, 5))

    for col in df.columns[1:]:
        plt.plot(
            df["year"],
            df[col],
            marker="o",
            linewidth=2,
            label=col
        )

    plt.title(title)
    plt.xlabel("Year")
    plt.ylabel(ylabel)
    plt.xticks(df["year"])
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


# =====================================================
# 7. Export Utilities
# =====================================================

def save_forecast(
    df: pd.DataFrame,
    output_path: str
):
    """
    Save forecast table to CSV.
    """
    df.to_csv(output_path, index=False)
