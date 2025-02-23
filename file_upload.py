# Topics:
# - Understand common file upload vulnerabilities and how attackers exploit them.
# - Project:
# - Write a script that simulates a file upload vulnerability
# - by allowing an attacker to upload a malicious file (e.g., PHP shell or reverse shell).

import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

# Configure upload directory
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# HTML form for file upload
HTML_FORM = '''
<!doctype html>
<html>
<head><title>File Upload</title></head>
<body>
<h1>Upload a File</h1>
<form method="POST" action="/upload" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="submit" value="Upload">
</form>
</body>
</html>
'''

# Home route to display the upload form
@app.route('/')
def index():
    return render_template_string(HTML_FORM)

# File upload handler
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded.", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected.", 400

    # Save the file to the upload directory
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return f"File uploaded successfully: <a href='/uploads/{file.filename}'>{file.filename}</a>"

# Serve uploaded files
@app.route('/uploads/<filename>')
def serve_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return f.read()
    return "File not found.", 404

if __name__ == '__main__':
    app.run(debug=True)