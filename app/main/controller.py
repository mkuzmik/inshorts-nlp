from flask_restful import Resource


class MainController(Resource):
    def get(self):
        return {'hello': 'world'}
