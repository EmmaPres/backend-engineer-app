import os

from employees_db import db
from models import EmployeeModel
from schemas import EmployeeSchema

from dotenv import load_dotenv
from flask import Flask
from sqlalchemy.exc import OperationalError

# Create the Flask app.
app = Flask(__name__)
# Load environment variables
load_dotenv()
# Get the path to the employees db.
db_path = os.path.join(os.path.dirname(__file__), 'employees.db')
# Configure the SQLite database.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(db_path)
# Initialize the app with the extension.
db.init_app(app)

@app.get("/employees")
def get_employees():
    try:
        # Get all the employees in the database
        employees = EmployeeModel.query.all()
    except OperationalError as err:
        # Return error message if table does not exist.
        return {"message": str(err.orig)}, 500

    # Return all the serialized employees (id and gender).
    return EmployeeSchema(many=True).dump(employees)

if __name__ == '__main__':
    app.run()