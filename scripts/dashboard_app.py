import streamlit as st
import pandas as pd
import plotly.express as px

# Load processed session data
df = pd.read_csv('../data/session_funnel_summary.csv')

st.set_page_config(page_title="Customer Journey Dashboard", layout="wide")

st.title("Customer Journey Analytics Dashboard")

# --- KPIs ---
total_sessions = len(df)
purchase_count = df[df['funnel_stage'] == 'Purchased'].shape[0]
cart_count = df[df['funnel_stage'] == 'Carted'].shape[0]
view_only_count = df[df['funnel_stage'] == 'Viewed Only'].shape[0]

col1, col2, col3 = st.columns(3)
col1.metric("Total Sessions", total_sessions)
col2.metric("Purchases", purchase_count, f"{purchase_count / total_sessions:.2%}")
col3.metric("Carted but Not Purchased", cart_count - purchase_count, f"{(cart_count - purchase_count) / total_sessions:.2%}")

# --- Funnel Chart ---
funnel_counts = df['funnel_stage'].value_counts().reindex(['Viewed Only', 'Carted', 'Purchased'], fill_value=0)

fig = px.funnel(
    y=funnel_counts.index,
    x=funnel_counts.values,
    labels={'x': 'Session Count', 'y': 'Funnel Stage'},
    title="User Funnel"
)

st.plotly_chart(fig, use_container_width=True)

# --- Drop-off Breakdown ---
st.subheader("Funnel Stage Distribution")
st.dataframe(funnel_counts.reset_index().rename(columns={'index': 'Stage', 'funnel_stage': 'Session Count'}))
