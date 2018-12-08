import requests

# GET请求
response = requests.get("https://www.baidu.com")
print(response.status_code)
print(response.content)     # 二进制
# response.encoding = 'utf-8'
print(response.text)
print(response.raw)
print(response.json())  # json.loads(response.text)
print(response.cookies)

# GET请求带参数
response = requests.get("https://www.baidu.com/s?wd=python")
print(response.text)

payload = {"wd": "python"}
response = requests.get("https://www.baidu.com/s", params=payload)
print(response.text)

# POST请求
response = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(response.text)

data = {}
response = requests.post('https://api.github.com/some/endpoint', json={'key': 'value'})
print(response.text)

# 指定data类型的
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
# headers = {'Content-Type': 'application/json; encoding:utf8'}
response = requests.post('', data={'key': 'value'}, headers=headers)
print(response.text)


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': '',
    'Refer': ''
}
response = requests.post('http://httpbin.org/post', data={'key': 'value'}, headers=headers)
print(response.text)

# 其它请求方法
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# Multipart-Encoded, 上传文件
r = requests.post('http://httpbin.org/post', files={'file1': open('report.xls', 'rb')})

# cookie发送
r = requests.get('http://httpbin.org/cookies', cookies={'cookie1': 'working'})

# 重定向
r = requests.get('http://github.com')
print(r.status_code)
print(r.history)
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)
