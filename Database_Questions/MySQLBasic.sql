-------------------------------------------------------------------------------------------------------------
-- MySQL crash course!
-- MySQL = an open-source relational database management system (data stored in tables and rows "records")
--      Links information from mult. tables using "primary and foreign keys" (assigned to row of data)
--      Examples in industry: Microsoft SQL Server, SQLite, MySQL. InnoDB is the default MySQL storage engine
--      Ex: Every employee has a primary key named EID, a Sale points to the EID of the employee that made
--      that sale. Hence, it's a foreign key (no orphans!).

-- Why: Accurate, consistent data. Constraints prevent a related record from being deleted without first 
--      deleting the primary record in the main table.
--      CASCADE DELETE = deleting all related records referencing a primary key that is also being del.

-- NoSQL = Non-relational DBMS. There are no tables/rows etc. Storage model is optim. for spec. requirements
-- of the type of data being stored. Uses Object-relational-mapping (ORM) instead of SQL, ex: Java, PHP.
--      Examples in industry: MongoDB, Apache Cassandra
-- Why: Large amts of data w/out needing rigid structure, document-oriented, flexible data model, scalable.
--      "Document Data Store": string field + object data values
--          JSON documents, can be encoded into XML, YAML, etc.
--          Pros: Does not require all documents to maintain identical data structures!
--      Key-Value: least complicated NoSQL database. Just keys and their values.

-- Examples of MySQL queries --------------------------------------------------------------------------------
-- CREATE TABLES
-- Create a unique table 'countries', where the columns are: (see below)
-- decimal(M, D) where M = maximum # digits TOTAL and D = # of those digits to the right of decimal point
--      Ex: my_column DECIMAL(6,4) can handle values -99.9999 to 99.9999
CREATE TABLE IF NOT EXISTS countries( 
    COUNTRY_ID varchar(2), -- COUNTRY_ID is a variable character data w/ 2 chars max
    COUNTRY_NAME varchar(40),
    CHECK(COUNTRY_NAME IN('Italy','India','China')), -- No countries except Italy, India, China allowed
    REGION_ID decimal(10,0) -- REGION_ID (whole number max 10 digits total)
);

-- Create a duplicate copy of COUNTRIES table including structure and data by name DUP_COUNTRIES.
CREATE TABLE IF NOT EXISTS dup_countries
AS SELECT * 
FROM countries;

-- Create a unique table named jobs with columns job_id, job_title, min_salary, max_salary.
-- Also, make sure no job has a maximum salary over $105,000.
CREATE TABLE IF NOT EXISTS jobs(
    JOB_ID varchar(10) NOT NULL, -- NOT NULL = required
    JOB_TITLE varchar(35) NOT NULL,
    MIN_SALARY decimal(6,0),
    MAX_SALARY decimal(6,0)
    CHECK(MAX_SALARY <= 105000) -- CHECK constraint allows only certain values for this column.
);

-- Create a table `job_history` including columns employee_id, 
-- starting_date, ending_date, job_id and department_id.
-- Make sure that `employee_id` column does not contain any duplicate values.
-- `job_id` contains only values which exist in the jobs table.
CREATE TABLE job_history(
    EMPLOYEE_ID decimal(6,0) NOT NULL PRIMARY KEY,
    STARTING_DATE date NOT NULL,
    ENDING_DATE date NOT NULL,
    JOB_ID varchar(10) NOT NULL, -- the FOREIGN KEY
    DEPARTMENT_ID decimal(4,0) DEFAULT NULL,
    FOREIGN KEY (job_id) 
        REFERENCES jobs(job_id) -- ref primary key, must declare this at the bottom
        ON DELETE SET NULL -- Set foreign key column values to NULL when the corresponding record
                           -- in the parent table(jobs) is deleted
        ON UPDATE SET NULL -- When rows in parent table(jobs) are updated.
);

-- SIMPLE SELECTIONS
-- Returns all company IDs from table "company" if they have an employee population > 10,000
-- Order them by IDs ascending
SELECT ID 
FROM company
WHERE EMPLOYEES > 10000
ORDER BY ID; -- automatically ordered by ASC, DESC is the opposite

-- Get all employee info, sales info, customer info, (from mult. tables) 
-- where the EmployeeID is 1.
SELECT * FROM employees
JOIN Sales ON Employees.EmployeeId = SALES.EmployeeId
JOIN Customers ON Customers.CustomerId = SALES.CustomerId
WHERE EmployeeId = 1;

-- MORE JOINS --> Diagram: https://tinyurl.com/ya9tekw8
-- Get the addresses (location_id, street_address, city, state_province, country_name) of all departments
--      Given `locations` and `countries` tables, where `country_id column` in both.
SELECT location_id, street_address, city, state_province, country_name
FROM locations
NATURAL JOIN countries; -- NATURAL JOIN = implicit join based on the common columns in the two tables

-- Find the (first_name, last name), department ID and department name of all employees, given tables
-- `employees` and `departments` that share DEPARTMENT_ID
SELECT FIRST_NAME, LAST_NAME, DEPARTMENT_ID, DEPARTMENT_NAME 
FROM employees
JOIN departments USING(department_id); -- USING is like ON, but ON is more general (ON column, condit., etc)
    -- USING: both tables share a column of the exact same name on which they join
    -- equivalent line: INNER JOIN departments ON employees.department_id = departments.department_id;

-- Find the (first_name, last_name), job ID, department ID and dep. name of the employees 
-- who work in London. Given tables `employees`, `locations` and `departments`.
SELECT e.FIRST_NAME, e.LAST_NAME, e.JOB_ID, e.DEPARTMENT_ID, d.DEPARTMENT_NAME
FROM employees e
JOIN departments d 
    ON (e.DEPARTMENT_ID = d.DEPARTMENT_ID)
JOIN locations l
    ON (l.LOCATION_ID = d.LOCATION_ID)
WHERE LOWER(l.CITY) = 'London';
