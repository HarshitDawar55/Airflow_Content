from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id="queue_dag", catchup=False, tags=["Queue"]) as dag:
    task = BashOperator(
        task_id="Queue_Bounded",
        bash_command="echo I am running on high_memory queue",
        queue="high_memory",
    )

    task2 = BashOperator(
        task_id="Non_Queue_Bounded",
        bash_command="echo I am non queue bounded",
    )