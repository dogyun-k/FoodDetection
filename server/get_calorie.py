import os
import sys
import json
import search_calorie as sc

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from yolov5 import detect


def in_img(img_file_path):
    detected_foods = detect.run(weights='../yolov5/weights/best_model.pt', source=img_file_path, nosave=True)

    calorie_list = {"foodname": [], "calorie": []}
    for food in detected_foods:
        calorie_list['foodname'].append(food)
        calorie_list['calorie'].append(sc.search_by_foodname(food))

    return calorie_list

# print(get_calories_in_img('../Server/rice.jpg'))
# print(detect.run(weights='../yolov5/weights/best_model.pt', source='../Server/rice.jpg', nosave=True))
