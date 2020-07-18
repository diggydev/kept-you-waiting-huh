import os

class Engine:

    def __init__(self):
        pass

    def update(self, post_data):
        if 'power' == post_data['command']:
            return {'type': 'text', 'heading': 'Enter your password'}
        #if no command...
        pass

    def get_graphics_dir(self):
        return os.path.split(os.path.abspath(self.file))[0]
