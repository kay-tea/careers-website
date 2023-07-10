from flask import Flask, render_template, jsonify, request
from database import load_all_jobs_from_db, load_single_job_from_db, add_application_to_db
app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs_list = load_all_jobs_from_db()
  return render_template('home.html', jobs=jobs_list)

@app.route("/jobs/<id>")
def show_job(id):
  job_list = load_single_job_from_db(id)
  if not job_list:
    return "Not Found", 404
  return render_template('jobpage.html', job=job_list)

@app.route("/jobs/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  job = load_single_job_from_db(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', application=data, job=job)

@app.route("/api/jobs/<id>")
def show_job_api(id):
  job = load_single_job_from_db(id)
  return jsonify(job)

@app.route("/api/jobs")
def list_jobs():
  jobs_list = load_all_jobs_from_db()
  return jsonify(jobs_list)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)