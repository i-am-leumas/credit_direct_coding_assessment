-- employees_model.sql

SELECT
    employee_id,
    first_name,
    last_name,
    CASE
        WHEN gender = 'M' THEN 'Male'
        WHEN gender = 'F' THEN 'Female'
        ELSE gender
    END AS gender,
    hire_date,
    last_update
FROM {{ source('employees') }}
