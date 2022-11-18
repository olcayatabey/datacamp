from airflow.models import DAG
default_args = {
  'owner': 'jdoe',
  'start_date': '2019-01-01'
}
dag = DAG( dag_id="etl_update", default_args=default_args )

"""----------- ex 1------------"""

Import the BashOperator object.
Define a BashOperator called cleanup with the task_id of cleanup_task.
Use the command cleanup.sh.
Add the operator to the DAG
"""--------- sol 1-----------------"""

# Import the BashOperator
from airflow.operators.bash_operator import BashOperator

# Define the BashOperator 
cleanup = BashOperator(
    task_id='cleanup_task',
    # Define the bash_command
    bash_command='cleanup.sh',
    # Add the task to the dag
    dag=analytics_dag
)
"""----------------------------"""
"""--------    ex2     ------"""
Define a BashOperator called consolidate, to run consolidate_data.sh with a task_id of consolidate_task.
Add a final BashOperator called push_data, running push_data.sh and a task_id of pushdata_task.
"""-----------sol 2-------------"""

# Define a second operator to run the `consolidate_data.sh` script
consolidate = BashOperator(
    task_id='consolidate_task',
    bash_command='consolidate_data.sh',
    dag=analytics_dag)

# Define a final operator to execute the `push_data.sh` script
push_data = BashOperator(
    task_id='pushdata_task',
    bash_command='push_data.sh',
    dag=analytics_dag)
