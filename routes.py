from flask import Flask, request, render_template
app = Flask(__name__)

from api import *

@app.route('/', methods=['GET', 'POST'])
def read_html():
    return render_template('search.html')

@app.route('/parkingData', methods=['GET'])
def parking_data():
    if request.method == 'GET':
        lat= request.args.get('lat')
        lng= request.args.get('lng')
        return json.dumps(parking_near_zipcode(lat, lng))