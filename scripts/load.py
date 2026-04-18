from pathlib import Path

import pandas as pd


def load_data(
    dataframe: pd.DataFrame, output_path: str = "data/processed/cleaned_data.csv"
) -> None:
    """Write cleaned dataframe to CSV, creating directories if needed."""
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    dataframe.to_csv(output_file, index=False)
    print("Data saved successfully")
