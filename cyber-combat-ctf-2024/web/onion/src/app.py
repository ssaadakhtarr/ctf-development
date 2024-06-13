# app.py
from flask import Flask, render_template, request, flash, redirect, url_for
import pickle

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8zadgac]!'

# Homepage
@app.route('/')
def home():
    return render_template('index.html')

# Function to validate if the file is a valid pickle file
def is_valid_pickle(data):
    try:
        pickle.loads(data)
        return True
    except pickle.UnpicklingError:
        return False

# Endpoint to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the POST request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # If user does not select file, browser also submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        try:
            # Read the uploaded file in binary mode
            file_content = file.read()
            print(file_content)
            # Check if the file is a valid pickle file
            if not is_valid_pickle(file_content):
                raise ValueError('Invalid pickle file')
            # Deserialize the content of the uploaded file
            data = pickle.loads(file_content)
            flash(f'File content: {data}')
        except Exception as e:
            flash(f'Error: {e}')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
