import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from main import main

# -----------------------------
# CONFIG
# -----------------------------
st.set_page_config(
    page_title="Sales Analytics Pro",
    layout="wide"
)

# -----------------------------
# PATH SETUP
# -----------------------------
ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT_DIR / "output"

# -----------------------------
# REFRESH PIPELINE BUTTON
# -----------------------------
if st.sidebar.button("🔄 Refresh Data Pipeline"):
    with st.spinner("Running ETL pipeline..."):
        main()
    st.success("Data refreshed successfully!")

# -----------------------------
# AUTO RUN IF FILES MISSING
# -----------------------------
required_files = [
    OUTPUT_DIR / "revenue_by_date.csv",
    OUTPUT_DIR / "revenue_by_product.csv",
    OUTPUT_DIR / "customer_sales.csv"
]

if not all(f.exists() for f in required_files):
    with st.spinner("Generating data..."):
        main()

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data(file_name):
    return pd.read_csv(OUTPUT_DIR / file_name)

revenue_by_date = load_data("revenue_by_date.csv")
revenue_by_product = load_data("revenue_by_product.csv")
customer_sales = load_data("customer_sales.csv")

# Convert date
revenue_by_date["date"] = pd.to_datetime(revenue_by_date["date"])

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

# Product filter
products = revenue_by_product["product"].unique()
selected_products = st.sidebar.multiselect(
    "Select Product",
    options=products,
    default=products
)

# Date filter
min_date = revenue_by_date["date"].min()
max_date = revenue_by_date["date"].max()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)

# Apply filters
filtered_product = revenue_by_product[
    revenue_by_product["product"].isin(selected_products)
]

filtered_date = revenue_by_date[
    (revenue_by_date["date"] >= pd.to_datetime(date_range[0])) &
    (revenue_by_date["date"] <= pd.to_datetime(date_range[1]))
]

# -----------------------------
# TITLE
# -----------------------------
st.title("📊 Sales Analytics PRO Dashboard")

# -----------------------------
# KPI CALCULATION
# -----------------------------
total_revenue = filtered_product["total_sales"].sum()

prev_revenue = revenue_by_product["total_sales"].sum()
growth = ((total_revenue - prev_revenue) / prev_revenue) * 100 if prev_revenue else 0

# -----------------------------
# KPI UI
# -----------------------------
st.header("Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Revenue", f"₹ {total_revenue:,.2f}", f"{growth:.2f}%")

col2.metric("📦 Products", filtered_product["product"].nunique())

col3.metric("👤 Customers", customer_sales["customer_id"].nunique())

# -----------------------------
# DOWNLOAD REPORT
# -----------------------------
csv = filtered_product.to_csv(index=False)

st.download_button(
    label="📥 Download Product Report",
    data=csv,
    file_name="product_report.csv",
    mime="text/csv"
)

# -----------------------------
# CHARTS
# -----------------------------
st.header("Revenue Over Time")

st.plotly_chart(
    px.line(
        filtered_date,
        x="date",
        y="total_sales",
        title="Revenue Trend"
    ),
    use_container_width=True
)

st.header("Product Performance")

st.plotly_chart(
    px.bar(
        filtered_product,
        x="product",
        y="total_sales",
        title="Revenue by Product"
    ),
    use_container_width=True
)

st.header("Customer Analysis")

st.plotly_chart(
    px.bar(
        customer_sales,
        x="customer_id",
        y="total_sales",
        title="Customer Spending"
    ),
    use_container_width=True
)