from server import app, db


@app.route('/', methods = ['GET'])
def index():
    return 'Hello World!'
