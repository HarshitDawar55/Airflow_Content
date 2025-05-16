from airflow import DAG
from airflow.operators.bash import BashOperator


# Way 1 to define the DAG using 'with' keyword
with DAG(
    dag_id="Airflow_Training_Dag_Day_3",
    description="This is a sample DAG",
    tags=["introduction"],
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id="Printing_Hello_to_the_World",
        bash_command='echo "Hello World"'
    )

    task2 = BashOperator(
        task_id="Printing_Second_Task",
        bash_command='echo "I am second task"'
    )

    task3 = BashOperator(
        task_id="Task_3",
        bash_command='echo "I am third task"'
    )

    task1.set_downstream([task2, task3])
