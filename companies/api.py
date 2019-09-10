from flask_restful import Resource, marshal_with
from .marshallers import unmarshaller, company_fields
from .repositories import list_all


class CompanyResource(Resource):
    def __init__(self):
        self.unmarshaller = unmarshaller()
        super(CompanyResource, self).__init__()

    @marshal_with(company_fields)
    def get(self):
        """returns a collection of companies"""
        return list_all()

    @marshal_with(company_fields)
    def post(self):
        """creates a new company"""
        args = self.unmarshaller.parse_args()

        return args
