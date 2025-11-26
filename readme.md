CLI To-Do List Application
A simple command-line to-do list application built with Python.

Features
Add tasks

View all tasks

Delete tasks

Exit application

Prerequisites
Python 3.11+

pip (Python package manager)

Docker (optional)

Installation
Clone the repository:

bash
git clone https://github.com/puskara123/CICDSoftwareEngineering.git
cd CICDSoftwareEngineering
Install dependencies:

bash
pip install -r requirements.txt
Running Locally
bash
python app.py
Running with Docker
bash
docker build -t my-todolist:latest .
docker run -it my-todolist:latest
Commands
add <task> - Add a new task

list - Show all tasks

delete <number> - Delete a task by number

exit - Exit the application

Testing
Run the tests with:

bash
pytest test_app.py -v
Author
Pushkar Kulkarni / IMT2023087