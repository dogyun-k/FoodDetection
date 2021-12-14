
<h1 align="middle">Food Analysis with Yolov5🥗</h1>
<h3 align="middle">음식 검출기</h3>
<br/>

## 📝 Introduce

사진 속 음식 객체를 인식하고 칼로리를 찾아줍니다.

사진파일 또는 바이너리 데이터로 요청하면 JSON형식으로 반환해줍니다.

## ⭐ Main Feature

- 객체 분석으로 사진 속 음식들 칼로리 계산.

## 🔧 Stack

**Python Flask**

- Yolo v5
- BeautifulSoup


## 📌 How To Run locally

**Clone repository and Install requirements**

```sh
$ git clone https://github.com/dogyun-k/FoodDetection.git
```

```sh
$ pip install -r requirements.txt
```

**Request**
```json
[POST] /calorie/binary 
{
  "filename": {fileName},
  "image": {encodedFile}
}
```

**Response**
```json
{
  "name": [a, b, c, ...],
  "calorie: [1, 2, 3, ...]
{
```


## 👀 More

- 날짜 : 2021.03 ~ 진행 중

- 팀원

  김도균 - @dogyun-k 👍
  
  노유진 - @jin-you 👍
  
  백지원 - @hm06063 👍


[0. 환경세팅 및 샘플데이터셋으로 YOLOv5 실습해보기](https://github.com/dogyun-k/Yolov5/blob/main/Summary/%EC%9A%9C%EB%A1%9C%EC%8B%A4%EC%8A%B5%ED%95%B4%EB%B3%B4%EA%B8%B0.md)

[1. YOLOv5로 칼로리 계산하기](https://github.com/dogyun-k/Yolov5/blob/main/Summary/Food.md)

[2. 이미지 인식을 활용한 웹 서비스 제작](https://github.com/dogyun-k/dietblog)
