# nlp.py

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def process_query(query):
    """
    This function processes the user's query to extract the department and hire_date.
    It uses SpaCy for Named Entity Recognition (NER) and simple keyword matching.

    Args:
        query (str): The user query (e.g., "Show me all employees in the Sales department").

    Returns:
        tuple: (department, hire_date)
    """
    department = None
    hire_date = None
    
    # Process the query with SpaCy NLP model
    doc = nlp(query)
    
    # Check for department keywords (Sales, Engineering, Marketing, etc.)
    departments = ['sales', 'engineering', 'marketing']
    
    # Try to find department by matching entity labels or keywords
    for token in doc:
        # If token matches a department keyword, store the department name
        if token.text.lower() in departments:
            department = token.text.lower()

    # Extract hire_date if mentioned in the query (e.g., "hired after 2022-01-01")
    if "hired after" in query:
        hire_date = query.split("hired after")[1].strip()

    return department, hire_date
