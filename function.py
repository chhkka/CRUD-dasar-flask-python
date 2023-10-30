from flask import Flask, url_for
app = Flask(__name__)

#GET http Method
@app.route('/req', methods=['GET'])
def get_req():
    return 'get'

#POST HTTP Method
@app.route('/req', methods=['POST'])
def masuk():
    return 'ini methods POST'

#PUT http method
@app.get('/req', methods=['PUT'])
def masuk():
    return 'put' 

#DELETE http method
