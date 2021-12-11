from sample_dag import dag
import pytest
from datetime import datetime, timezone
import pytz

def test_dag_Structure():


    assert dag.description == 'Hello World DAG'
    assert dag.schedule_interval == '0 12 * * *'
    assert dag.start_date == datetime(2017, 3, 20).replace(tzinfo=timezone.utc)
    assert dag.catchup == False
    