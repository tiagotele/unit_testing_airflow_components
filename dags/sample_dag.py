from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from dags.multiply_by_5operator import MultiplyBy5Operator
from datetime import datetime, timedelta


def print_hello():
    return 'Hello world from first Airflow DAG!'


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}
dag = DAG('hello_world',
          description='Hello World DAG',
          schedule='0 12 * * *',
          start_date=datetime(2017, 3, 20),
          default_args=default_args,
          catchup=False)

task1 = PythonOperator(task_id='hello_task1',
                       python_callable=print_hello, dag=dag)
task2 = PythonOperator(task_id='hello_task2',
                       python_callable=print_hello, dag=dag)

multiplyby5_operator = MultiplyBy5Operator(
    task_id='multiplyby5_task', my_operator_param='my_operator_param', dag=dag)

task1 >> task2 >> multiplyby5_operator
