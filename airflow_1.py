from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

defaults_args ={
  'owner'='olcay',
  'start_date=datetime (20,11,18),
  'retries'=1}
  
codependency_dag =DAG('codependency',default=args=default_args)

task1= BashOperator(task_id='first_task',
                    bash_command='echo 1',
                    dag=codependecy_dag)
 task2= BashOperator(task_id='second_task',
                    bash_command='echo 2',
                    dag=codependecy_dag)
task3= BashOperator(task_id='third_task',
                    bash_command='echo 3',
                    dag=codependecy_dag)
                    
 #task1 must run before task2  which must run task3
 
 task1 >>task2
 task2 >> task3
 task3 >> task1
  
