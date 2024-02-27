import RPi.GPIO as GPIO
import time
from flask import Flask

LED1  = 11  
LED2  = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/<led>/<st>')
def control(led, st):
    if led == 'led1':
        if st == 'on':
            GPIO.output(LED1, 1)
            return f'Led 1 - ON'
        if st == 'off':
            GPIO.output(LED1, 0)
            return f'Led 1 - OFF'
    elif led == 'led2':
        if st == 'on':
            GPIO.output(LED2, 1)
            return f'Led 2 - ON'
        if st == 'off':
            GPIO.output(LED2, 0)
            return f'Led 2 - OFF'

if __name__ == '__main__':
    app.run(debug=True, host='192.168.204.172')
