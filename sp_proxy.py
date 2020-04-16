from flask import Flask, request
from flask_restx import Api, Resource, fields, reqparse
from waitress import serve
import os
import logging
import requests 
from requests_ntlm import HttpNtlmAuth

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
api = Api(app, version='1.0', title='Sharepoint NTLM Proxy Forwarder API',description='Authenticate Sharepoint Forwarded Requests Using NTLM',)
ns = api.namespace('api/v1', description='Sharepoint NTLM Proxy Pperations')

CA=os.path.dirname(os.path.realpath(__file__))+'/certs/XXX_CA.pem'

@ns.route('/splists')
class TodoList(Resource):

    @ns.doc('Sharepoint List API')
    @ns.param('uri', description='Sharepoint URL To Forward For NTLM Authentication', _in='formData')
    def post(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument('uri', required=True, location='form', type=str, help='Sharepoint URL To Forward For NTLM Authentication')
        args = parser.parse_args()
        x = requests.get(args['uri'],auth=HttpNtlmAuth("USERNAME","PASSWORD"),verify=False, headers= {"Accept":"application/json; odata=verbose"})
        return  x.json() , x.status_code

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    app.run(host='127.0.0.1', port=port, debug=True)