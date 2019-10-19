from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    return jsonify({'info': 'File received'})


@app.route("/post", methods=['GET', 'POST'])
def postIndex():
    if request.method == 'POST':
        print(request.form)
        return jsonify({'info': 'File received'})


if __name__ == "__main__":
    app.run(debug=True)