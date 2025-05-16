from airflow import DAG
from airflow.operators.python import BranchPythonOperator, PythonOperator
from airflow.operators.bash import BashOperator

import random

def download_file():
    return "even" if random.randint(1,10) % 2 == 0 else "odd"

def even_number():
    return "Even Number"

def odd_number():
    return "Odd Number"

with DAG(dag_id="Branching_DAG",
         catchup=False,
         tags=["Branching"]) as dag:
    starting = BashOperator(task_id="Starting_Point", bash_command="echo I am starting the execution")

    branching = BranchPythonOperator(task_id="Branching_Task", python_callable=download_file)  # Either it will have 'even' value or 'odd' value

    even = PythonOperator(task_id="even", python_callable=even_number)
    odd = PythonOperator(task_id="odd", python_callable=odd_number)

    starting >> branching >> [even, odd]