from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id="Child_DAG", catchup=False, tags=["Child"]) as dag:
    task = BashOperator(
        task_id="Child_Task_1", bash_command="echo I am task 1 of child DAG"
    )

