
<h1 align="middle">Food Analysis with Yolov5π₯</h1>
<h3 align="middle">μμ κ²μΆκΈ°</h3>
<br/>

## π Introduce

μ¬μ§ μ μμ κ°μ²΄λ₯Ό μΈμνκ³  μΉΌλ‘λ¦¬λ₯Ό μ°Ύμμ€λλ€.

μ¬μ§νμΌ λλ λ°μ΄λλ¦¬ λ°μ΄ν°λ‘ μμ²­νλ©΄ JSONνμμΌλ‘ λ°νν΄μ€λλ€.

## β­ Main Feature

- κ°μ²΄ λΆμμΌλ‘ μ¬μ§ μ μμλ€ μΉΌλ‘λ¦¬ κ³μ°.

## π§ Stack

**Python Flask**

- Yolo v5
- BeautifulSoup


## π How To Run locally

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
  "name": ["apple", "banana", "candy", ...],
  "calorie: [100, 100, 30, ...]
{
```


## π More

- λ μ§ : 2021.03 ~ μ§ν μ€

- νμ

  κΉλκ·  - @dogyun-k π
  
  λΈμ μ§ - @jin-you π
  
  λ°±μ§μ - @hm06063 π


[0. νκ²½μΈν λ° μνλ°μ΄ν°μμΌλ‘ YOLOv5 μ€μ΅ν΄λ³΄κΈ°](https://github.com/dogyun-k/Yolov5/blob/main/Summary/%EC%9A%9C%EB%A1%9C%EC%8B%A4%EC%8A%B5%ED%95%B4%EB%B3%B4%EA%B8%B0.md)

[1. YOLOv5λ‘ μΉΌλ‘λ¦¬ κ³μ°νκΈ°](https://github.com/dogyun-k/Yolov5/blob/main/Summary/Food.md)

[2. μ΄λ―Έμ§ μΈμμ νμ©ν μΉ μλΉμ€ μ μ](https://github.com/dogyun-k/dietblog)
