from airflow import DAG

# from airflow.utils.email import send_email
from airflow.operators.python import PythonOperator
from airflow.providers.smtp.operators.smtp import EmailOperator
import random
from airflow.operators.empty import EmptyOperator


def event():
    if random.random() < 0.5:
        raise ValueError("Error on Purpose for Email Operator showcase")
    return "Event Succesful"


default_args = {"retries": 0, "email_on_failure": True, "email_on_success": True}

with DAG(
    dag_id="EmailOperator_Showcase",
    catchup=False,
    tags=["Email"],
    default_args=default_args,
) as dag:
    empty_task = EmptyOperator(task_id="Empty_Task")
    python_task = PythonOperator(task_id="Python_Task", python_callable=event)
    email_task = EmailOperator(
        task_id="Email_Task",
        to=[
            "trainingsbyharshitdawar@gmail.com",
            "temp.sidhari@gmail.com",
            "manishsngh804@gmail.com",
            "gaurav.joshi9890@gmail.com",
            "thakregaurav28@gmail.com",
            "gnanadurgasi1@gmail.com",
        ],
        subject="Alert By Airflow Email Operator",
        html_content="Email Notification by Email Operator of Airflow",
        conn_id="Email_Notification",
        trigger_rule="all_success",
    )

    empty_task >> python_task >> email_task
