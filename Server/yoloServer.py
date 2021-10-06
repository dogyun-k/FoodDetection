import json
import os
import io
from PIL import Image
import sys
import base64

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask, request
from yolov5 import get_calorie



app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():

    data = {'food': ['apple', 'banana'], 'calorie': ['120', '300']}
    response = json.dumps(data, indent=4)

    # img = request.form['image']
    img = request.files['image']
    print(type(img))
    
    # print(img)

    # print("\n요청 MIME TYPE :", request.mimetype)
    # if request.mimetype == "application/json":
    #     print("JSON :", request.json)
    # else:
    #     print("Form :", request.form['image'])
    #     print("Files :", request.files, "\n")

    return response


@app.route('/getCalorie', methods=['POST'])
def getCalorie():

    if request.method == "POST":
        imagefile = request.files['image']
        print(type(imagefile))
        response = get_calorie.prediction(imagefile)

    return response


if __name__ == "__main__":
    app.run()
