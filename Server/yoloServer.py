import json

import get_calorie
from flask import Flask, request

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return 'hello'
    # return response


@app.route('/calorie', methods=['POST'])
def calorie():
    if request.method == "POST":

        filename = request.json['filename'][0]
        img = request.json['image'][0]

        print(filename, img)
        # stored_path = './img/' + filename
        # img.save(stored_path)
        #
        # response = get_calorie.get_calories_in_img(stored_path)
        # return response

    return None


if __name__ == "__main__":
    app.run()
