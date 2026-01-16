import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Smart AdTune Dashboard",
    layout="wide"
)

st.title("📊 Smart AdTune – Amazon Ad Optimization Dashboard")

# Load decision log
DATA_PATH = "outputs/decisions_log.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

try:
    df = load_data()
except FileNotFoundError:
    st.error("Decision log not found. Run the pipeline first.")
    st.stop()

# ---- Summary Metrics ----
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Campaigns", len(df))
col2.metric("Paused Campaigns", (df["action"] == "PAUSE").sum())
col3.metric("Increased Budgets", (df["action"] == "INCREASE").sum())
col4.metric("Decreased Budgets", (df["action"] == "DECREASE").sum())

st.divider()

# ---- Filters ----
action_filter = st.multiselect(
    "Filter by Action",
    options=df["action"].unique(),
    default=df["action"].unique()
)

filtered_df = df[df["action"].isin(action_filter)]

# ---- Table View ----
st.subheader("📌 Campaign Decisions")

st.dataframe(
    filtered_df[[
        "asin",
        "campaign_id",
        "old_budget",
        "new_budget",
        "action",
        "reason",
        "roas",
        "inventory"
    ]],
    use_container_width=True
)

st.divider()

# ---- Simple Insights ----
st.subheader("📈 Budget Change Impact")

filtered_df["budget_change"] = (
    filtered_df["new_budget"] - filtered_df["old_budget"]
)

st.bar_chart(
    filtered_df.set_index("asin")["budget_change"]
)

st.caption(
    "Positive values indicate budget increases; negative values indicate reductions or pauses."
)
