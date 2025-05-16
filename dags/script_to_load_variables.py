import json
from airflow.models import Variable

# Providing the Variables to Airflow Cluster
with open("./myvariables.json", "r") as f:
    variables = json.load(f)

for k,v in variables.items():
    Variable.set(k, v)