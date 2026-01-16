def evaluate_campaign(row):
    inventory = row["inventory_available"]
    roas = row["roas"]
    budget = row["daily_budget"]
    units_sold = row.get("units_sold", 0)

    # Rule 1: Inventory protection
    if inventory is not None and inventory < 10:
        return "PAUSE", 0, "Low inventory risk"

    # Rule 2: High performer scaling
    if roas >= 3.0 and inventory >= 20 and units_sold >= 5:
        return "INCREASE", round(budget * 1.2, 2), "High ROAS with healthy inventory"

    # Rule 3: Poor performance control
    if roas < 1.2:
        return "DECREASE", round(budget * 0.7, 2), "Low ROAS"

    # Rule 4: Stable state
    return "NO_CHANGE", budget, "Performance stable"

