from airflow import DAG
from airflow.operators.python import PythonOperator
import logging


def send_data(**context):
    context["ti"].xcom_push(key="sender", value="Harshit Dawar")


def receive_data(**context):
    data = context["ti"].xcom_pull(task_ids="task_for_xcom_to_push", key="sender")
    logging.warning(f"Data Received from XCOM is {data}")


with DAG(dag_id="XCOM_Training", tags=["XCOM"], catchup=False, schedule="@once") as dag:
    task_to_push = PythonOperator(
        task_id="task_for_xcom_to_push", python_callable=send_data
    )
    task_to_pull = PythonOperator(
        task_id="task_to_pull_xcom_data", python_callable=receive_data
    )

    task_to_push >> task_to_pull

