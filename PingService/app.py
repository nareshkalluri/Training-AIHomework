from flask import Flask,request,jsonify
from flask_restplus import Api, Resource, reqparse,fields
import requests
import json

app = Flask(__name__)
api = Api(app)

resource_fields = api.model('Resource', {
    'url': fields.String,
})

@api.route('/api/v1/ping')
class PingUrl(Resource):
    @api.expect(resource_fields, validate=True)
    def post(self):
        url = request.get_json()["url"]
        data = requests.request("GET",url,verify=False)
        responce = json.loads(data.text)
        return responce

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
    