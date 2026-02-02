# 📒 Notebooks Documentation  
**Financial Inclusion Analysis – Ethiopia**

This folder contains all Jupyter notebooks for the Ethiopia Financial Inclusion project, covering **data preparation, exploratory analysis, forecasting, and scenario modeling**. Each notebook corresponds to a specific task and builds upon the previous ones for a logical, reproducible workflow.

---

## 📘 `task1_data_preparation.ipynb`  
**Task 1: Data Collection & Cleaning**

**Purpose**  
Prepare raw financial inclusion datasets for analysis and modeling.

**Key Steps**  
- Load raw datasets: account ownership, digital payments  
- Standardize column names and formats  
- Convert fiscal year labels (e.g., FY2022/23 → 2022)  
- Handle missing values and type conversions  
- Merge datasets into a single, unified structure  

**Output**  
- Cleaned dataset saved to: `data/processed/ethiopia_fi_unified_data.csv`  

**Importance**  
Ensures **consistency and reproducibility** for all downstream analysis and forecasting.

---

## 📊 `task2_eda_events.ipynb`  
**Task 2: Exploratory Data Analysis & Event Impact**

**Purpose**  
Analyze historical trends and evaluate how major events affected financial inclusion.

**Key Steps**  
- Time-series visualization of key indicators  
- Event annotation (policy reforms, mobile money expansion, telecom competition)  
- Growth rate analysis  
- Correlation analysis between indicators  

**Insights**  
- Digital payment adoption grows faster than account ownership  
- Policy and telecom events often align with periods of accelerated growth  

**Outputs**  
- Analytical plots  
- Summary statistics  
- Event–indicator relationship tables  

---

## 🔮 `task3_forecasting.ipynb`  
**Task 3: Baseline Forecasting**

**Purpose**  
Generate forecasts for financial inclusion indicators using historical trends.

**Key Steps**  
- Define forecasting targets:
  - Account ownership (%)  
  - Digital payment usage (%)  
- Apply trend-based regression models  
- Produce baseline forecasts for **2025–2027**  
- Evaluate model assumptions and limitations  

**Outputs**  
- Forecast tables  
- Baseline projection plots  
- Saved forecast results for dashboard integration  

---

## 📈 `task4_forecasting_scenarios.ipynb`  
**Task 4: Scenario & Uncertainty Analysis**

**Purpose**  
Extend baseline forecasts by incorporating scenario adjustments and uncertainty ranges.

**Key Steps**  
- Define scenarios:
  - Optimistic  
  - Base  
  - Pessimistic  
- Apply event-driven impact multipliers  
- Generate scenario ranges and confidence intervals  
- Compare trajectories across scenarios  

**Outputs**  
- Scenario forecast tables  
- Visualizations showing uncertainty bands  
- Written interpretation of assumptions and risks  

---

## ⚡ Recommended Workflow

**Run notebooks sequentially:**  
`task1 → task2 → task3 → task4`  

### Notes & Assumptions
- Data availability is limited (sparse Findex points)  
- Forecasts are trend-based, not causal  
- Scenario analysis reflects assumptions, not precise predictions  
- Results are intended for **strategic insight**, not exact estimations  

### Best Practices
- ✅ Always start with Task 1  
- ✅ Do not skip intermediate tasks  
- ✅ Outputs from forecasting notebooks feed directly into the dashboard  

---

## 📌 Summary

These notebooks form the **analytical backbone** of the project, transforming raw data into actionable insights and forecasts. The workflow ensures clarity, reproducibility, and seamless integration with the interactive dashboard.
# Notebooks

This directory contains Jupyter notebooks used to support analysis for the **Forecasting Financial Inclusion in Ethiopia** project.  
The notebooks follow the project tasks and are designed to be run sequentially.

## Contents

- **01_data_exploration_enrichment.ipynb**  
  Explores the unified financial inclusion dataset, validates the shared schema, reviews record types (observations, events, targets), assesses data quality, and documents any data enrichment activities.  
  *Corresponds to Task 1: Data Exploration and Enrichment.*

- **02_exploratory_data_analysis.ipynb**  
  Conducts exploratory data analysis of financial inclusion indicators, focusing on Access (account ownership) and Usage (digital payments).  
  Includes trend analysis, event timeline visualization, correlation analysis, and documentation of key insights and data limitations.  
  *Corresponds to Task 2: Exploratory Data Analysis.*

