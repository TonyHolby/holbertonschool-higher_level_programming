from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}


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
    This function retrieves a list of usernames from the 'users' dictionary
    and return it as a JSON response.

    Returns:
            A JSON response containing a list of usernames.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    This function returns the status endpoint of the API.

    Returns:
            str: The status message "OK".
    """
    return "OK"


@app.route("/users/<username>")
def user(username):
    """
    This function retrieves user information based on the provided username.

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
            - If the JSON data is invalid: {"error": "Invalid JSON data"}
            - If the username is missing: {"error": "username is required"}
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
        return jsonify({"error": "Username already exists"}), 400

    users[username] = {
        "name": username.get("name"),
        "age": username.get("age"),
        "city": username.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
