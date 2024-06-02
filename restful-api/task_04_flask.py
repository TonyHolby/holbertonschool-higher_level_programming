from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

""" Defines a route for the root URL. """


@app.route('/')
def home():
    """ Handles the route.

    Returns: The string: "Welcome to the Flask API!".
    """
    return "Welcome to the Flask API!"


""" Defines a new route and return a JSON response using jsonify(). """


@app.route("/data")
def data():
    """ Stores the users in memory using a dictionary.

    Returns: A list of all the usernames stored in the API.
    """
    return jsonify(list(users.keys()))


""" Defines endpoints to simulate different functionalities. """


@app.route("/status")
def status():
    """ Returns the status of the request.

    Returns: OK.
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """ Gets a user.

    Args:
        username: the name of the user.

    Returns: The full object corresponding to the provided username.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


""" Defines a new route that accepts POST requests. """


@app.route("/add_user", methods=["POST"])
def add_user():
    """ Adds the new user to the users dictionary.

    Returns: A confirmation message with the added user's data.
    """
    new_user = request.get_json()
    username = data.get("username")

    if not username:
        return jsonify({"error": "username is required"}), 400

    if username in users:
        return jsonify({"error": "username already exists"}), 409

    users[username] = new_user
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
