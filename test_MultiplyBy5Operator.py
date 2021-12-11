from datetime import datetime
from airflow.models.dag import DAG
from airflow.models.taskinstance import TaskInstance
from MultiplyBy5Operator import MultiplyBy5Operator

def test_obj_creation():
    param = 10
    dag = DAG(dag_id='test_dag', start_date=datetime.now())
    operator = MultiplyBy5Operator(my_operator_param=param, dag=dag, task_id='MyCustomOperator')
    assert operator != None
    assert operator.operator_param == param

def test_execute_with_number():
    dag = DAG(dag_id='test_dag', start_date=datetime.now())
    task = MultiplyBy5Operator(my_operator_param=10, dag=dag, task_id='MyCustomOperator')
    result = task.execute(context=None)
    assert result == 50