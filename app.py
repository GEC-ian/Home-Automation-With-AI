from flask import Flask, render_template, request
import RPi.GPIO as GPIO
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Configure basic authentication
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'

# Initialize basic authentication
basic_auth = BasicAuth(app)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(1, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)


@app.route('/')
@basic_auth.required  # Require authentication for accessing the root route
def index():
    return render_template('index.html')

@app.route('/gpio', methods=['POST'])
def gpio():
    action = request.form['action']
    pin = int(request.form['pin'])
    if action == 'on':
        GPIO.output(pin, GPIO.HIGH)
    elif action == 'off':
        GPIO.output(pin, GPIO.LOW)
    return '', 204




if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')
