
# IDS706-Week6-ComplexSQL-SQLite

This repository is part of the Week 6 mini-project for IDS706. It illustrates the implementation of complex SQL queries involving joins, aggregation, and sorting using Python and SQLite.

## 1 Interaction with SQLite Database
In this assignment, a Python script is used to interact with an SQLite database. It covers the creation of tables, insertion of data, as well as performing complex SQL operations that showcase joins, aggregation, and sorting.

## 2 How to Run
1. Make sure Python is installed.
2. Execute the script using `python complex_sql.py`. 
3. For saving outputs, use `python complex_sql.py > output_log.txt`.
4. Check the results.

## 3 Script Breakdown
1. **Connection Establishment**:
    A connection is made to an SQLite database, named `jobsDB.db`. If absent, it's generated.
    
2. **CRUD Operations**:
    Detailed functions for creating, reading, updating, and deleting data in both `jobs` and `job_applicants` tables.

3. **Complex SQL Query**:
    An intricate query combines both tables, highlighting aggregation, joins, and sorting.

## 4 Assignment Requirements
This project fulfills the Week 6 assignment requirements for IDS706:
- **Complex SQL Query Design**: The project implements SQL queries showcasing joins, aggregation, and sorting.
- **Explanation & Documentation**: This README, along with in-script comments, provides a comprehensive breakdown of the code's functionality.
