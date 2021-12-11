from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def print_hello():
    return 'Hello world from first Airflow DAG!'

dag = DAG('hello_world', 
        description='Hello World DAG',
        schedule_interval='0 12 * * *',
        start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)
hello_operator2 = PythonOperator(task_id='hello_task2', python_callable=print_hello, dag=dag)

hello_operator2
hello_operator

for t in dag.tasks:
    print(t)
    print(type(t))