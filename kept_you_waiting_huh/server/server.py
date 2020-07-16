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

app.run()

# https://github.com/alecthomas/flask_injector
# from flask_injector import FlaskInjector
# from injector import Module
#
# class MyModule(Module):
#     @provider
#     @singleton
#     def provide_ext(self, app: Flask) -> ExtClass:
#         return ExtClass(app)
#
# def main():
#     app = Flask(__name__)
#     app.config.update(
#         EXT_CONFIG_VAR='some_value',
#     )
#
#     # attach your views etc. here
#
#     FlaskInjector(app=app, modules=[MyModule])
#
#     app.run()
