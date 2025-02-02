# app.py
from flask import Flask, request, render_template, jsonify
from nlp import process_query
from database import get_employees_in_department, get_manager_of_department, get_employees_hired_after, get_total_salary_expense

app = Flask(__name__)

@app.route('/')
def home():
    """Render the HTML form."""
    return render_template('index.html')

@app.route('/query', methods=['GET'])
def handle_query():
    query = request.args.get('query').lower()

    # Extract department and date from the query using NLP
    department, hire_date = process_query(query)

    # Show employees in a department
    if "show me all employees in the" in query:
        if department:
            result, columns = get_employees_in_department(department)
            if result:
                # Convert the result to a list of dictionaries using the column names
                result_dicts = [dict(zip(columns, row)) for row in result]
                return jsonify(result_dicts)
            else:
                return jsonify({"message": f"No employees found in {department} department."}), 404
        else:
            return jsonify({"message": "Please specify a valid department."}), 400

    # Get manager of a department
    elif "who is the manager of the" in query:
        if department:
            manager = get_manager_of_department(department)
            if manager:
                return jsonify({"manager": manager})
            else:
                return jsonify({"message": f"No manager found for {department} department."}), 404
        else:
            return jsonify({"message": "Please specify a valid department."}), 400

    # List employees hired after a specific date
    elif "list all employees hired after" in query:
        if hire_date:
            result, columns = get_employees_hired_after(hire_date)
            if result:
                # Convert the result to a list of dictionaries using the column names
                result_dicts = [dict(zip(columns, row)) for row in result]
                return jsonify(result_dicts)
            else:
                return jsonify({"message": "No employees found hired after this date."}), 404
        else:
            return jsonify({"message": "Please specify a valid date."}), 400

    # Calculate the total salary expense for a department
    elif "what is the total salary expense for the" in query:
        if department:
            total_salary = get_total_salary_expense(department)
            if total_salary is not None:
                return jsonify({"total_salary": total_salary})
            else:
                return jsonify({"message": f"No salary data found for {department} department."}), 404
        else:
            return jsonify({"message": "Please specify a valid department."}), 400

    return jsonify({"message": "Sorry, I didn't understand that query."}), 400

if __name__ == '__main__':
    app.run(debug=True)
