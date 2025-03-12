from flask import Flask, render_template


app = Flask(__name__)


@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def home():
    return "Hello"


@app.route("/welcome/user_name", methods=["get"])
def welcome(user_name: str = ""):
    return f"Hello {user_name}"


@app.route("/students/list")
def students_list():
    student_list = [
        "Nugo", "Giorgi", "Mariami",
        "Nugo", "Giorgi", "Mariami",
        "Nugo", "Giorgi", "Mariami",
    ]

    return render_template("students.html", students=student_list)


@app.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "John Doe", "email": "johndoe@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "janesmith@example.com"},
        {"id": 3, "name": "Alice Johnson", "email": "alicejohnson@example.com"},
        {"id": 4, "name": "Bob Brown", "email": "bobbrown@example.com"},
        {"id": 5, "name": "Charlie Davis", "email": "charliedavis@example.com"},
        {"id": 6, "name": "David Wilson", "email": "davidwilson@example.com"},
        {"id": 7, "name": "Eve Taylor", "email": "evetaylor@example.com"},
        {"id": 8, "name": "Frank Moore", "email": "frankmoore@example.com"},
        {"id": 9, "name": "Grace Lee", "email": "gracelee@example.com"},
        {"id": 10, "name": "Hannah Clark", "email": "hannahclark@example.com"}
    ]
    return render_template("users.html", user_list=users)