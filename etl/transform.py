import pandas as pd
from utils.logger import log_info

def clean_data(df):
    """
    Cleans raw sales data
    """

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove missing values
    df.dropna(inplace=True)

    # Convert numeric columns safely
    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    df.dropna(
        subset=["quantity", "price"],
        inplace=True
    )

    # Fix data types
    df["quantity"] = df["quantity"].astype(int)
    df["price"] = df["price"].astype(float)

    # Feature engineering
    df["total_sales"] = (
        df["quantity"] *
        df["price"]
    )

    # Fix date column
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    df.dropna(
        subset=["date"],
        inplace=True
    )

    log_info(
        "Data Cleaned Successfully"
    )

    print(
        "Data Cleaned Successfully"
    )
    return df