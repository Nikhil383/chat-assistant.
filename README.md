# chat-assistant.
This is a simple chat assistant built using SpaCy, Flask, and SQLite. The chat assistant is designed to process natural language inputs, provide intelligent responses, and store chat data in a SQLite database for later retrieval.

Technologies Used
SpaCy: A powerful NLP (Natural Language Processing) library used for processing and understanding text.
Flask: A lightweight web framework for building the chat interface and API.
SQLite: A lightweight, serverless database to store user messages and chat data.
Features
Natural Language Understanding: Uses SpaCy to analyze and understand user input.
Chat Interface: Built using Flask, allowing users to interact with the assistant through a simple web interface.
Message Storage: Messages are saved in an SQLite database for future reference or analysis.
Setup
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
Pip (Python package installer)
Installation
Clone the repository to your local machine:

git clone https://github.com/Nikhil383/chat-assistant.git
cd chat-assistant
Install the required Python packages


pip install -r requirements.txt
Download the necessary SpaCy language model:


python -m spacy download en_core_web_sm
Set up the SQLite database:


python init_db.py
Running the Application
Start the Flask app:


python app.py
Open your web browser and go to http://127.0.0.1:5000/ to interact with the chat assistant.
