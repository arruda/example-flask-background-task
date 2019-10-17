from flask import Flask
from flask import render_template, jsonify, request, make_response

# app = Flask(__name__)
from example.tasks import long_sum

app = Flask(__name__, template_folder="./templates")


@app.route('/', methods=['GET'])
def index():
    info = {}
    return render_template('index.html', **info)
    # return "It is running!!"


@app.route('/call_task', methods=['POST'])
def call_task():
    result_task = long_sum.delay(1, 2)
    response_dict = {'status': result_task.status,
                     'result_task_id': result_task.id}
    return make_response(jsonify(response_dict))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
