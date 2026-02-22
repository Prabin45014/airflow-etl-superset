# Airflow-ETL-Superset



📌 Project Overview
This project demonstrates an end-to-end data pipeline using Apache Airflow, where raw datasets are cleaned, transformed, stored in MySQL, and visualized using Apache Superset dashboards.



🛠️ Tech Stack



&nbsp;  Raw Data Source → Kaggle dataset (medical\_insurance.csv)

&nbsp;  Server → AWS Cloud (EC2 Ubuntu Server)

&nbsp;  Apache Airflow → Workflow orchestration

&nbsp;  Python (Pandas) → Data cleaning \& transformation

MySQL → Data storage
Apache Superset → Data visualization
GitHub → Version control



📂 Project Structure
airflow/
│
├── dags/
│   ├── medical\_insurance\_pipeline.py
│  
├── data/
│   ├── raw/medical\_insurance.csv
│   └── processed/clean\_medical\_insurance.csv
│
├── logs/
└── airflow.cfg



🔄 Data Pipeline Flow
Raw CSV Data
↓
AWS (Ubuntu Server)
↓
Apache Airflow DAG
↓
Data Cleaning (Pandas)
↓
Processed Data (CSV)
↓
MySQL Database
↓
Apache Superset Dashboard



🔑 Key Features
✅ Automated ETL pipelines using Airflow
✅ Data cleaning using Pandas
✅ MySQL integration for structured storage
✅ Dashboard-ready datasets for Superset
✅ Reusable pipeline design



📈 Dashboard and Chart Insights
(Dashboard -> Medical Insurance Risk \& Claims Analytics)
Charts

Total Customer

&nbsp;  Total Claims Paid

Avg claim Amount

Avg Premium by Urban Rural

Premium by age

Region-wise customers

Claim count distribution

Claim vs Premium

Avg Claim amount by age group

Age distribution

Gender distribution

Marital Status





