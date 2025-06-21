from flask import Flask
""" python module for setting up the api endpoint """

app = Flask(__name__)


@app.route("/hi")
def calling():
    """ This method sends response via json to the frontend """
    return {'message': "hi"}


def calculate_sum(a, b):
    """ This method calculates the sum of two numbers and returns the value """
    return a + b
