import pandas as pd


def generate_kpis(df):
    """
    Generates KPI metrics
    """

    total_revenue = df["total_sales"].sum()
    total_orders = len(df)
    total_products = df["product"].nunique()
    total_customers = df["customer_id"].nunique()

    return {
        "total_revenue": total_revenue,
        "total_orders": total_orders,
        "total_products": total_products,
        "total_customers": total_customers
    }


def analyze_data(df):
    """
    Generates business insights
    """

    total_revenue = df["total_sales"].sum()

    top_product = (
        df.groupby("product")
        ["total_sales"]
        .sum()
        .idxmax()
    )

    customer_sales = (
        df.groupby("customer_id")
        ["total_sales"]
        .sum()
    )

    report = {
        "total_revenue": float(total_revenue),
        "top_product": top_product,
        "top_customers": customer_sales.head(5).to_dict()
    }

    print("Analysis Done")

    return report


def prepare_chart_data(df):
    """
    Prepares chart-ready data
    """

    revenue_by_date = (
        df.groupby("date")
        ["total_sales"]
        .sum()
        .reset_index()
    )

    revenue_by_product = (
        df.groupby("product")
        ["total_sales"]
        .sum()
        .reset_index()
    )

    customer_sales = (
        df.groupby("customer_id")
        ["total_sales"]
        .sum()
        .reset_index()
    )

    return {
        "revenue_by_date": revenue_by_date,
        "revenue_by_product": revenue_by_product,
        "customer_sales": customer_sales
    }