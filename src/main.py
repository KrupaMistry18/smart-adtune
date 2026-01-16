from src.ingestion.inventory_loader import load_inventory
from src.ingestion.sales_loader import load_sales
from src.ingestion.ads_loader import load_ads
from src.apply_decisions import apply_budget_decisions

def run():
    inventory = load_inventory()
    sales = load_sales()
    ads = load_ads()

    merged = (
        ads
        .merge(inventory, on="asin", how="left")
        .merge(sales, on="asin", how="left")
    )

    decision_log = apply_budget_decisions(merged)
    decision_log.to_csv("outputs/decisions_log.csv", index=False)

    print(decision_log)

if __name__ == "__main__":
    run()
