from datetime import date, timedelta
import pathlib

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def create_dag(
    base_folder=pathlib.Path('~/aiflow/logs').expanduser(),
    pattern='{day:%Y-%m-%d}*',
    days_ago=15
):
    today = date.today()
