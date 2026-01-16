# Smart AdTune – Automated Amazon Ad Budget Optimization

Smart AdTune is a Python-based automation system that processes real Amazon Seller Central and Amazon Advertising reports to automatically optimize ad campaign budgets using inventory-aware and ROAS-driven rules.

---

## Features

- Uses real Amazon Seller & Ads report schemas  
- Automatically pauses, increases, or reduces ad budgets  
- Daily scheduled execution with GitHub Actions  
- Streamlit dashboard for operational visibility  

---

## Decision Logic

| Condition | Action |
|---------|--------|
| Inventory < 10 | Pause campaign |
| ROAS ≥ 3.0 & healthy inventory | Increase budget |
| ROAS < 1.2 | Decrease budget |
| Otherwise | No change |

---

## System Architecture


system_architecture:
  data_sources:
    - amazon_seller_central_reports
    - amazon_advertising_reports

  ingestion_layer:
    language: python
    responsibilities:
      - read_csv_reports
      - validate_schemas
      - clean_and_normalize_data

  decision_engine:
    type: rule_based
    inputs:
      - inventory_levels
      - roas
      - sales_volume
    actions:
      - pause_campaign
      - increase_budget
      - decrease_budget
      - no_change

  automation:
    scheduler: github_actions
    frequency: daily

  outputs:
    decision_logs:
      format: csv
      location: outputs/decisions_log.csv

  notifications:
    type: email
    trigger: pipeline_completion

  visualization:
    tool: streamlit
    purpose: operational_dashboard


## Project Structure
project_structure:
  root:
    - README.md
    - requirements.txt

  data:
    raw:
      - inventory_report.csv
      - sales_report.csv
      - ads_campaign_report.csv

  src:
    ingestion:
      - inventory_loader.py
      - sales_loader.py
      - ads_loader.py
    utils:
      - validators.py
    core:
      - decision_engine.py
      - apply_decisions.py
    notifications:
      - email_notifier.py
    app:
      - dashboard.py
      - main.py

  outputs:
    - decisions_log.csv

  automation:
    github:
      workflows:
        - daily_run.yml

## Setup

Clone the repository:

git clone https://github.com/<your-username>/smart-adtune.git
cd smart-adtune


Create and activate a virtual environment:

macOS / Linux:

python3 -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
.\venv\Scripts\Activate.ps1


## Install dependencies:

pip install -r requirements.txt

## Run the Pipeline
python -m src.main


Output file:

outputs/decisions_log.csv

## Run the Dashboard
streamlit run src/dashboard.py


Open in browser:

http://localhost:8501

## Automation

The pipeline runs daily using GitHub Actions and generates auditable decision logs for each execution.

Author
Krupa Mistry
