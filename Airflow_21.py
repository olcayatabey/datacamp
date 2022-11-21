 """__________________________________________________________________________
                     More PythonOperators
To continue implementing your workflow, you need to add another step to parse and save the changes of the downloaded file. 
The DAG process_sales_dag is defined and has the pull_file task already added.
In this case, the Python function is already defined for you, parse_file(inputfile, outputfile).

Note that often when implementing Airflow tasks, you won't necessarily understand the individual steps given to you. 
As long as you understand how to wrap the steps within Airflow's structure, you'll be able to implement a desired workflow.


Define the Python task to the variable parse_file_task with the id parse_file.
Add the parse_file(inputfile, outputfile) to the Operator.
Define the arguments to pass to the callable.
Add the task to the DAG.
"""

# Add another Python task
parse_file_task = PythonOperator(
    task_id='parse_file',
    # Set the function to call
    python_callable=parse_file,
    # Add the arguments
    op_kwargs={'inputfile':'latestsales.json', 'outputfile':'parsedfile.json'},
    # Add the DAG
    dag=process_sales_dag
)
   """__________________________________________________________________________   
  EmailOperator and dependencies
  
Now that you've successfully defined the PythonOperators for your workflow, 
your manager would like to receive a copy of the parsed JSON file via email when the workflow completes.
The previous tasks are still defined and the DAG process_sales_dag is configured.

Import the class to send emails.
Define the Operator and add the appropriate arguments (to, subject, files).
Set the task order so the tasks run sequentially (Pull the file, parse the file, then email your manager).
 ____________________"""
  # Import the Operator
from airflow.operators.email_operator import EmailOperator

# Define the task
email_manager_task = EmailOperator(
    task_id='email_manager',
    to='manager@datacamp.com',
    subject='Latest sales JSON',
    html_content='Attached is the latest sales JSON file as requested.',
    files='parsedfile.json',
    dag=process_sales_dag
)

# Set the order of tasks
pull_file_task >> parse_file_task >> email_manager_task
