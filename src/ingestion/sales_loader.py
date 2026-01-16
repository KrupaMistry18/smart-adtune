import pandas as pd
from src.utils.validators import validate_columns

REQUIRED_COLUMNS = [
    "order-id", "purchase-date", "asin", "quantity", "revenue"
]

def load_sales(path="data/raw/sales_report.csv"):
    df = pd.read_csv(path)

    validate_columns(df, REQUIRED_COLUMNS, "Sales Report")

    df["purchase-date"] = pd.to_datetime(df["purchase-date"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")

    daily_sales = (
        df.groupby("asin")
        .agg(
            units_sold=("quantity", "sum"),
            revenue=("revenue", "sum")
        )
        .reset_index()
    )

    return daily_sales
