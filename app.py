from flask import Flask, render_template


app = Flask(__name__)


@app.route("/home", methods=["GET"])
@app.route("/", methods=["GET"])
def home():
    return "Hello"


@app.route("/welcome/<user_name>", methods=["get"])
def welcome(user_name: str):
    return f"Hello {user_name}"


@app.route("/students/list")
def students_list():
    student_list = [
        "Nugo", "Giorgi", "Mariami",
        "Nugo", "Giorgi", "Mariami",
        "Nugo", "Giorgi", "Mariami",
    ]
    return render_template("students.html", student_list=student_list)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
