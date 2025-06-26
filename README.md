# Oladapo_Omolaja_Credit_Direct_Coding_Assessment

Data Engineer Code Challenge

Using the public Employees sample database in MySQL[1], create a DAG to move data
from the employees table to bigquery.
There should also be 2 different dags which would have different logics.
The first dag should be a full load dag which moves all the data from the employees
table to bigquery while the second dag would be an incremental dag which would move
data daily and only contain changes that have happened in the past day.
On the gender column in the employees table, transform the values before they are
loaded into big query as below using a DBT model:
M to Male
F to Female
All codes should be on a public code repository hosted on Github and also create a
CI/CD pipeline to deliver and deploy new code changes to your Airflow environment as
new releases.

#
References:
[1] https://dev.mysql.com/doc/employee/en/
