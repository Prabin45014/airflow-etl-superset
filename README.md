Airflow-ETL-Superset
Project Overview
This project demonstrates an end-to-end data pipeline using Apache Airflow, where raw datasets are cleaned, transformed, stored in MySQL, and visualized using Apache Superset dashboards.

📌 Project Overview**
This project is an end-to-end data pipeline built using Apache Airflow to process a medical insurance dataset. The goal of the project is to automate data cleaning, storage, and visualization for better analysis.
The raw dataset is first uploaded into the Airflow system, where a DAG pipeline is created to clean and transform the data using Python (Pandas). Only the required columns are selected, and unnecessary data is removed. The cleaned data is then stored in a separate processed directory.
After processing, the data is automatically loaded into a MySQL database. This database is then connected to Apache Superset, where SQL queries are used to create charts and interactive dashboards.
The project helps in analyzing key insights such as customer risk levels, claims behavior, premium trends, and demographic patterns.

🛠️ Tech Stack
* Raw Data Source → Kaggle dataset (medical\_insurance.csv)
* Server → AWS Cloud (EC2 Ubuntu Server)
* Apache Airflow → Workflow orchestration
* Python (Pandas) → Data cleaning \& transformation
* MySQL → Data storage Apache Superset → Data visualization 
* GitHub → Version control
 
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

⚙️ Step-by-Step Implementation
1. Downloaded the medical insurance dataset (CSV) from Kaggle and stored it locally.
2. Launched an AWS EC2 Ubuntu server and set up the environment by installing:
* Apache Airflow
* MySQL
* Apache Superset
* Python and required libraries (Pandas, SQLAlchemy, PyMySQL)
3. Configured Airflow and created a proper directory structure:
* data/raw/ → for input datasets
* data/processed/ → for cleaned data
4. Uploaded the dataset (medical\_insurance.csv) into the raw data directory of Airflow.
5. Developed an Airflow DAG pipeline to automate the ETL process:
  # Extracted data from CSV
  # Transformed data using Pandas:
   * Selected only required columns
   * Cleaned missing values
   * Removed duplicates
# Saved the cleaned dataset into the processed directory
6. Implemented a data loading step in the DAG:
* Connected to MySQL using SQLAlchemy
* Loaded cleaned data into a MySQL table (medical\_insurance)
7. Configured database connection (host, username, password) inside the DAG for automation.
8. Connected MySQL to Apache Superset for visualization.
9. Created interactive dashboards in Superset using SQL queries.
  
📈 Dashboard and Chart Insights
(Dashboard -> Medical Insurance Risk \& Claims Analytics)
Charts
* Total Customer
* Total Claims Paid
* Avg claim Amount
* Avg Premium by Urban Rural
* Premium by age
* Region-wise customers
* Claim count distribution
* Claim vs Premium
* Avg Claim amount by age group
* Age distribution
* Gender distribution
* Marital Status
 





