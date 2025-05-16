from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def task1():
    return "I am Task 1"

def task2():
    return "I am Task 2"

with DAG(dag_id="Empty_Operator", catchup=False, tags=["Empty"]) as dag:
    starting = EmptyOperator(task_id="Starting_Point")
    task_one = PythonOperator(task_id="1", python_callable=task1)
    task_two = PythonOperator(task_id="2", python_callable=task2)
    stop = EmptyOperator(task_id="DAG_Completed")

    starting >> [task_one, task_two] >> stop