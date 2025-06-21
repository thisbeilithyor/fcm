from flask import Flask

app = Flask(__name__)

@app.route("/hi")
def calling():
    return {'message': "hi"}

def calculate_sum(a, b):
    return a + b