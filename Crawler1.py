import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
print(r.apparent_encoding)
r.encoding = 'utf-8'
print(r.text)