# unit_testing_airflow_components
Sandbox to learn pytest and apply it to Airflow components

## Requirements 
- pytest
- airflow
## Set Up environment
```bash
python3 -m venv airflow_env                                                        
source airflow_venv
source airflow_env/bin/activate
pip install airflow
pip install pytest
```

## Run locally
airflow db init # run once
make run_unit_test
