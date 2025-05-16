from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
import logging

table = "sales"


def get_value_of_variable(**context):
    logging.warning(f"Received context is: {context}")
    table_name = context["dag_run"].conf.get("table_name", "default")
    print(f"Table_Name fetched is: {table_name}")


with DAG(
    dag_id="Parameterized_DAG",
    catchup=False,
    tags=["Parameterized"],
    params={"table_name": table},
) as dag:
    task = PythonOperator(
        task_id="Parameterized_task", python_callable=get_value_of_variable
    )
