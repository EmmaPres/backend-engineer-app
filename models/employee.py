from employees_db import db


# Represents an Employee in the "employees" database
class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String, nullable=False)