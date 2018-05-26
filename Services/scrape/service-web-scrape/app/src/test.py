from flask import Flask
app = Flash(__name__)

@app.route("/")
def hell():
    return "Hello World"