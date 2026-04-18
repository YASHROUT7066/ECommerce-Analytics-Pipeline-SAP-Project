import pandas as pd


def transform_data(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Clean missing values and enforce expected data types."""
    cleaned_df = dataframe.copy()

    cleaned_df["amount"] = pd.to_numeric(cleaned_df["amount"], errors="coerce")
    mean_amount = cleaned_df["amount"].mean()
    cleaned_df["amount"] = cleaned_df["amount"].fillna(mean_amount)

    cleaned_df["date"] = pd.to_datetime(cleaned_df["date"], errors="coerce")
    cleaned_df = cleaned_df.dropna(subset=["date"])

    cleaned_df["amount"] = cleaned_df["amount"].astype(float)
    return cleaned_df
