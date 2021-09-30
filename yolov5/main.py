import json
import cv2
import requests
import torch
from bs4 import BeautifulSoup as bs

import search_calorie as sc


def detect_food():
    # img
    img_PATH = 'IMAGE_PATH'

    # Model Load('Yolov5 경로', 'custom = 커스텀 모델임', path='모델 가중치파일 경로', source='local' 로컬에 저장된 것임)
    model = torch.hub.load('./models/yolo.py', 'custom',
                           path='WEIGHT_PATH', source='local')  # local repo

    # Images load
    img = cv2.imread(img_PATH)[:, :, ::-1]  # OpenCV image (BGR to RGB)
    imgs = [img]  # batch of images

    # Inference
    results = model(imgs, size=640)  # includes NMS

    # Results
    # results.print()
    # results.save()  # or .show()

    df = results.pandas().xyxy[0]
    food_name = list(df['name'])[0]
    food_name = sc.get_translate(food_name)
    # print(food_name)

    target_url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'
    response = requests.get(target_url)


df = results.pandas().xyxy[0]
foods_name = list(df['name'])
dic = {}

for food in foods_name:
    food_name = sc.get_translate(food_name)
    # print(food_name)
    if "food_name" in dic:
        dic["food_name"].append(food_name)
    else:
        dic["food_name"] = [food_name]

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

    if "calorie" in dic:
        dic["calorie"].append(cal)
    else:
        dic["calorie"] = [cal]

dic = json.dumps(dic, ensure_ascii=False)
# print(dic)
# print(is_json(dic))
