import math
import matplotlib.pyplot as plt
import geopandas as gp

def get_columns(df):
    num_columns = df.select_dtypes(include = ["int64", "float64"]).columns.tolist()
    num_columns = [col for col in num_columns if col.lower() != "product_id"]
    cat_columns = df.select_dtypes(include = ["object", "category"]).columns.tolist()
    cat_cardinal_columns = [col for col in cat_columns if df[col].nunique() > 20]
    cat_columns = [col for col in cat_columns if col not in cat_cardinal_columns and col not in ['product_category', 'brand', 'currency']]
    return cat_columns, cat_cardinal_columns, num_columns

def sub_plot(columns):
    n_cols = 5
    n_rows = math.ceil(len(columns) / n_cols)
    fig, axes = plt.subplots(n_rows, n_cols, figsize = (5 * n_cols, 4 * n_rows), constrained_layout = True)
    axes = axes.flatten()
    return fig, axes