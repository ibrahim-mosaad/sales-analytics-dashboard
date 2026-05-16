import streamlit as st

from data_loader import load_data
from analysis import calculate_kpis, create_target
from model import predict_profit
from visualizations import sales_by_region, profit_distribution

st.set_page_config(
    page_title="Sales AI Dashboard",
    layout="wide"
)

st.title("📊 Sales Analytics + AI Prediction (SVM)")

# Load data
df = load_data()
df = create_target(df)

# KPIs
kpis = calculate_kpis(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Sales", f"{kpis['sales']:,.0f}")
col2.metric("Profit", f"{kpis['profit']:,.0f}")
col3.metric("Orders", kpis["orders"])
col4.metric("Customers", kpis["customers"])

st.markdown("---")

# AI Section
st.subheader("🤖 Predict Order Profitability")

sales_input = st.number_input("Sales")
qty_input = st.number_input("Quantity")

if st.button("Predict"):

    result = predict_profit(sales_input, qty_input)

    st.success(result)

st.markdown("---")

# Charts
st.plotly_chart(sales_by_region(df), use_container_width=True)

st.plotly_chart(profit_distribution(df), use_container_width=True)