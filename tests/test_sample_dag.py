import pytest

from airflow.models import DagBag
from datetime import datetime, timezone


@pytest.fixture()
def dagbag():
    return DagBag(dag_folder='dags/', include_examples=False)


def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="hello_world")
    assert dagbag.import_errors == {}
    assert dag is not None


def test_dag_count(dagbag):
    dag = dagbag.get_dag(dag_id="hello_world")
    assert len(dag.tasks) == 3


def test_contain_tasks(dagbag):
    """Check task contains in hello_world dag"""
    dag_id = 'hello_world'
    dag = dagbag.get_dag(dag_id)
    tasks = dag.tasks
    task_ids = list(map(lambda task: task.task_id, tasks))
    assert sorted(task_ids) == ['hello_task1',
                                'hello_task2', 'multiplyby5_task']


def test_dag_structure(dagbag):
    dag_id = 'hello_world'
    dag = dagbag.get_dag(dag_id)
    assert dag.description == 'Hello World DAG'
    assert dag.schedule_interval == '0 12 * * *'
    assert dag.start_date == datetime(2017, 3, 20).replace(tzinfo=timezone.utc)
    assert dag.catchup == False
    assert len(dag.tasks) == 3
    assert set(map(lambda task:  task.task_id, dag.tasks)
               ) == set(['hello_task2', 'hello_task1', 'multiplyby5_task'])


def test_dependencies_of_task1(dagbag):
    dag_id = 'hello_world'
    dag = dagbag.get_dag(dag_id)
    t1 = dag.get_task('hello_task1')

    upstream_tasks_ids = list(map(lambda task: task.task_id, t1.upstream_list))
    downstream_tasks_ids = list(
        map(lambda task: task.task_id, t1.downstream_list))
    assert upstream_tasks_ids == []
    assert downstream_tasks_ids == ['hello_task2']


def test_dependencies_of_task2(dagbag):
    dag_id = 'hello_world'
    dag = dagbag.get_dag(dag_id)
    t2 = dag.get_task('hello_task2')

    upstream_tasks_ids = list(map(lambda task: task.task_id, t2.upstream_list))
    downstream_tasks_ids = list(
        map(lambda task: task.task_id, t2.downstream_list))
    assert upstream_tasks_ids == ['hello_task1']
    assert downstream_tasks_ids == ['multiplyby5_task']
