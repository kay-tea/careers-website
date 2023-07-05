from flask import Flask, render_template, jsonify
app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "India",
    "salary": "10000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "India",
  },
  {
    "id": 3,
    "title": "Project Manager",
    "location": "Remote",
    "salary": "12000"
  },
  {
    "id": 4,
    "title": "Frontend Engineer",
    "location": "America",
    "salary": "15000"
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Katies")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)