from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to the folder containing images
IMAGE_FOLDER = os.path.join(app.static_folder, 'images')

@app.route("/images")
def list_images():
    """
    Endpoint to return a list of image filenames in the folder.
    """
    try:
        # List image files with valid extensions
        images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        return jsonify(images)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/static/images/<path:filename>")
def serve_image(filename):
    """
    Endpoint to serve an individual image.
    """
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
