from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.get("/employees")
def get_employees():
    return "The employees"

if __name__ == '__main__':
    app.run()