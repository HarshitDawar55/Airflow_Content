from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json


def extract():
    extractionHook = HttpHook(http_conn_id="http_hooks", method="GET")
    response = extractionHook.run("posts/10")
    return response.text


def load_in_DB(**context):
    extracted_data = json.loads(context["ti"].xcom_pull(task_ids="Extraction_Task"))
    db_hook = PostgresHook(postgres_conn_id="postgres_integration")
    query = f"insert into airflow_integration_training (id, title, body) values ({extracted_data['id']}, '{extracted_data['title']}', '{extracted_data['body']}');"
    db_hook.run(query)


with DAG(
    dag_id="Integration_Pipeline", catchup=False, tags=["Pipeline", "Hooks", "DB"]
) as dag:
    extraction_task = PythonOperator(task_id="Extraction_Task", python_callable=extract)
    load_task = PythonOperator(task_id="Load_Data", python_callable=load_in_DB)

    extraction_task >> load_task
