from flask import Flask
from flask import Response
import os


app = Flask(__name__)


@app.route('/')
def func1():
    return 'Hello World!!!'

@app.route('/trubles')
def func2():
    return 'I~ts a trap!!'



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port)
    