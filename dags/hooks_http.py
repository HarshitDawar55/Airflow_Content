from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.operators.python import PythonOperator
import logging


def fetch_data():
    MyHook = HttpHook(http_conn_id="http_hooks", method="GET")
    response = MyHook.run(endpoint="posts/10")
    logging.warning(f"Response Received from the website is: {response.text}")


with DAG(dag_id="HOOK_HTTP", catchup=False, tags=["Hooks", "HTTP"]) as dag:
    task = PythonOperator(task_id="Executing_Hook", python_callable=fetch_data)
