import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    file_name = request.args.get("file")
    if file_name is None:
        return "No file name specified."
    if ".." in file_name:
        return "Invalid file name."
    file_path = os.path.join("/dev/null", file_name)
    try:
        with open(file_path, "r") as f:
            contents = f.read()
            return contents
    except:
        return "The file does not exist or cannot be opened."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

