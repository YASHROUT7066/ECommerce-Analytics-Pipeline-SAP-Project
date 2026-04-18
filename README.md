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

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the web app:
   ```bash
   python app.py
   ```
3. Open browser:
   - [http://localhost:3000](http://localhost:3000)
4. Click **Run Pipeline** to generate cleaned data and view dashboard outputs.

You can also run ETL directly:
```bash
python main.py
```

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

## Future Improvements
- Add database loading step (PostgreSQL/MySQL) after transformation
- Add unit tests for ETL scripts
- Add more advanced KPI metrics (AOV, repeat rate, category trends)
- Add authentication and role-based access in Flask app
- Dockerize the project for easier deployment
