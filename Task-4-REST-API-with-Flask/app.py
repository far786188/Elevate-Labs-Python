from flask import Flask, jsonify, request
app = Flask(__name__)
users = [
    {
        "id": 1,
        "name": "Farhana",
        "age": 20
    },
    {
        "id": 2,
        "name": "Laasya",
        "age": 21
    }
]

@app.route('/')
def home():
    return "Welcome to User Management API"

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)

    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"})
    return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)