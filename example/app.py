from flask import Flask
from flask import render_template, jsonify, request

app = Flask(__name__)


# app = Flask(__name__, template_folder="./templates")


@app.route('/', methods=['GET'])
def index():
    info = {}
    # return render_template('index.html', **info)
    return "It is running!!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
