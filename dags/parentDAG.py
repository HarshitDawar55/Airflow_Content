from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(dag_id="Parent_DAG", catchup=False, tags=["Parent_DAG"], schedule="@daily") as dag:
    start = EmptyOperator(task_id="Starting_Point")
    intermediate = BashOperator(
        task_id="Intermediate_Task",
        bash_command="echo I will be responsible for the processing",
    )
    heavy = TriggerDagRunOperator(
        task_id="Triggering_Heavy_DAG",
        trigger_dag_id="Child_DAG",
        wait_for_completion=False,
        conf={"additional_data": "Triggered from the Parent DAG"},
    )
    post_processing = BashOperator(
        task_id="Post_Processing_Task",
        bash_command="echo I will be responsible for the post processing",
    )
    end = EmptyOperator(task_id="DAG_Completed")

    start >> intermediate >> heavy >> post_processing >> end
