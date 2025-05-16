from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.bash import BashOperator

with DAG(dag_id="task_grouping_dag",
        catchup=False,
        tags=["task_grouping"]) as dag:
    pre_flight_checks = BashOperator(task_id="pre_flight_checks", bash_command="echo Starting")

    with TaskGroup("ETL_Pipeline") as etl:
        extract = BashOperator(task_id="Extract_Operation", bash_command="echo Extracting the Data")
        transform = BashOperator(task_id="Transforming_the_data", bash_command="echo Transform Data")
        load = BashOperator(task_id="Loading_Operation", bash_command="echo Loading")
        
        extract >> transform >> load

    post_job_checks = BashOperator(task_id="post_job_checks", bash_command="echo Job is perfectly fine")

    pre_flight_checks >> etl >> post_job_checks