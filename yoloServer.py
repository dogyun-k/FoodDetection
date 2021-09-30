from flask import Flask, json, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route("/getCalorie", methods=['POST'])
def getCalorie():

    img = request.get_json()
    print(request.files['foodImg'])
    return jsonify(img)



if __name__ == '__main__':
    app.run()
