from flask import Flask
app = Flask(__name__)

@app.route("/chaos")
def hello():
    return "Hello, Welcome to Azure Chaos Engineering!"
