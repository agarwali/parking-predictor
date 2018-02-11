from flask import Flask, request, render_template
app = Flask(__name__)

from api import *

@app.route('/', methods=['GET', 'POST'])
def read_html():
    if request.method=='GET':
        return render_template("index.html")
    if request.method == 'POST':
        data = request.form
        # print(data['lon'], data['lat'])

        parkingdata = parking_near_zipcode(data['lon'], data['lat'])
        return render_template("search.html", parkingdata=parkingdata)