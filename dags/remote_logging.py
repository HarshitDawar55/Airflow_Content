from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="DAG_For_Remote_logging", catchup=False, tags=["Remote", "Logging"]
) as dag:
    task = BashOperator(
        task_id="Any_Task_For_Which_Remote_Logs_Will_Be_Generated",
        bash_command="echo My logs will be genrated at a remote location which is S3 in this scenario",
    )
