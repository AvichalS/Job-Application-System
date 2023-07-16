from flask import Flask, render_template, jsonify, request
from database import load_jobs, load_job, add_app

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job(id)
  if not job:
    return "Not found", 404
  return render_template('jobpage.html', job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job(id)
  return jsonify(job)


@app.route("/job/<id>/apply", methods=["post"])
def apply_to_job(id):
  data = request.form
  # return jsonify(data)
  job = load_job(id)
  add_app(id, data)
  return render_template('app_sub.html', application=data, job=job)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
