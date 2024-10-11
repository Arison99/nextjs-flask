from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store developer names
developers = []

@app.route("/api/developers", methods=['POST'])
def create_developer():
    data = request.json
    name = data.get('name')
    if name:
        developers.append(name)
        return jsonify({"message": "Developer added", "name": name}), 201
    return jsonify({"error": "Name is required"}), 400

@app.route("/api/developers", methods=['GET'])
def get_developers():
    return jsonify(developers)

@app.route("/api/developers/<int:index>", methods=['GET'])
def get_developer(index):
    if 0 <= index < len(developers):
        return jsonify({"name": developers[index]})
    return jsonify({"error": "Developer not found"}), 404

@app.route("/api/developers/<int:index>", methods=['PUT'])
def update_developer(index):
    if 0 <= index < len(developers):
        data = request.json
        name = data.get('name')
        if name:
            developers[index] = name
            return jsonify({"message": "Developer updated", "name": name})
        return jsonify({"error": "Name is required"}), 400
    return jsonify({"error": "Developer not found"}), 404

@app.route("/api/developers/<int:index>", methods=['DELETE'])
def delete_developer(index):
    if 0 <= index < len(developers):
        deleted_name = developers.pop(index)
        return jsonify({"message": "Developer deleted", "name": deleted_name})
    return jsonify({"error": "Developer not found"}), 404