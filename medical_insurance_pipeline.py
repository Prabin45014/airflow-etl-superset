from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# 🔹 File Paths
RAW_PATH = "/home/ubuntu/airflow/data/raw/medical_insurance.csv"
CLEAN_PATH = "/home/ubuntu/airflow/data/processed/clean_medical_insurance.csv"

default_args = {
    'owner': 'prabin',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id="medical_insurance_pipeline",
    default_args=default_args,
    schedule_interval=None,
    catchup=False
) as dag:

    # 🔹 1. CLEAN DATA
    @task
    def clean_data():

        df = pd.read_csv(RAW_PATH)

        # Strip column spaces
        df.columns = df.columns.str.strip()

        # ✅ KEEP ONLY REQUIRED COLUMNS
        required_columns = [
            "person_id",
            "age",
            "sex",
            "region",
            "urban_rural",
            "income",
            "marital_status",
            "smoker",
            "alcohol_freq",
            "annual_premium",
            "monthly_premium",
            "claims_count",
            "avg_claim_amount",
            "total_claims_paid",
            "diabetes",
            "cancer_history",
            "kidney_disease",
            "liver_disease",
            "mental_health",
            "is_high_risk"
        ]

        # Keep only available columns
        df = df[[col for col in required_columns if col in df.columns]]

        # 🔹 Remove duplicates
        df = df.drop_duplicates()

        # 🔹 Handle missing values
        df = df.fillna("Unknown")

        # 🔹 Save cleaned file
        df.to_csv(CLEAN_PATH, index=False)

        print("✅ Medical data cleaned and saved")

    # 🔹 2. LOAD TO MYSQL
    @task
    def load_to_mysql():

        df = pd.read_csv(CLEAN_PATH)

        engine = create_engine("mysql+pymysql://root:Pass%40123@localhost:3306/medical_insurance")

        df.to_sql("medical_insurance", con=engine, if_exists="replace", index=False)

        print("✅ Medical data loaded into MySQL")

    # 🔹 Task Flow
    clean_data() >> load_to_mysql()
