from server import app #db
from flask import render_template, request
import spur

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    val1 = request.form['input1']
    val2 = request.form['input2']
    output = "Test"
    return render_template('index.html', output=output)
