import base64
import get_food
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calorie/binary', methods=['POST'])
def calorie_with_binary():
    if request.method == "POST":
        filename = request.json['filename'][0]
        img_binary_string = request.json['image'][0]

        # 파일 인코딩
        stored_path = './img/' + filename
        img_data = base64.b64decode(img_binary_string)

        f = open(stored_path, 'wb')
        f.write(img_data)
        f.close()

        response = get_food.in_img(stored_path)

        return jsonify(response)

    return None


if __name__ == "__main__":
    app.run()
