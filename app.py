from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'New York',
        'salary': '$100,000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'San Francisco',
        'salary': '$120,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Delht India'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francusco USA',
        'salary': '$15,000,000'
    },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
