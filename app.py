from flask import Flask, request
app = Flask(__name__)

@app.route('/passesinventory'­, methods=['GET']))
def hello_world():
    print(request.args['args1'])
    return "ergerg" #request.args['args1']
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=54453)
