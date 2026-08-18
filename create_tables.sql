CREATE TABLE customers(
customer_id STRING,
customer_name STRING,
city STRING,
phone STRING
);

CREATE TABLE accounts(
account_id STRING,
customer_id STRING,
account_type STRING,
balance DOUBLE
);

CREATE TABLE loans(
loan_id STRING,
customer_id STRING,
loan_amount DOUBLE,
status STRING
);

CREATE TABLE transactions(
transaction_id STRING,
account_id STRING,
amount DOUBLE,
transaction_type STRING
);

CREATE TABLE payments(
payment_id STRING,
loan_id STRING,
amount DOUBLE,
payment_date DATE
);
