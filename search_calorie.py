import requests
from bs4 import BeautifulSoup as bs

# 파파고 API
def get_translate(text):
    text = text.capitalize()

    client_id = "RdYkXsVY_QfOOvVwX5vG" # <-- client_id 기입
    client_secret = "noPzgToDOJ" # <-- client_secret 기입

    data = {'text' : text,
            'source' : 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id":client_id,
              "X-Naver-Client-Secret":client_secret}

    response = requests.post(url, headers=header, data=data)
    rescode = response.status_code

    if(rescode==200):
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:" , rescode)

classes = ['rice', 'eels on rice', 'pilaf', "chicken-'n'-egg on rice", 
           'pork cutlet on rice', 'beef curry', 'sushi', 'chicken rice', 
           'fried rice', 'tempura bowl', 'bibimbap', 'toast', 'croissant', 
           'roll bread', 'raisin bread', 'chip butty', 'hamburger', 'pizza', 
           'sandwiches', 'udon noodle', 'tempura udon', 'soba noodle', 
           'ramen noodle', 'beef noodle', 'tensin noodle', 'fried noodle', 
           'spaghetti', 'Japanese-style pancake', 'takoyaki', 'gratin', 
           'sauteed vegetables', 'croquette', 'grilled eggplant', 
           'sauteed spinach', 'vegetable tempura', 'miso soup', 'potage', 
           'sausage', 'oden', 'omelet', 'ganmodoki', 'jiaozi', 'stew', 
           'teriyaki grilled fish', 'fried fish', 'grilled salmon', 
           'salmon meuniere', 'sashimi', 'grilled pacific saury', 'sukiyaki', 
           'sweet and sour pork', 'lightly roasted fish', 
           'steamed egg hotchpotch', 'tempura', 'fried chicken', 
           'sirloin cutlet', 'nanbanzuke', 'boiled fish', 
           'seasoned beef with potatoes', 'hambarg steak', 'beef steak', 
           'dried fish', 'ginger pork saute', 'spicy chili-flavored tofu', 
           'yakitori', 'cabbage roll', 'rolled omelet', 'egg sunny-side up', 
           'fermented soybeans', 'cold tofu', 'egg roll', 'chilled noodle', 
           'stir-fried beef and peppers', 'simmered pork', 
           'boiled chicken and vegetables', 'sashimi bowl', 'sushi bowl', 
           'fish-shaped pancake with bean jam', 'shrimp with chill source', 
           'roast chicken', 'steamed meat dumpling', 'omelet with fried rice', 
           'cutlet curry', 'spaghetti meat sauce', 'fried shrimp', 
           'potato salad', 'green salad', 'macaroni salad', 
           'Japanese tofu and vegetable chowder', 'pork miso soup', 
           'chinese soup', 'beef bowl', 'kinpira-style sauteed burdock', 
           'rice ball', 'pizza toast', 'dipping noodles', 'hot dog', 
           'french fries', 'mixed rice', 'goya chanpuru']

food_name_en = classes[10]
food_name = get_translate(food_name_en)

url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = bs(html, 'html.parser')
    
    # 검색결과 최상단 결과 가져오기
    calorie = soup.select_one('#container > div.contents.calorieDc > table > tbody > tr:nth-child(1) > td:nth-child(2)')
    print(food_name, str(calorie)[4:-5])
else:
    print(response.status_code)
    
    
