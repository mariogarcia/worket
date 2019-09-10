from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from employees.api import EmployeeResource
from companies.api import CompanyResource


def setup_app():
    # linking flask with flask_restful
    app = Flask(__name__)
    api = Api(app)

    # add CORS to be front-end friendly
    CORS(app)

    # URL mappings
    api.add_resource(EmployeeResource, '/employees')
    api.add_resource(CompanyResource, '/companies')

    return app
