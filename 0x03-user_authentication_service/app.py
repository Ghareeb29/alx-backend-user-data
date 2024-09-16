#!/usr/bin/env python3
"""
Flask App
"""

from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def welcome() -> str:
    """
    Defines a route for the root URL ("/") of the Flask application.

    Returns a JSON response with a welcome message.
    """

    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users() -> str:
    """Register a new user"""
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login() -> str:
    """POST /sessions"""
    try:
        email = request.form["email"]
        password = request.form["password"]
        user = AUTH.valid_login(email, password)
        session_id = AUTH.create_session(user.id)
        response = jsonify(user.to_json())
        response.set_cookie("session_id", session_id)
        return response
    except Exception as e:
        abort(401)


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    """DELETE /sessions"""
    session_id = request.cookies.get("session_id", None)
    if session_id is None:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
