from flask import Flask
from flask import Response
import os


app = Flask(__name__)


@app.route('/')
def func1():
    return 'Hello World!!!'

@app.route('/<name>')
def func2(name):
    return name



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
    
