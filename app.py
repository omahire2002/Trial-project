
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Mini Sales Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Mini Sales Analytics Dashboard")
st.write("Explore sales performance using Python and Streamlit.")

# Sample sales dataset
data = [
    {"Product": "Laptop", "Quantity": 2, "Price": 50000},
    {"Product": "Mouse", "Quantity": 10, "Price": 500},
    {"Product": "Keyboard", "Quantity": 5, "Price": 1500},
    {"Product": "Monitor", "Quantity": 3, "Price": 12000},
    {"Product": "Laptop", "Quantity": 1, "Price": 50000},
    {"Product": "Mouse", "Quantity": 8, "Price": 500},
]

df = pd.DataFrame(data)
df["Revenue"] = df["Quantity"] * df["Price"]

# Sidebar filter
st.sidebar.header("Filters")
products = st.sidebar.multiselect(
    "Select products",
    options=sorted(df["Product"].unique()),
    default=sorted(df["Product"].unique())
)

filtered_df = df[df["Product"].isin(products)]

# Calculate KPIs from filtered data
total_revenue = filtered_df["Revenue"].sum()
transactions = len(filtered_df)
units_sold = filtered_df["Quantity"].sum()
avg_transaction = (
    total_revenue / transactions if transactions else 0
)

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Transactions", transactions)
col3.metric("Units Sold", units_sold)
col4.metric("Avg. Transaction", f"₹{avg_transaction:,.0f}")

st.divider()

# Sales chart
st.subheader("Revenue by Product")

product_revenue = (
    filtered_df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(product_revenue)

# Dataset
st.subheader("Sales Dataset")
st.dataframe(filtered_df, use_container_width=True)

# Download filtered data
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Sales Data as CSV",
    data=csv,
    file_name="sales_analysis.csv",
    mime="text/csv"
)