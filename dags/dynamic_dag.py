from airflow import DAG
from airflow.operators.bash import BashOperator

use_cases = ["UC1", "UC2", "UC3", "UC4", "UC5"]

for uc in use_cases:
    dagid = f"dynamic_etl_pipeline_for_{uc}"

    with DAG(dag_id=dagid, catchup=False, tags=["Dynamic"]) as dag:
        extract = BashOperator(
            task_id=f"Extract_Task_for_{uc}", bash_command=f"echo Extract task for {uc}"
        )
        transform = BashOperator(
            task_id=f"Transform_Task_for_{uc}",
            bash_command=f"echo Transform task for {uc}",
        )
        load = BashOperator(
            task_id=f"Load_Task_for_{uc}", bash_command=f"echo Load task for {uc}"
        )

        extract >> transform >> load

        globals()[dagid] = dag
