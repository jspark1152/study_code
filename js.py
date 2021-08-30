#파일 이름을 json으로 할시 오류 발생

#JSON은 데이터를 주곱다는 데 사용하는 경량의 데이터 형식
#키-값 쌍으로 이루어진 데이터 객체를 저장

#JSON 인코딩은 파이썬의 자료형을 JSON 객체로 변환하는 작업
import json

#사전 자료형 데이터 선언
user = {
    "id": "jinseok",
    "password": "901016",
    "age": 30,
    "hobby": ["sing", "exercise"]
}

#인코딩: 파이썬 변수를 JSON 객체로 변환(띄어쓰기 네 칸 들여쓰기 적용)
json_data = json.dumps(user, indent = 4)
print(json_data)

#JSON 디코딩은 인코딩과 반대로 JSON 객체를 파이썬의 기본 자료형으로 변환하는 작업
import json

#사전 자료형 데이터 선언
user = {
    "id": "jinseok",
    "password": "901016",
    "age": 30,
    "hobby": ["sing", "exercise"]
}

#인코딩: 파이썬 변수를 JSON 객체로 변환
json_data = json.dumps(user)

#디코딩: JSON 객체를 파이썬 변수로 변환
data = json.loads(json_data)
print(data)

#파이썬의 객체를 JSON 데이터로 변환하여 파일로 저장
import json

#사전 자료형 데이터 선언
user = {
    "id": "jinseok",
    "password": "901016",
    "age": 30,
    "hobby": ["sing", "exercise"]
}

#JSON 데이터로 변환하여 파일로 저장
with open("user.json", "w", encoding="utf-8") as file:
    json.dump(user, file, indent = 4)