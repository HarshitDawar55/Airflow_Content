from airflow.models import Variable
from airflow import DAG
from airflow.operators.python import PythonOperator
import logging

def print_backend_url():
    logging.info(Variable.get("backend_application_url"))


with DAG(
    dag_id="DAG_With_Variables",
    catchup=False,
    tags=["With_Variables"],
    schedule="@daily",
) as dag:
    task = PythonOperator(
        task_id="Printing_Value_From_Variable", python_callable=print_backend_url
    )

    task

