# routes.py
import os
import util

from flask import Blueprint, request, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return 'Hello, World!'

@routes.route('/upload', methods=['POST'])  # Specify that this route accepts POST requests
def upload_file():
    file = request.files['file']
    filename = util.generate_filename(6)
    file.save(os.path.join('img', filename))

    return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
