import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    layout="wide"
)

st.title("🇪🇹 Ethiopia Financial Inclusion Dashboard")
st.markdown(
    """
    This dashboard explores financial inclusion trends,  
    event impacts, and forecasts (2025–2027) for Ethiopia.
    """
)

# ======================================================
# LOAD DATA
# ======================================================
@st.cache_data
def load_data():
    df = pd.read_csv("../data/processed/ethiopia_fi_unified_data_enriched.csv")
    forecast_acc = pd.read_csv("../data/processed/forecast_account_ownership_2025_2027.csv")
    forecast_mm = pd.read_csv("../data/processed/forecast_digital_payments_2025_2027.csv")
    return df, forecast_acc, forecast_mm


df, forecast_acc, forecast_mm = load_data()

# ======================================================
# CLEAN FISCAL YEAR (ROBUST)
# ======================================================
df["fiscal_year_clean"] = (
    df["fiscal_year"]
    .astype(str)
    .str.extract(r"(\d{4})")
)

df["fiscal_year_clean"] = pd.to_numeric(
    df["fiscal_year_clean"], errors="coerce"
)

# ======================================================
# SIDEBAR NAVIGATION
# ======================================================
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Trends", "Forecasts", "Inclusion Projections"]
)

# ======================================================
# OVERVIEW PAGE (FIXED)
# ======================================================
if page == "Overview":
    st.header("📌 Overview")

    def latest_indicator_value(indicator_code):
        subset = (
            df[
                (df["indicator_code"] == indicator_code) &
                (df["record_type"] == "observation")
            ]
            .dropna(subset=["value_numeric", "fiscal_year_clean"])
            .sort_values("fiscal_year_clean")
        )

        if subset.empty:
            return np.nan, np.nan

        row = subset.iloc[-1]
        return row["value_numeric"], int(row["fiscal_year_clean"])

    acc_value, acc_year = latest_indicator_value("ACC_OWNERSHIP")
    mm_value, mm_year = latest_indicator_value("ACC_MM_ACCOUNT")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Account Ownership (%)",
        f"{acc_value:.1f}",
        help=f"Latest observed value ({acc_year})"
    )

    col2.metric(
        "Digital Payment Usage (%)",
        f"{mm_value:.1f}",
        help=f"Latest observed value ({mm_year})"
    )

    col3.metric(
        "Latest Observation Year",
        max(acc_year, mm_year)
    )

    st.markdown(
        """
        **Insight:**  
        Financial inclusion in Ethiopia is advancing steadily, driven by mobile
        money expansion and telecom competition. However, access growth continues
        to lag behind usage, highlighting the importance of policy and
        infrastructure interventions.
        """
    )

# ======================================================
# TRENDS PAGE
# ======================================================
elif page == "Trends":
    st.header("📈 Historical Trends")

    indicator_map = {
        "Account Ownership (%)": "ACC_OWNERSHIP",
        "Digital Payment Usage (%)": "ACC_MM_ACCOUNT"
    }

    selected = st.selectbox("Select Indicator", list(indicator_map.keys()))
    code = indicator_map[selected]

    trend_df = (
        df[
            (df["indicator_code"] == code) &
            (df["record_type"] == "observation")
        ]
        .dropna(subset=["value_numeric", "fiscal_year_clean"])
        .sort_values("fiscal_year_clean")
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        trend_df["fiscal_year_clean"],
        trend_df["value_numeric"],
        marker="o"
    )
    ax.set_title(selected)
    ax.set_xlabel("Year")
    ax.set_ylabel("Percent of Adults")
    ax.grid(True)

    st.pyplot(fig)

# ======================================================
# FORECASTS PAGE
# ======================================================
elif page == "Forecasts":
    st.header("🔮 Forecasts (2025–2027)")

    scenario = st.selectbox(
        "Select Scenario",
        ["baseline", "base", "optimistic", "pessimistic"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Account Ownership Forecast")
        fig, ax = plt.subplots()
        ax.plot(
            forecast_acc["year"],
            forecast_acc[scenario],
            marker="o"
        )
        ax.set_xlabel("Year")
        ax.set_ylabel("Percent of Adults")
        ax.grid(True)
        st.pyplot(fig)

    with col2:
        st.subheader("Digital Payment Usage Forecast")
        fig, ax = plt.subplots()
        ax.plot(
            forecast_mm["year"],
            forecast_mm[scenario],
            marker="o"
        )
        ax.set_xlabel("Year")
        ax.set_ylabel("Percent of Adults")
        ax.grid(True)
        st.pyplot(fig)

# ======================================================
# INCLUSION PROJECTIONS PAGE
# ======================================================
elif page == "Inclusion Projections":
    st.header("🎯 Inclusion Projections vs Target")

    target = 60
    scenario = st.selectbox(
        "Scenario",
        ["baseline", "base", "optimistic", "pessimistic"]
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        forecast_acc["year"],
        forecast_acc[scenario],
        marker="o",
        label="Projected Account Ownership"
    )

    ax.axhline(
        target,
        color="red",
        linestyle="--",
        label="60% Target"
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Percent of Adults")
    ax.set_title("Progress Toward Financial Inclusion Target")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    st.markdown(
        """
        **Interpretation:**  
        Under optimistic scenarios, Ethiopia approaches the 60% inclusion target
        by 2027. Achieving this outcome depends on sustained infrastructure
        investment, digital ID rollout, and inclusive regulatory reforms.
        """
    )
