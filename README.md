# unit_testing_airflow_components
Sandbox to learn pytest and apply it to Airflow components

## Requirements 
- pytest
- airflow
## Set Up environment
```bash
python3 -m venv .venv                                                        
source .venv/bin/activate
pip install "apache-airflow[celery]==2.7.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt"
pip install pytest
```

## Run locally
airflow db init # run once
make run_unit_test
