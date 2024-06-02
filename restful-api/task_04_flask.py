#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    Handles the route.

    Returns:
        The string: "Welcome to the Flask API!".
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
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
        The status message: OK.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Gets user information.

    Args:
            username (str): The username of the user.

    Returns:
            If the user is found, the user information
            is returned as a JSON response.
            If the user is not found, a JSON response with an
            error message and a 404 status code is returned.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the users dictionary.

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
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
