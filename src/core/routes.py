import os
import config
import random
import string

from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

def generate_filename(length):
    letters = string.ascii_letters
    filename = ''.join(random.choices(letters, k=length))
    return filename

# Endpoint to upload images
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = generate_filename(7) + '.png'
    file.save(os.path.join(f'src/core/{config.upload_directory}', filename))  # Save the file to the 'img' directory
    image_url = f"{config.url}:{config.webserver_port}/img/{filename}"
    return jsonify({'message': 'File uploaded successfully', 'filename': filename, 'url': image_url})


# Endpoint to serve images
@app.route('/img/<filename>', methods=['GET'])
def uploaded_file(filename):
    # Serve images from the 'img' directory
    return send_from_directory(f'{config.upload_directory}', filename)

def start_webapp():
    app.run(host='0.0.0.0', port=config.webserver_port, debug=False)
