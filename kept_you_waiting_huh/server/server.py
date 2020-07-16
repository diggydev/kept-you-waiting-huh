"""
Server to support multiplayer.
"""
from flask import Flask
from flask import render_template
from flask import request
from kept_you_waiting_huh.engine.engine import Engine

app = Flask(__name__)
engine = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        global engine
        return engine.update(request.form)
    return render_template('index.html')

def run(_engine: Engine):
    global engine
    engine = _engine
    app.static_folder='/Users/.../dev/kept-you-waiting-huh/kept_you_waiting_huh/demo'
    #works for map.gif but then ui.js isn't found.. can move js to index.html
    print(app.static_folder)
    print(app.config)
    app.run()
