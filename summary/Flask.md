# Flask

Flask로 서버를 구축하고 서버에 이미지를 전송해 학습모델을 동작하게 해 보자



## 1. Flask 특징

- 마이크로 웹 프레임워크 -> 구축이 쉽고 하나의 파일로 끝남.

- 스프링처럼 디렉토리 구성이 주어지지 않음.

    ```
    ├── project/
    │      ├─ __init__.py
    │      ├─ models.py
    │      ├─ forms.py
    │      ├─ views/
    │      │   └─ main_views.py
    │      ├─ static/
    │      │   └─ style.css
    │      └─ templates/
    │            └─ index.html
    └── config.py
    ```

    - 주로 이렇게 구성함

- 자체에 Form, Database 처리 기능 없다. -> 모듈로 처리

    - DB : SQLAlchemy -> models.py
    - Form : WTForms -> forms.py

- 개발 자유도가 높음. 굳.
