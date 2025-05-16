from airflow import DAG
from airflow.sensors.filesystem import FileSensor
from airflow.operators.bash import BashOperator

with DAG(dag_id="FileSensor_DAG", catchup=False, tags=["Sensor", "FileSensor"]) as dag:
    waiting_for_a_file1 = FileSensor(
        task_id="Waiting_For_A_File1", filepath="data1.csv", poke_interval=10, timeout=500
    )
    waiting_for_a_file2 = FileSensor(
        task_id="Waiting_For_A_File2", filepath="data2.csv", poke_interval=10, timeout=500
    )
    final_step = BashOperator(
        task_id="Final_Step", bash_command="echo Everything Completed"
    )

    [waiting_for_a_file1, waiting_for_a_file2] >> final_step