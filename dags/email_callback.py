from airflow import DAG
from airflow.utils.email import send_email
from airflow.operators.python import PythonOperator
import random


def success_email_function(context):
    subject = "Alert from Airflow - The Dag is successful"
    html_body = "<h2>Task is Successful</h2>"

    send_email(
        to=[
            "trainingsbyharshitdawar@gmail.com",
            "temp.sidhari@gmail.com",
            "manishsngh804@gmail.com",
            "gaurav.joshi9890@gmail.com",
            "thakregaurav28@gmail.com",
            "gnanadurgasi1@gmail.com",
        ],
        subject=subject,
        html_content=html_body,
    )


def failure_email_function(context):
    subject = "Alert from Airflow - The Dag is unsuccessful"
    html_body = "<h2>Task is UnSuccessful</h2>"

    send_email(
        to=[
            "trainingsbyharshitdawar@gmail.com",
            "temp.sidhari@gmail.com",
            "manishsngh804@gmail.com",
            "gaurav.joshi9890@gmail.com",
            "thakregaurav28@gmail.com",
            "gnanadurgasi1@gmail.com",
        ],
        subject=subject,
        html_content=html_body,
    )


default_args = {
    "email_on_failure": True,
    "email_on_success": True,
    "email_on_retry": True,
    "retries": 1,
    "on_failure_callback": failure_email_function,
    "on_success_callback": success_email_function,
    "on_retry_callback": failure_email_function,
}


def event():
    if random.random() < 0.5:
        raise ValueError("Failed On Purpose for the simulation of email notification")
    return "Event Successful"


with DAG(
    dag_id="Email_through_callback",
    catchup=False,
    schedule="@daily",
    tags=["Email"],
    default_args=default_args,
) as dag:
    task = PythonOperator(task_id="Running_an_event", python_callable=event)
