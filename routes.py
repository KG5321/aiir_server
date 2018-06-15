from server import app, db
from flask import render_template, request
import spur

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    val1 = request.form['input'] #input
    val2 = request.form['hashowanie'] #hashing method
    val3 = request.form['alfabet[]'] #alphabet
    val4 = request.form['wezly'] #number of clusters


    output = "Test"
    # actually there are 3 lines of output: hash, password and time


    return render_template('index.html', output=output) #to be added: time, hash
