from flask import Flask
app = Flask(__name__)

from api import *

@app.route('/')
def get_data():
    return json.dumps(parking_near_zipcode('38.219053699999996', '-85.7532753'))