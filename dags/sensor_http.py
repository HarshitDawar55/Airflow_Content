from airflow import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="HTTP_SENSOR_DAG", catchup=False, schedule=None, tags=["Sensor", "HTTP"]
) as dag:
    task = HttpSensor(
        task_id="Waiting_For_API_Availability",
        http_conn_id="http_sensor",
        endpoint="posts/10",
        poke_interval=10,
        timeout=20,
    )
    task2 = EmptyOperator(task_id="Empty_Operator")

    task >> task2
