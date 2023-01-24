import os

from employees_db import db
from models import EmployeeModel
from schemas import EmployeeSchema

from dotenv import load_dotenv
from flask import Flask


app = Flask(__name__)
load_dotenv()
db_path = os.path.join(os.path.dirname(__file__), 'employees.db')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(db_path)
db.init_app(app)

@app.get("/employees")
def get_employees():
    employees = EmployeeModel.query.all()
    return EmployeeSchema(many=True).dump(employees)

if __name__ == '__main__':
    app.run()