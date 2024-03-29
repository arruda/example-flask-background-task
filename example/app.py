from flask import Flask
from flask import render_template, jsonify, make_response, request
from celery.result import AsyncResult
from celery import Celery

from example.conf import REDIS_ADDRESS, REDIS_PORT

app = Flask(__name__, template_folder="./templates")

celery_app = Celery(
    backend=f'redis://{REDIS_ADDRESS}:{REDIS_PORT}',
    broker=f'redis://{REDIS_ADDRESS}:{REDIS_PORT}'
)
long_sum = celery_app.signature('example.worker.tasks.long_sum')


@app.route('/', methods=['GET'])
def index():
    info = {}
    return render_template('index.html', **info)
    # return "It is running!!"


@app.route('/call_task', methods=['POST'])
def call_task():
    j = request.json
    result_task = long_sum.delay(11, 2)
    response_dict = {'status': result_task.status,
                     'result_task_id': result_task.id}
    return make_response(jsonify(response_dict))


@app.route('/show_result/<string:result_task_id>', methods=['GET'])
def show_result(result_task_id):
    result_task = AsyncResult(id=result_task_id, app=celery_app)
    response_dict = {
        'status': result_task.status,
        'content': result_task.info
    }
    return make_response(jsonify(response_dict))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
