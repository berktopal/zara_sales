# Zara Sales — Exploratory Data Analysis

Exploratory data analysis of a retail product dataset (~20,000 Zara products, 17 attributes) using Python. The project covers data cleaning, univariate and multivariate analysis, and a geographic view of product origins.

## Dataset

`data/Zara_sales_EDA.csv` (raw) → `data/Zara_sales_clean.csv` (cleaned), semicolon-separated.

Key columns: `product_position`, `promotion`, `product_category`, `seasonal`, `sales_volume`, `price`, `terms` (product type), `section` (MAN / WOMAN), `season`, `material`, `origin`.

## Analysis Workflow

### 1. Data cleaning — `notebook/data_cleaning.ipynb`
- Load and inspect shape, missing values and duplicates
- Drop incomplete rows
- Normalize column names (`trim → lower case → snake_case`)
- Classify columns into numeric, low-cardinality categorical and high-cardinality categorical (`src/functions.py`)
- Export the cleaned dataset

### 2. Exploratory analysis — `notebook/visualization.ipynb`
- Summary statistics and data types
- Distributions of numeric features (histograms with KDE)
- Frequency of categorical features (count plots)
- Product types by section and by season
- Average numeric metrics per section
- Total sales volume by season
- Material usage by country of origin; top 10 materials
- World choropleth of average metrics by country of origin (GeoPandas + Natural Earth)

## Project Structure

```
zara_sales/
├── data/        # raw and cleaned CSV files
├── notebook/    # data_cleaning.ipynb, visualization.ipynb
└── src/
    └── functions.py   # reusable helpers: column classification, subplot grid
```

## Tech Stack

Python · pandas · NumPy · Matplotlib · Seaborn · GeoPandas · Jupyter

## Getting Started

```bash
pip install -r requirements.txt
jupyter notebook notebook/
```

Run `data_cleaning.ipynb` first, then `visualization.ipynb`. The world map cell downloads Natural Earth boundaries, so it needs an internet connection.
