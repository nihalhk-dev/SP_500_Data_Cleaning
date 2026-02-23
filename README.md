# S&P 500 Data Cleaning & Quantitative Analysis Pipeline

## 1. Project Overview

This project develops a fully reproducible data pipeline for cleaning, validating, engineering, and analyzing historical data from the **S&P 500**.

The primary objective is to transform a deliberately corrupted dataset into a statistically reliable and financially interpretable time-series dataset suitable for quantitative modeling.

To rigorously evaluate the robustness of the cleaning system, controlled data corruption is introduced during the Exploratory Data Analysis (EDA) stage. The pipeline is then designed to detect and correct these issues in a modular and reproducible manner.

The project demonstrates:

- Robust data cleaning techniques
- Modular pipeline architecture
- Financial feature engineering
- Statistical validation of time-series properties
- Risk and performance analysis using industry-standard metrics

---

## 2. Dataset Description

**Asset:** S&P 500
**Source:** Historical price data downloaded from Investing.com
**Observations:** 5,001 daily records

The project uses two dataset versions:

### 1. Original Dataset (`sp500_raw.csv`)

Clean historical data downloaded from Investing.com, stored in:

```
data/raw/sp500_raw.csv
```

Columns include:

- Date
- Price
- Open
- High
- Low
- Vol.
- Change %

### 2. Simulated Dirty Dataset (`sp500_dirty.csv`)

During EDA, the original dataset is intentionally corrupted to simulate real-world data integrity problems. The corrupted version is exported to:

```
data/raw/sp500_dirty.csv
```

Introduced issues include:

- Duplicate rows
- Missing values
- Artificial extreme values
- Shuffled chronological order
- Column name inconsistencies

This controlled corruption enables systematic validation of the cleaning pipeline.

---

## 3. Research Objectives

The analysis addresses the following quantitative questions:

1. Are price levels stationary?
2. Are returns stationary?
3. Do returns follow a normal distribution?
4. What is the historical volatility and downside risk?
5. How stable is risk-adjusted performance over time?
6. What relationships exist between engineered features?

---

## 4. Simulated Data Quality Issues & Resolution

To evaluate robustness, the original dataset was intentionally corrupted during the EDA stage.

The dirty dataset contained:

| Issue                      | Description                                | Resolution                                 |
| -------------------------- | ------------------------------------------ | ------------------------------------------ |
| Inconsistent column names  | Extra trailing spaces introduced           | Standardized and stripped whitespace       |
| Missing price observations | 30 NaNs injected randomly                  | Forward-filled where appropriate           |
| Duplicate records          | 20 duplicated rows added                   | Removed                                    |
| Artificial extreme values  | High column multiplied by 5 in random rows | Corrected using threshold-based validation |
| Shuffled rows              | Chronological order disrupted              | Sorted by date                             |

All corrections are implemented through modular functions in the `src/` directory to ensure traceability and reproducibility.

---

## 5. Pipeline Architecture

The project follows a structured workflow:

**Raw Data → EDA → Controlled Corruption → Cleaning → Feature Engineering → Validation → Analysis → Export**

### Cleaning Stage

- Datetime parsing and chronological ordering
- Numeric coercion and validation
- Duplicate removal
- Missing value handling
- Outlier correction
- OHLC logical consistency enforcement

### Feature Engineering

- Daily returns
- Moving averages (20-day and 50-day)
- Rolling volatility (20-day standard deviation)
- Cumulative return
- Maximum drawdown
- Annualized volatility
- Sharpe ratio
- Rolling Sharpe ratio

### Validation

- Structural integrity checks
- Chronological ordering verification
- Missing value diagnostics
- Assertion-based safeguards

---

## 6. Statistical Findings

### Price Behavior

- Augmented Dickey-Fuller test indicates non-stationarity (p ≈ 0.50).
- The price series exhibits long-term upward drift and cyclical corrections.

### Return Properties

- Returns are stationary (ADF p ≈ 0.000).
- Mean daily return ≈ 0.000286
- Daily volatility ≈ 1.17%
- Maximum daily return ≈ 11.6%
- Minimum daily return ≈ −9.0%
- Excess kurtosis ≈ 9.42 (fat-tailed distribution)

The Jarque-Bera test strongly rejects normality (p ≈ 0), confirming the presence of fat tails — a well-documented empirical characteristic of financial time series.

---

## 7. Risk & Performance Metrics

The analysis includes several industry-standard measures:

- **Maximum Drawdown** — worst historical peak-to-trough decline
- **Annualized Volatility** — scaled using √252 trading days
- **Sharpe Ratio** — risk-adjusted return (risk-free rate assumed zero)
- **Rolling Sharpe Ratio** — time-varying performance regimes

Results align with established empirical properties of equity markets, including volatility clustering and non-normal return distributions.

---

## 8. Feature Relationships

A correlation matrix was computed for:

- Return
- MA_20
- MA_50
- Volatility_20

Findings:

- Strong correlation between moving averages (expected due to overlapping windows)
- Low correlation between volatility and returns
- No structural anomalies detected

---

## 9. Project Structure

```
project/
├── main.py
├── data/
│   ├── raw/
│   │   ├── sp500_raw.csv
│   │   └── sp500_dirty.csv
│   └── processed/
│       └── sp500_clean.csv
├── notebooks/
│   ├── eda.ipynb
│   └── Processed_Analysis.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
└── requirements.txt
```

### Design Principles

- Separation of concerns
- Reproducibility
- Modularity
- Clear validation checkpoints
- Controlled experimental design

---

## 10. Reproducibility

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run the EDA Notebook (Required First Step)

Open:

```
notebooks/eda.ipynb
```

Execute all cells sequentially.

This notebook:

- Explores the original dataset
- Introduces controlled corruption
- Exports the dirty dataset to:

```
data/raw/sp500_dirty.csv
```

⚠️ This step must be completed before running the pipeline.

---

### 3. Run the Cleaning & Feature Engineering Pipeline

```bash
python main.py
```

This script:

- Cleans `sp500_dirty.csv`
- Engineers financial features
- Exports the processed dataset to:

```
data/processed/sp500_clean.csv
```

---

### 4. Run the Processed Data Analysis

Open:

```
notebooks/Processed_Analysis.ipynb
```

Execute all cells sequentially to reproduce the statistical validation and quantitative analysis results.

---

## 11. Conclusion

The dataset was successfully cleaned, validated, and analyzed.

Empirical findings confirm well-established financial time-series characteristics:

- Prices are non-stationary
- Returns are stationary
- Returns are not normally distributed
- Fat tails and volatility clustering are present

All engineered features behave as theoretically expected, and the dataset is suitable for further quantitative modeling applications, including forecasting, portfolio optimization, and risk modeling.
