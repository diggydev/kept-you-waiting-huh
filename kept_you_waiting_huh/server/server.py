"""
Server to support multiplayer.
"""
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        screen = [
            [
                [0,0], [0,0], [0,0]
            ],
            [
                [2,0], [2,0], [2,0]
            ],
            [
                [0,1], [0,1], [0,1]
            ]
        ]
        return {'screen': screen, 'secretId': 'xxx'}
    return render_template('index.html')
