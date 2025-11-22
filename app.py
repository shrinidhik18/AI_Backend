from flask import Flask, request, jsonify
from tagger import get_tags
import os

app = Flask(__name__)

@app.route("/tag-image", methods=["POST"])
def tag_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    path = "temp.jpg"
    file.save(path)

    tags = get_tags(path)

    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
