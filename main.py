import requests

url = "http://openapi.seoul.go.kr:8088/5143694e69736b7935304a70545948/json/trafficSafetyA057PInfo/1/5/"
res = requests.get(url)

data = res.json()
print(data)