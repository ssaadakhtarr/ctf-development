from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code_text = request.form.get('code_text', '')
    if has_non_ascii(code_text):
        return jsonify({"output_text": "Hacking not allowed!"}), 403
    result_text = ""
    try:
        result_text = eval(code_text)
    except Exception as e:
        result_text = str(e)

    return jsonify({"output_text": result_text}), 200

def has_non_ascii(text_string):
    ascii_pattern = re.compile(r".*[\x20-\x7E]+.*")
    return ascii_pattern.match(text_string)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
