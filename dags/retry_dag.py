from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta

params = {
    "retries": 5,
    "retry_delay": timedelta(seconds=5)
}

with DAG(
    dag_id="Retry_DAG",
    catchup=False,
    tags=["Retriable"],
    schedule="@weekly",
    default_args = params,
) as dag:
    task = BashOperator(
        task_id="Retry_Demo_Task",
        bash_command="echo I am a task with the power to retry myself",
    )

    task

