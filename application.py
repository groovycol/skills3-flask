from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""
  
    return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Renders an application form page"""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def application():
    """Renders a page confirming the application submission"""

    fname = request.form.get("first-name")
    lname = request.form.get("last-name")
    salary_req = request.form.get("salary")
    job_wanted = request.form.get("job")

    return render_template("application-response.html", 
                            fname=fname,
                            lname=lname,
                            salary_req=salary_req,
                            job_wanted=job_wanted)


if __name__ == "__main__":
    app.run(debug=True)
