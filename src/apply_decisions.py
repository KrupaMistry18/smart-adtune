import pandas as pd
from src.decision_engine import evaluate_campaign

def apply_budget_decisions(df):
    decisions = []

    for _, row in df.iterrows():
        action, new_budget, reason = evaluate_campaign(row)

        decisions.append({
            "asin": row["asin"],
            "campaign_id": row["campaign_id"],
            "old_budget": row["daily_budget"],
            "new_budget": new_budget,
            "action": action,
            "reason": reason,
            "roas": row["roas"],
            "inventory": row["inventory_available"]
        })

    return pd.DataFrame(decisions)
