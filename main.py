from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return "Hello!"

def print_world():
    return "World!"


a = print_world()
print(a)
