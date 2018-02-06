from datetime import date, timedelta
import pathlib

from airflow import DAG
from airflow.utils import dates
from airflow.operators.python_operator import PythonOperator

from airflow_log_cleanup.tasks import cleanup_before_date

DEFAULT_ARGS = {
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=30),
    'start_date': dates.days_ago(1)
}


def create_dag(
    base_dir=pathlib.Path('~/airflow/logs').expanduser(),
    pattern=r'(?P<year>[0-9]{4})-(?P<month>[0-9]{2})-(?P<day>[0-9]{2})',
    days_ago=15,
    schedule='@daily',
    dag_args=DEFAULT_ARGS
):
    dag = DAG(
        dag_id='airflow_log_cleanup',
        default_args=DEFAULT_ARGS,
        schedule_interval=schedule
    )

    PythonOperator(
        task_id='log_cleanup',
        python_callable=cleanup_before_date,
        op_args=[base_dir, pattern, days_ago],
        dag=dag
    )

    return dag
