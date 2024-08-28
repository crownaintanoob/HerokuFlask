from flask import Flask
app = Flask(__name__)

@app.route('/passesinventory')
def hello_world():
    print(request.args['args1'])
    return request.args['args1']
