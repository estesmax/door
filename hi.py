from flask import Flask
import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

pin = 5

GPIO.setup(pin,GPIO.OUT)
GPIO.output(pin,0)

print(pin)


app = Flask(__name__)

@app.route("/")
def hello():
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
    return "opened"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

