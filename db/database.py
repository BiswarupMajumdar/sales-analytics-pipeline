import sqlite3
import os


def connect_db(
        db_path="database/sales.db"
):
    """
    Connects to SQLite database
    """

    os.makedirs(
        "database",
        exist_ok=True
    )

    conn = sqlite3.connect(
        db_path
    )

    return conn