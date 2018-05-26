from flask import Flask
app = Flask(__name__)


# Run Service: FLASK_APP=testService.py flask run
@app.route("/")
def hell():
    return "Hello World"
    