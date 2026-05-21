import pandas as pd
from utils.logger import log_info, log_error


def load_data(file_path):
    """
    Reads sales data
    """

    try:
        df = pd.read_csv(file_path)

        log_info(
            "Data Loaded Successfully"
        )

        print(
            "Data Loaded Successfully"
        )

        return df

    except Exception as e:

        log_error(
            f"Failed loading data: {e}"
        )

        raise