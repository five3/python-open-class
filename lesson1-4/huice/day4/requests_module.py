import requests

# GET请求
response = requests.get("https://www.baidu.com")
print(response.status_code)
print(response.cotent)
# response.encoding = 'utf-8'
print(response.text)
print(response.json())  # json.loads(response.text)

# GET请求带参数
response = requests.get("https://www.baidu.com/s?wd=python")
print(response.text)

args = {"wd": "python"}
response = requests.get("https://www.baidu.com/s", args)
print(response.text)

# POST请求
data = {}
response = requests.post('', data=data)
print(response.text)

data = {}
response = requests.post('', json=data)
print(response.text)

# 指定data类型的
data = {}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
headers = {'Content-Type': 'application/json; encoding:utf8'}
response = requests.post('', data=data, headers=headers)
print(response.text)

data = {}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': '',
    'Refer': ''
}
response = requests.post('', data=data, headers=headers)
print(response.text)