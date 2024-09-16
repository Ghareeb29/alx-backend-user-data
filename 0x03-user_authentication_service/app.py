#!/usr/bin/env python3
"""
Flask App
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def welcome():
    """
    Defines a route for the root URL ("/") of the Flask application.
    
    Returns a JSON response with a welcome message.
    """
    
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
