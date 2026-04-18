# End-to-End Data Engineering Pipeline for E-Commerce Analytics

## Overview
This is a simple but complete academic project that shows how a data engineering pipeline works from raw data to analytics dashboard.  
The project reads sales data, cleans it with ETL scripts, stores processed data, and shows business insights in a Flask web app.

This project is inspired by real-world data warehouse pipelines similar to SAP analytics systems.

## Features
- Raw e-commerce sales dataset with real-world style missing values
- ETL pipeline split into clear `ingest`, `transform`, and `load` scripts
- Logging support for pipeline execution
- SQL schema and analysis queries
- Jupyter notebook dashboard with charts
- Flask UI to run pipeline and view analytics in browser

## Tech Stack
- Python
- Pandas
- Matplotlib
- Flask
- SQL
- Jupyter Notebook

## Project Structure
```text
sap-data-analytics-project/
├── app.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── raw/sales_data.csv
│   └── processed/cleaned_data.csv
├── scripts/
│   ├── ingest.py
│   ├── transform.py
│   └── load.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── dashboard.ipynb
├── templates/
│   └── index.html
└── logs/
    └── pipeline.log
```
