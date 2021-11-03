import requests
from bs4 import BeautifulSoup as bs

# 파파고 API
f = open('secret.txt', 'r')
key = f.read().split('\n')


def translate_en_to_kr(text):
    """파파고 API 호출"""
    text = text.capitalize()

    client_id = key[0]  # <-- client_id 기입
    client_secret = key[1]  # <-- client_secret 기입

    data = {'text': text,
            'source': 'en',
            'target': 'ko'}

    url = "https://openapi.naver.com/v1/papago/n2mt"

    header = {"X-Naver-Client-Id": client_id,
              "X-Naver-Client-Secret": client_secret}

    response = requests.post(url, headers=header, data=data)

    if response.status_code == 200:
        send_data = response.json()
        trans_data = (send_data['message']['result']['translatedText'])
        return trans_data
    else:
        print("Error Code:", response.status_code)


def search_by_foodname(food_name):
    food_name = translate_en_to_kr(food_name)
    url = f'https://www.dietshin.com/calorie/calorie_search.asp?keyword={food_name}'

    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = bs(html, 'html.parser')

        # 검색결과 최상단 결과 가져오기
        calorie = soup.select_one(
            '#container > div.contents.calorieDc > table > tbody > tr:nth-child(1) > td:nth-child(2)')
        calorie = str(calorie)[4:-5]
        return calorie
    else:
        return response.status_code


# print(search_by_foodname('rice'))
