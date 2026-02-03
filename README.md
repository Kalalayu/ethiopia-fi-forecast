# Ethiopia Financial Inclusion Analytics Platform  
**Tasks 1–5 | Data Engineering, Analysis, Forecasting & Visualization**

## 📌 Project Summary

This project examines the evolution of financial inclusion in Ethiopia, with a particular focus on **account ownership** and **digital payment adoption**. By combining historical data, event-driven insights, and forward-looking forecasts, the project delivers an analytics dashboard designed to support policymakers, financial institutions, and development partners to:

- Analyze long-term inclusion trends  
- Assess the influence of policy, telecom, and market events  
- Compare alternative future scenarios  
- Monitor progress toward the **60% financial inclusion benchmark**

The work is organized into **five sequential tasks**, progressing from data preparation to interactive dashboard delivery.

---

## ✅ Task 1: Data Collection & Harmonization

### Objective  
Compile and prepare diverse financial inclusion datasets into a single, analysis-ready resource.

### Key Steps  
- Collected raw datasets covering:
  - Account ownership  
  - Digital payments and mobile money usage  
- Standardized variable names, data types, and formats  
- Normalized fiscal year representations (e.g., FY2022/23 → 2022)  
- Converted indicators into consistent numeric measures  
- Exported the unified dataset to:  
  `data/processed/ethiopia_fi_unified_data.csv`

### Output  
✔ A clean, structured dataset suitable for downstream analysis and modeling

---

## 📊 Task 2: Exploratory Analysis & Event Assessment

### Objective  
Understand historical patterns and identify how major events have shaped financial inclusion outcomes.

### Key Activities  
- Time-series analysis of:
  - Account ownership rates  
  - Digital payment usage  
- Annotation of significant events (policy reforms, telecom competition, mobile money expansion)  
- Correlation analysis between key indicators  
- Visual detection of structural breaks and growth accelerations  

### Key Insight  
Digital payment usage has expanded more rapidly than account ownership, suggesting that **usage intensity is increasing faster than access coverage**.

---

## 🔮 Task 3: Forecasting & Scenario Modeling

### Objective  
Project future financial inclusion trends under alternative assumptions.

### Methodology  
- Trend-based baseline forecasting  
- Scenario-based adjustments:
  - Optimistic  
  - Base  
  - Pessimistic  

### Forecast Window  
**2025–2027**

### Outputs  
- Account ownership forecasts  
- Digital payment usage forecasts  
- Scenario-specific results saved as:
  - `data/processed/forecast_account_ownership.csv`  
  - `data/processed/forecast_digital_payments.csv`

### Key Insight  
Under favorable conditions, Ethiopia moves close to the **60% inclusion target by 2027**.

---

## 📈 Task 4: Indicator Engineering & Analytical Metrics

### Objective  
Develop derived indicators to strengthen analytical and policy insights.

### Indicators Produced  
- Growth rate metrics  
- Channel usage comparisons (e.g., P2P vs ATM)  
- Access–usage crossover measures  
- Latest observed values versus projected outcomes  

### Outcome  
✔ Metrics designed for seamless dashboard integration  
✔ Consistent and validated indicators across all tasks  

---

## 🖥 Task 5: Interactive Dashboard Development

### Objective  
Deliver an interactive analytics dashboard using **Streamlit**.

### Dashboard Components  

#### 📌 Overview  
- Key summary metrics  
- Latest account ownership and digital payment indicators  
- High-level insights  

#### 📈 Trends  
- Interactive time-series visualizations  
- Indicator selection and historical comparisons  

#### 🔮 Forecasts  
- Scenario selectors  
- Forecast visualizations for 2025–2027  
- Comparative views for access and usage  

#### 🎯 Inclusion Targets  
- Progress tracking toward the 60% benchmark  
- Scenario-based comparisons  
- Policy-relevant interpretations  

### Key Features  
- ✅ At least four interactive visualizations  
- ✅ Clear labels and narrative explanations  
- ✅ Scenario selection controls  
- ✅ Clean, reproducible codebase  

---
## Continuous Integration (CI)

This project uses GitHub Actions to automatically validate code quality.
On every push or pull request, the CI pipeline:

- Installs project dependencies
- Runs unit tests for the impact modeling module
- Ensures core analytical functions execute correctly

This helps maintain reproducibility and prevents regressions as the project evolves.

---

## 🎯 Key Questions Addressed

- ✔ How quickly is financial inclusion expanding?  
- ✔ Which channels drive usage compared to access?  
- ✔ What role do policy and telecom events play?  
- ✔ Is Ethiopia on track to reach 60% inclusion by 2027?  
- ✔ Which scenarios accelerate or delay progress?  

---

## 📌 Conclusion

This project delivers a **data-driven, forward-looking, and policy-relevant analytics framework** for tracking and forecasting financial inclusion in Ethiopia. By integrating clean data, event analysis, scenario modeling, and interactive visualization, it supports **evidence-based decision-making** for regulators, financial service providers, and development partners.