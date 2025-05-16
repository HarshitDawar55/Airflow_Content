from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.bash import BashOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
import random

def download_file():
    return "even" if random.randint(1, 100) % 2 == 0 else "odd"

def even_number():
    return "I am even"

def odd_number():
    return "I am odd"

with DAG(dag_id="hybrid_dag", catchup=False, tags=["Hybrid"]) as dag:
    task1 = BashOperator(task_id="Starting_Task", bash_command="echo Starting")

    with TaskGroup("ETL_Pipeline") as etl:
        extract = BashOperator(task_id="Extract_Operation", bash_command="echo Extracting the Data")
        transform = BashOperator(task_id="Transforming_the_data", bash_command="echo Transform Data")
        load = BashOperator(task_id="Loading_Operation", bash_command="echo Loading")
        
        extract >> transform >> load

    branching = BranchPythonOperator(task_id="Check_number", python_callable=download_file)

    even = PythonOperator(task_id="even", python_callable=even_number)
    odd = PythonOperator(task_id="odd", python_callable=odd_number)

    task1 >> etl >> branching >> [even ,odd]   
    
