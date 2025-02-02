# queries.py

import sqlite3

def get_db_connection():
    """Connects to the SQLite database."""
    conn = sqlite3.connect('company.db')
    conn.row_factory = sqlite3.Row  # For easy dictionary-like access to rows
    return conn

def execute_query(query, params=()):
    """Executes an SQL query and fetches the result."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

def get_employees_in_department(department):
    """Fetches employees in the specified department."""
    return execute_query('SELECT * FROM Employees WHERE Department = ?', (department,))

def get_manager_of_department(department):
    """Fetches the manager of the specified department."""
    result = execute_query('SELECT Manager FROM Departments WHERE Name = ?', (department,))
    return result[0]['Manager'] if result else None

def get_employees_hired_after(hire_date):
    """Fetches employees hired after the specified date."""
    return execute_query('SELECT * FROM Employees WHERE Hire_Date > ?', (hire_date,))

def get_total_salary_expense(department):
    """Calculates the total salary expense for the specified department."""
    result = execute_query('SELECT SUM(Salary) AS TotalSalary FROM Employees WHERE Department = ?', (department,))
    return result[0]['TotalSalary'] if result else None
