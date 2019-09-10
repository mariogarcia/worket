from flask_restful import Resource


class EmployeeResource(Resource):
    def get(self):
        return {'hello': 'employees'}
