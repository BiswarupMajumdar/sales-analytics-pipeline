from utils.logger import log_info

def insert_data(conn, df):
    """
    Inserts cleaned data into database
    """

    df.to_sql(
        "sales",
        conn,
        if_exists="replace",
        index=False
    )

    log_info(
        "Data inserted into database"
    )

    print(
        "Data inserted into database"
    )