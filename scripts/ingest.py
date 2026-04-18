import pandas as pd


def ingest_data(file_path: str = "data/raw/sales_data.csv") -> pd.DataFrame:
    """Read raw sales CSV and return a dataframe."""
    dataframe = pd.read_csv(file_path)
    print("Data loaded successfully")
    return dataframe
