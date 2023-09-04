-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id varchar,
	company_name varchar,
	contact_name varchar

)

CREATE TABLE employees
(
	employee_id varchar,
	first_name varchar,
	last_name varchar,
	title varchar,
	birth_date date,
	notes text

)

CREATE TABLE orders
(
	order_id int NOT NULL,
	customer_id varchar (10),
	employee_id int2,
	order_date date,
	ship_city varchar
)
