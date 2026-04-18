import os
import subprocess
import sys
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)


def build_dashboard_context(cleaned_path: Path) -> dict:
    if not cleaned_path.exists():
        return {
            "message": "Run pipeline first",
            "total_sales": 0.0,
            "sales_by_product": {},
            "tables": "",
            "labels": [],
            "values": [],
            "records": [],
        }

    dataframe = pd.read_csv(cleaned_path)
    if dataframe.empty:
        return {
            "message": "No data available",
            "total_sales": 0.0,
            "sales_by_product": {},
            "tables": "",
            "labels": [],
            "values": [],
            "records": [],
        }

    dataframe["amount"] = pd.to_numeric(dataframe["amount"], errors="coerce").fillna(0.0)
    dataframe["date"] = pd.to_datetime(dataframe["date"], errors="coerce")
    dataframe = dataframe.sort_values("date")

    sales_by_product = dataframe.groupby("product")["amount"].sum().round(2).to_dict()
    display_df = dataframe.copy()
    display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")
    table_html = display_df.to_html(classes="data-table", index=False)
    return {
        "message": "Data loaded successfully",
        "total_sales": float(dataframe["amount"].sum()),
        "sales_by_product": sales_by_product,
        "tables": table_html,
        "labels": list(sales_by_product.keys()),
        "values": list(sales_by_product.values()),
        "records": display_df.to_dict(orient="records"),
    }


@app.route("/", methods=["GET"])
def index():
    cleaned_path = Path("data/processed/cleaned_data.csv")
    context = build_dashboard_context(cleaned_path)
    return render_template("index.html", **context)


@app.route("/run", methods=["POST"])
def run_pipeline():
    Path("logs").mkdir(parents=True, exist_ok=True)
    with open("logs/flask_run.log", "a", encoding="utf-8") as log_file:
        subprocess.run(
            [sys.executable, "main.py"],
            stdout=log_file,
            stderr=log_file,
            check=False,
        )

    cleaned_path = Path("data/processed/cleaned_data.csv")
    context = build_dashboard_context(cleaned_path)
    return render_template("index.html", **context)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
