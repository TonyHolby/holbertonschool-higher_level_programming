#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
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
