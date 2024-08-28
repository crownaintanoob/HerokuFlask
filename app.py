from flask import Flask, request
app = Flask(__name__)

@app.route('/passesinventory'­, methods=['GET']))
def hello_world():
    print(request.args['args1'])
    return request.args['args1']
if __name__ == '__main__':
    app.run(debug=True)
