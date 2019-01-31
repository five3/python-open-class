from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Python!'


@app.route('/mirror', methods=['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS'])
def mirror():
    if request.method == 'GET':
        return str(dict(request.args))
    elif request.method == 'POST':
        if 'json' in request.headers.get('Content-Type'):
            return request.data, 200, {'Content-Type': 'application/json'}
        else:
            return request.form
    return 'miss method'


if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
