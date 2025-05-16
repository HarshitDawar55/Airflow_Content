from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule

with DAG(dag_id="Triggering_Rule_Example", catchup=False, tags=["Trigger"]) as dag:
    startingpoint = EmptyOperator(task_id="StartingPoint")
    task1 = BashOperator(task_id="task1", bash_command="echo I am Task 1")
    task2 = BashOperator(task_id="task2", bash_command="echo I am Task 2")
    task3 = BashOperator(task_id="task3", bash_command="echo I am Task 3")
    task4 = BashOperator(task_id="task4", bash_command="echo I am Task 4")
    task5 = BashOperator(task_id="task5", bash_command="echo I am Task 5")
    task6 = BashOperator(task_id="task6", bash_command="echo I am Task 6")
    task7 = BashOperator(task_id="task7", bash_command="echo I am Task 7")
    task8 = BashOperator(task_id="task8", bash_command="echo I am Task 8")
    task9 = BashOperator(task_id="task9", bash_command="echo I am Task 9")
    task10 = BashOperator(task_id="task10", bash_command="echo I am Task 10")
    endingpoint = EmptyOperator(
        task_id="Completed", trigger_rule=TriggerRule.ALL_SUCCESS
    )
    endingpoint_For_Failed = EmptyOperator(
        task_id="Completed_For_Failed_Tasks", trigger_rule=TriggerRule.ALL_FAILED
    )
    endingpoint_For_Skipped = EmptyOperator(
        task_id="Completed_For_Skipped_Tasks", trigger_rule=TriggerRule.ALL_SKIPPED
    )


    #startingpoint >> [task1, task2] >> task3 >> [task4, task5] >> task6 >> task7 >> task8 >> task9 >> task10 >> [endingpoint, endingpoint_For_Failed, endingpoint_For_Skipped]

    startingpoint >> [task1, task2, task3, task4, task5, task6, task7, task8, task9] >> task10 >> [endingpoint, endingpoint_For_Failed, endingpoint_For_Skipped]

