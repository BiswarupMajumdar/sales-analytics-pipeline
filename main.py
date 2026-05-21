from utils.logger import log_info, log_error
import os
import json

from config.config import (
    DATA_PATH,
    OUTPUT_DIR
)

from etl.extract import load_data
from etl.transform import clean_data
from etl.load import insert_data

from db.database import connect_db

from analytics.analysis import (
    analyze_data,
    prepare_chart_data
)


def main():

  try:
    # -----------------------------
    # EXTRACT
    # -----------------------------
    df = load_data(DATA_PATH)

    # -----------------------------
    # TRANSFORM
    # -----------------------------
    df = clean_data(df)

    # -----------------------------
    # LOAD TO DATABASE
    # -----------------------------
    conn = connect_db()

    insert_data(conn, df)

    # -----------------------------
    # ANALYSIS
    # -----------------------------
    report = analyze_data(df)

    chart_data = prepare_chart_data(df)

    conn.close()

    # -----------------------------
    # SAVE OUTPUTS
    # -----------------------------
    os.makedirs(
        OUTPUT_DIR,
        exist_ok=True
    )

    with open(
            f"{OUTPUT_DIR}/report.json",
            "w"
    ) as f:
        json.dump(
            report,
            f,
            indent=4
        )

    chart_data[
        "revenue_by_date"
    ].to_csv(
        f"{OUTPUT_DIR}/revenue_by_date.csv",
        index=False
    )

    chart_data[
        "revenue_by_product"
    ].to_csv(
        f"{OUTPUT_DIR}/revenue_by_product.csv",
        index=False
    )

    chart_data[
        "customer_sales"
    ].to_csv(
        f"{OUTPUT_DIR}/customer_sales.csv",
        index=False
    )

    log_info(
        "Pipeline completed successfully"
    )

    print(
        "Pipeline completed successfully 🚀"
    )

  except Exception as e:

        log_error(
            f"Pipeline failed: {e}"
        )

        print(
            f"Pipeline failed: {e}"
        )


if __name__ == "__main__":
    main()