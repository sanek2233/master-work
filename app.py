from flask import Flask, request
from functools import wraps
import json
from decouple import config
from flask_cors import CORS
from problems import problems
from utils import run_code


app = Flask(__name__)
CORS(app)


API_KEY = config('API_KEY')


def token_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token is None and token != API_KEY:
            return json.dumps({'Message': 'A valid token is missing'})
        return func(*args, **kwargs)
    
    return decorator


@app.route('/')
@token_required
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/problems')
@token_required
def get_problems():
    return json.dumps(problems)


@app.route('/code', methods=['POST'])
@token_required
def post_code():
    parameters = request.get_json()
    result = run_code(parameters)
    return json.dumps(result)


if __name__ == '__main__':
    app.run(debug=True, port=3000)