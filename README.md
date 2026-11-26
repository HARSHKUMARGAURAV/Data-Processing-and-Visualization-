Student Scores API & Chart

A small Python project with two parts:

student_api.py: a Flask REST API that serves a list of students and their test scores.
student_scores.py: a client script that fetches the scores from the API, prints them, calculates the average, and shows a bar chart.
Features
REST endpoint returning student data as JSON
Fetches data with requests (with timeout and error handling)
Calculates the average score
Displays a bar chart of scores using Matplotlib
Project Structure
.
├── student_api.py       # Flask API server
├── student_scores.py    # Client: fetch, average, chart
└── README.md
Requirements
Python 3.8+
Flask
requests
Matplotlib
Installation
bash
# (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# Install dependencies
pip install flask requests matplotlib
Usage

Step 1: Start the API server (in one terminal):

bash
python student_api.py

The server runs at http://127.0.0.1:5000.

Step 2: Run the client (in a second terminal):

bash
python student_scores.py

The script prints each student's score, the average score, and opens a bar chart window.

API Reference
GET /students

Returns all students and their scores.

URL: http://127.0.0.1:5000/students

Example response:

json
[
  {"name": "rahul", "score": 85},
  {"name": "priya", "score": 90},
  {"name": "Amit", "score": 75},
  {"name": "Sneha", "score": 95},
  {"name": "Rohit", "score": 80}
]
Example Output
Student test Score
--------------------
rahul:85
priya:90
Amit:75
Sneha:95
Rohit:80

Average Score:85.00
Error Handling

The client catches requests.RequestException, ValueError, KeyError and TypeError and prints a readable error message, for example when the API server is not running.

Possible Improvements
Load student data from a database or file instead of a hard-coded list
Add endpoints to create, update and delete students (POST, PUT, DELETE)
Save the chart as an image instead of only displaying it
Add unit tests
