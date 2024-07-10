A simple Todo List application built with Flask python .
Features:
-Add tasks
-Delete tasks
-Mark tasks as completed
installation
Make sure you have the following installed:

- Python 3.x
- Flask

### Steps

1. Clone the repository:

```sh
git clone https://github.com/yourusername/todo-list.git
cd todo-list
Create a virtual environment:
sh
python -m venv .venv
Activate the virtual environment:
On Windows:
sh
.venv\Scripts\activate
On macOS/Linux:
sh
source .venv/bin/activate
Install the dependencies:
sh
pip install -r requirements.txt
Set up the database:
sh
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
Run the application:
sh
flask run
