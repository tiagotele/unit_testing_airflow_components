from datetime import datetime, timezone
from sample_dag import dag


def test_dag_Structure():
    assert dag.description == 'Hello World DAG'
    assert dag.schedule_interval == '0 12 * * *'
    assert dag.start_date == datetime(2017, 3, 20).replace(tzinfo=timezone.utc)
    assert dag.catchup == False
    assert len(dag.tasks) == 2
    assert set(map(lambda task:  task.task_id, dag.tasks)
               ) == set(['hello_task2', 'hello_task1'])


def test_dependencies_of_task1():
    t1 = dag.get_task('hello_task1')

    upstream_tasks_ids = list(map(lambda task: task.task_id, t1.upstream_list))
    downstream_tasks_ids = list(
        map(lambda task: task.task_id, t1.downstream_list))
    assert upstream_tasks_ids == []
    assert downstream_tasks_ids == ['hello_task2']


def test_dependencies_of_task2():
    t2 = dag.get_task('hello_task2')

    upstream_tasks_ids = list(map(lambda task: task.task_id, t2.upstream_list))
    downstream_tasks_ids = list(
        map(lambda task: task.task_id, t2.downstream_list))
    assert upstream_tasks_ids == ['hello_task1']
    assert downstream_tasks_ids == []
