from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import timedelta

with DAG(dag_id="Timeout_DAG", catchup=False, tags=["Timeout"]) as dag:
    task = BashOperator(
        task_id="Sleep_For_30_Seconds",
        bash_command="sleep 30",
        execution_timeout=timedelta(seconds=10),
    )
    