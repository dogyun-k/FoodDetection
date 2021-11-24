import base64
import get_calorie
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return 'hello'


@app.route('/calorie', methods=['POST'])
def calorie():
    if request.method == "POST":
        filename = request.json['filename'][0]
        img_binary_string = request.json['image'][0]

        # 파일 인코딩
        stored_path = './img/' + filename
        img_data = base64.b64decode(img_binary_string)

        f = open(stored_path, 'wb')
        f.write(img_data)
        f.close()

        response = get_calorie.in_img(stored_path)

        # print(response)

        print(type(jsonify(response)))
        print(jsonify(response))

        return jsonify(response)

    return None


if __name__ == "__main__":
    app.run()
