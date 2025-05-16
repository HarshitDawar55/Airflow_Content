from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id="Pools_DAG", catchup=False, tags=["Pools"]) as dag:
    task1 = BashOperator(
        task_id="PoolTask1",
        bash_command="sleep 15",
        pool="Concurrent_Database_Operations",
        priority_weight=50
    )
    task2 = BashOperator(
        task_id="PoolTask2",
        bash_command="sleep 15",
        pool="Concurrent_Database_Operations",
        priority_weight=50
    )
    task3 = BashOperator(
        task_id="PoolTask3",
        bash_command="sleep 15",
        pool="Concurrent_Database_Operations",
        priority_weight=10
    )
    task4 = BashOperator(
        task_id="PoolTask4",
        bash_command="sleep 15",
        pool="Concurrent_Database_Operations",
        priority_weight=100
    )
    task5 = BashOperator(
        task_id="PoolTask5",
        bash_command="sleep 15",
        pool="Concurrent_Database_Operations",
        priority_weight=100
    )

