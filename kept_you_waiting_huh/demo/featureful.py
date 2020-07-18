from kept_you_waiting_huh.engine.engine import Engine
from kept_you_waiting_huh.server import server

class Featureful(Engine):

    def __init__(self):
        self.file = __file__

    # def update(self, post_data):
    #     super().update(post_data)
    #     print(post_data)
    #     screen = [
    #         [
    #             [0,0], [0,0], [0,0]
    #         ],
    #         [
    #             [2,0], [2,0], [2,0]
    #         ],
    #         [
    #             [0,1], [0,1], [0,1]
    #         ]
    #     ]
    #     return {'screen': screen, 'secretId': 'xxx'}

server.run(Featureful())
