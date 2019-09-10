from flask_restful import fields, reqparse


company_fields = {
    'name': fields.String
}


def unmarshaller():
    marshaller = reqparse.RequestParser()
    marshaller.add_argument('name', type=str, location='json')

    return marshaller
