from flask import Flask,request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/info')
class PingUrl(Resource):
    def get(self):
        return {'Receiver': 'Cisco is the best!'}

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)

