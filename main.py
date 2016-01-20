from flask import Flask
from flask import request
from Model.Database import Database as DB
import Credentials

app = Flask(__name__)

db = DB(Credentials.user, Credentials.password)

@app.route('/')
def index():
    return 'index'


@app.route('/echo', methods=['POST'])
def echo():
    """
    receive data and sent it back

    :return: same json that was sent
    """
    print request

    return request.data

@app.route('/save', methods=['POST'])
def save():
    network_information = request.get_json()["network_info"];
    return request.data




if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')