# database.py
import sqlite3

# Connect to the SQLite database
def connect_db():
    return sqlite3.connect('company.db')

# Fetch employees in a given department
def get_employees_in_department(department):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''SELECT * FROM Employees WHERE Department = ?'''
    cursor.execute(query, (department,))
    result = cursor.fetchall()
    conn.close()
    return result

# Fetch manager of a given department
def get_manager_of_department(department):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''SELECT Manager FROM Departments WHERE Name = ?'''
    cursor.execute(query, (department,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Fetch employees hired after a specific date
def get_employees_hired_after(date):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''SELECT * FROM Employees WHERE Hire_Date > ?'''
    cursor.execute(query, (date,))
    result = cursor.fetchall()
    conn.close()
    return result

# Fetch total salary expense for a department
def get_total_salary_expense(department):
    conn = connect_db()
    cursor = conn.cursor()
    query = '''SELECT SUM(Salary) FROM Employees WHERE Department = ?'''
    cursor.execute(query, (department,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0
