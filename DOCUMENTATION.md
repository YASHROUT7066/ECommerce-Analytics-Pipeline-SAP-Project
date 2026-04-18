# End-to-End Data Engineering Pipeline for E-Commerce Analytics

## 1. Introduction
In modern digital commerce, data is generated every second from orders, payments, product views, and customer interactions. Businesses need reliable systems to collect this data, clean it, and turn it into useful analytics. Without a proper pipeline, decision-making becomes slow and often inaccurate.

This project demonstrates a practical academic implementation of an end-to-end data engineering workflow. It includes data ingestion, transformation, loading, SQL-based analysis, notebook visualization, and a lightweight web dashboard. The objective is to replicate how real companies structure reporting pipelines in a simplified learning-friendly way.

---

## 2. Problem Statement
E-commerce teams often face the following challenges:
- Data arrives in raw CSV or logs with missing values and inconsistent formats.
- Business users need quick insights such as total sales and product-level performance.
- Manual analysis in spreadsheets is error-prone and difficult to repeat.
- There is no single process that connects raw data to live dashboard outputs.

The project solves this by creating a reproducible ETL pipeline and presenting processed insights through both notebook visuals and a web interface.

---

## 3. Proposed Solution
The solution is built as a modular pipeline with clear responsibilities:

1. **Ingest** raw sales CSV data from `data/raw/sales_data.csv`.
2. **Transform** the data by:
   - Filling missing `amount` values with mean amount.
   - Dropping rows where `date` is missing.
   - Casting date and amount to proper types.
3. **Load** cleaned data into `data/processed/cleaned_data.csv`.
4. **Log** each step in `logs/pipeline.log` for traceability.
5. **Analyze** with SQL queries and notebook charts.
6. **Visualize** in a Flask dashboard with one-click pipeline execution.

This modular design improves maintainability, debugging, and readability.

---

## 4. Key Features

### 4.1 Structured Project Layout
The repository is organized into dedicated folders for scripts, SQL, templates, dashboard notebooks, and data. This mirrors common enterprise project standards.

### 4.2 Robust Data Cleaning Logic
Transformation handles common data quality issues:
- Missing numeric values
- Missing date records
- Type normalization

### 4.3 Repeatable ETL Execution
Pipeline execution can be triggered:
- Directly via command line (`python main.py`)
- Through UI button in Flask dashboard (`/run`)

### 4.4 Logging and Traceability
Every ETL step is logged with timestamps, enabling quick troubleshooting and process monitoring.

### 4.5 Multi-Channel Analytics Output
Insights are available in multiple forms:
- SQL query scripts
- Jupyter notebook charts
- Browser-based HTML dashboard with Chart.js

---

## 5. Tech Stack
- **Language:** Python
- **Data Processing:** Pandas
- **Visualization:** Matplotlib, Chart.js
- **Web Framework:** Flask
- **Query Layer:** SQL scripts
- **Notebook:** Jupyter (`.ipynb`)
- **Storage:** CSV-based file system (raw + processed)

---

## 6. Workflow Architecture

### 6.1 Data Source Layer
Raw data is stored in `data/raw/sales_data.csv`. It simulates real order events with fields:
`order_id, customer, product, amount, date`.

### 6.2 Processing Layer
`scripts/ingest.py`, `scripts/transform.py`, and `scripts/load.py` form the ETL pipeline.

### 6.3 Orchestration Layer
`main.py` coordinates all ETL steps and writes logs.

### 6.4 Consumption Layer
Users consume insights through:
- Notebook charts in `dashboard/dashboard.ipynb`
- Flask dashboard in browser at port `3000`

---

## 7. SQL Analytics
The SQL folder includes:
- `schema.sql`: table design for sales dataset
- `queries.sql`: business-level analytics queries

Sample insights:
- Total revenue
- Sales distribution by product
- Top customers by spending

---

## 8. Screenshot Placeholders
> Add final screenshots here before project submission.

1. **Project Folder Structure**
   - Placeholder: `[Screenshot 1 - Project explorer view]`

2. **Flask Dashboard Home**
   - Placeholder: `[Screenshot 2 - Dashboard initial screen]`

3. **After Running Pipeline**
   - Placeholder: `[Screenshot 3 - Total sales + product sales + data table]`

4. **Notebook Charts**
   - Placeholder: `[Screenshot 4 - Bar chart and line chart output]`

5. **Log File Evidence**
   - Placeholder: `[Screenshot 5 - pipeline.log entries]`

---

## 9. Unique Points of This Project
- Combines data engineering and full-stack elements in one academic project.
- Keeps logic beginner-friendly while following industry-style structure.
- Includes both backend pipeline and frontend presentation layer.
- Designed to run without database setup, making it easy for demonstration and grading.
- Handles missing data gracefully to reflect practical ETL scenarios.

---

## 10. Future Improvements
- Integrate PostgreSQL or BigQuery as warehouse target.
- Add Airflow/Prefect for scheduled orchestration.
- Add data validation checks (e.g., Great Expectations).
- Introduce API ingestion from real e-commerce endpoints.
- Implement authentication and role-based dashboard access.
- Add automated tests and CI pipeline.
- Add KPI cards: daily sales trend, top category, average order value.

---

## 11. Conclusion
This project provides a complete, hands-on blueprint of how raw e-commerce data can be transformed into meaningful analytics through a clean ETL pipeline. It is intentionally simple to understand, but structured in a way that reflects real-world data engineering practices. Students can use this as a strong foundation for advanced projects involving cloud data platforms, orchestration tools, and production dashboards.
