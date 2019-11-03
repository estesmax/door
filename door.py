from celery import Celery
from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

pin = 11

GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,0)

print(pin)


app = Flask(__name__)

app.config.update(
    CELERY_BROKER_URL='redis://redis:6379',
    CELERY_RESULT_BACKEND='redis://redis:6379'
)

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


celery = make_celery(app)

@celery.task(name="open_door")
def open_door():
    GPIO.output(pin,1)
    time.sleep(.25)
    GPIO.output(pin,0)
    time.sleep(.25)
    GPIO.output(pin,1)
    time.sleep(.25)
    GPIO.output(pin,0)
    time.sleep(.25)
    print("Open start")
    GPIO.output(pin,1)
    time.sleep(3)
    GPIO.output(pin,0)
    print("Open end")

@app.route("/")
def hello():
    open_door.apply_async()
    return "opened"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

