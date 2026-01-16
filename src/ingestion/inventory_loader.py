import pandas as pd
from src.utils.validators import validate_columns

REQUIRED_COLUMNS = [
    "sku", "asin", "product-name", "available"
]

def load_inventory(path="data/raw/inventory_report.csv"):
    df = pd.read_csv(path)

    validate_columns(df, REQUIRED_COLUMNS, "Inventory Report")

    df = df.rename(columns={
        "product-name": "product_name",
        "available": "inventory_available"
    })

    df["inventory_available"] = pd.to_numeric(
        df["inventory_available"], errors="coerce"
    )

    return df[["sku", "asin", "product_name", "inventory_available"]]
