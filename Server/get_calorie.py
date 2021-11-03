import json
from Server import search_calorie as sc
from yolov5 import detect


def get_calories_in_img(img_file_path):
    detected_foods = detect.run(weights='../yolov5/weights/best_model.pt', source=img_file_path, nosave=True)


    calorie_list = {}
    for food in detected_foods:
        if food not in calorie_list:
            calorie_list[food] = sc.search_by_foodname(food)

    name_cal = json.dumps(calorie_list, ensure_ascii=False)

    return name_cal

# print(get_calories_in_img('../Server/rice.jpg'))
# print(detect.run(weights='../yolov5/weights/best_model.pt', source='../Server/rice.jpg', nosave=True))
