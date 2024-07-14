from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    This function handles the root route of the Flask API.
    Returns:
            str: A welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Retrieve a list of usernames from the 'users' dictionary and return it as
    a JSON response.

    Returns:
            A JSON response containing a list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns the status of the API.
    Returns:
            str: The status message "OK".
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    Retrieve user information based on the provided username.
    Args:
            username: The username of the user to retrieve information for.
    Returns:
            If the user is found, the user information is returned
            as a JSON response.
            If the user is not found, a JSON response with an error
            message and a 404 status code is returned.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add a new user to the system.
    Returns:
            A JSON response with the following structure:
            - If the user is added without username:
            {"error": "Username is required"}
            - If the user is added with a duplicate username:
            {"error": "Username already exists"}
            - If the user is successfully added:
            {"message": "User added", "user": <users[username]>}
    """
    new_user = request.get_json()

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    """if username in users:
        return jsonify({"error": "Username already exists"}), 400"""

    users[username] = new_user
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()