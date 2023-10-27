CREATE DATABASE employment;

USE employment;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    SSN VARCHAR(9) UNIQUE NOT NULL
);

CREATE TABLE contact_info (
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT UNIQUE,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    address TEXT,
    phone_number VARCHAR(15),
    email VARCHAR(100),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
