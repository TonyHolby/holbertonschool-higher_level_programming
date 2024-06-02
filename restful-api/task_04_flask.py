#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Handles the route.

    Returns:
        The string: "Welcome to the Flask API!".
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Stores the users in memory using a dictionary.

    Returns:
        A list of all the usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns the status of the request.

    Returns:
        The string: OK.
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Gets a user.

    Args:
        username (str): the name of the user.
    Returns:
        The full object corresponding to the provided username or an
        error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the users dictionary.

    Returns:
            A JSON response with the following structure:
            - If the JSON data is invalid: {"error": "Invalid JSON data"}
            - If the username already exists:
            {"error": "Username already exists"}
            - If the user is successfully added:
            {"message": "User added", "user": <user_data>}
            - If an exception occurs: {"error": <exception_message>}
    """
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = new_user
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
