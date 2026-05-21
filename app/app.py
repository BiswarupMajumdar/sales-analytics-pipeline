import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os
import sys

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(ROOT_DIR)

from main import main
# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# PROJECT PATH
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

# -----------------------------
# AUTO GENERATE DATA
# -----------------------------
required_files = [
    "revenue_by_date.csv",
    "revenue_by_product.csv",
    "customer_sales.csv"
]

missing_files = any(
    not (OUTPUT_DIR / file).exists()
    for file in required_files
)

if missing_files:
    with st.spinner(
            "Generating analytics data..."
    ):
        main()

# -----------------------------
# CACHE DATA LOADING
# -----------------------------
@st.cache_data
def load_csv(filename):
    file_path = OUTPUT_DIR / filename

    if file_path.exists():
        return pd.read_csv(file_path)

    st.error(
        f"Missing file: {file_path}"
    )
    st.stop()


# -----------------------------
# LOAD DATA
# -----------------------------
revenue_by_date = load_csv(
    "revenue_by_date.csv"
)

revenue_by_product = load_csv(
    "revenue_by_product.csv"
)

customer_sales = load_csv(
    "customer_sales.csv"
)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("📌 Filters")

selected_products = st.sidebar.multiselect(
    "Select Product",
    options=revenue_by_product[
        "product"
    ].unique(),
    default=revenue_by_product[
        "product"
    ].unique()
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_products = revenue_by_product[
    revenue_by_product[
        "product"
    ].isin(selected_products)
]

# -----------------------------
# DASHBOARD TITLE
# -----------------------------
st.title(
    "📊 Sales Analytics Dashboard"
)

st.markdown(
    """
    Production-grade sales analytics dashboard  
    powered by **Python, SQLite, Streamlit & Plotly**
    """
)

# -----------------------------
# KPI SECTION
# -----------------------------
st.header("📌 Key Metrics")

total_revenue = filtered_products[
    "total_sales"
].sum()

total_products = filtered_products[
    "product"
].nunique()

total_customers = customer_sales[
    "customer_id"
].nunique()

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Total Revenue",
    f"₹ {total_revenue:.2f}"
)

col2.metric(
    "📦 Products",
    total_products
)

col3.metric(
    "👤 Customers",
    total_customers
)

# -----------------------------
# REVENUE OVER TIME
# -----------------------------
st.header("📈 Revenue Over Time")

fig_line = px.line(
    revenue_by_date,
    x="date",
    y="total_sales",
    title="Revenue Over Time"
)

st.plotly_chart(
    fig_line,
    use_container_width=True
)

# -----------------------------
# PRODUCT REVENUE
# -----------------------------
st.header("🏆 Product Revenue")

fig_product = px.bar(
    filtered_products,
    x="product",
    y="total_sales",
    title="Revenue by Product"
)

st.plotly_chart(
    fig_product,
    use_container_width=True
)

# -----------------------------
# CUSTOMER SALES
# -----------------------------
st.header("👤 Customer Sales")

fig_customer = px.bar(
    customer_sales,
    x="customer_id",
    y="total_sales",
    title="Customer Sales"
)

st.plotly_chart(
    fig_customer,
    use_container_width=True
)