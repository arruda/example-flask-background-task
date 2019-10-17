import time
from flask import Flask
from celery import Celery
from .conf import REDIS_ADDRESS
from .conf import REDIS_PORT


flask_app = Flask(__name__)
flask_app.config.update(
    CELERY_BROKER_URL=f'redis://{REDIS_ADDRESS}:{REDIS_PORT}',
    CELERY_RESULT_BACKEND=f'redis://{REDIS_ADDRESS}:{REDIS_PORT}'
)


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


celery_app = make_celery(flask_app)


@celery_app.task()
def long_sum(a, b):
    time.sleep(10)
    return a + b
