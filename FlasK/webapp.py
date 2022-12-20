from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

@app.route("/myapp")
def index():
    return "Hello work"

if __name__ == "__main__":
    app.run(debug=True)
