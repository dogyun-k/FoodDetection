import io
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask, request
from yolov5 import get_calorie

app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    
    data = {'food': ['apple', 'banana'], 'calorie': ['120', '300']}
    response = json.dumps(data, indent=4)

    return response


@app.route('/getCalorie', methods=['POST'])
def getCalorie():

    if request.method == "POST":
        imagefile = request.files['image']
        response = get_calorie.prediction(imagefile)

    return response


if __name__ == "__main__":
    app.run()
