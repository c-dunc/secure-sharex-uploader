# routes.py
import os
import random
import string

from flask import Blueprint, request, jsonify

routes = Blueprint('routes', __name__)

def generate_filename(length):
    letters = string.ascii_letters
    filename = ''.join(random.choices(letters, k=length))
    return filename

@routes.route('/')
def index():
    return 'Hello, World!'

@routes.route('/upload', methods=['POST'])  # Specify that this route accepts POST requests
def upload_file():
    file = request.files['file']
    filename = generate_filename(7)
    file.save(os.path.join('img', filename))

    return jsonify({'message': 'File uploaded successfully', 'filename': filename})
    
