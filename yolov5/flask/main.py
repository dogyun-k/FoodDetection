from flask import Flask, request
from PIL import Image
import io
import torch
import requests
from bs4 import BeautifulSoup as bs
import search_calorie as sc
import json


app=Flask(__name__)

def prediction(img_file) :

    img_bytes=img_file.read()
    img = Image.open(io.BytesIO(img_bytes))

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/user/PycharmProjects/food_detect_server/best_model.pt')

    results = model(img, size=640)

    df = results.pandas().xyxy[0]
    foods = list(df['name'])

    name_cal = {}

    for food in foods :
        food_name = sc.get_translate(food)

        if "food_name" in name_cal:
            name_cal["food_name"].append(food_name)
        else:
            name_cal["food_name"] = [food_name]

        target_url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'

        response = requests.get(target_url)

        if response.status_code == 200:
            html = response.text
            soup = bs(html, 'html.parser')

            # 검색결과 최상단 결과 가져오기
            calorie = soup.select_one(
                '#container > div.contents.calorieDc > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)')
            print(food_name, str(calorie)[4:-5])
            cal = (str(calorie)[4:-5])

        else:
            print(response.status_code)
            cal = 'none'

        if "calorie" in name_cal:
            name_cal["calorie"].append(cal)
        else:
            name_cal["calorie"] = [cal]

    name_cal = json.dumps(name_cal, ensure_ascii=False)
    print(name_cal)

    return name_cal


@app.route('/', methods=['POST'])
def recv_img() :
    if request.method == "POST" :
        imagefile = request.files['image']

        food_name = prediction(imagefile)


    return food_name
