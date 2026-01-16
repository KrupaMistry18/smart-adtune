import pandas as pd
from src.utils.validators import validate_columns

REQUIRED_COLUMNS = [
    "campaignId", "asin", "dailyBudget", "spend", "roas", "cpc"
]

def load_ads(path="data/raw/ads_campaign_report.csv"):
    df = pd.read_csv(path)

    validate_columns(df, REQUIRED_COLUMNS, "Ads Campaign Report")

    df = df.rename(columns={
        "campaignId": "campaign_id",
        "dailyBudget": "daily_budget"
    })

    numeric_cols = ["daily_budget", "spend", "roas", "cpc"]
    df[numeric_cols] = df[numeric_cols].apply(
        pd.to_numeric, errors="coerce"
    )

    return df[[
        "campaign_id", "asin", "daily_budget", "spend", "roas", "cpc"
    ]]
