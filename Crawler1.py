import requests
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.apparent_encoding)
# # encod是从header中猜测的网页编码 很可能不准确
# # apparent_encoding是通过分析内容得到的编码 原则上更准确
# r.encoding = 'utf-8'
# print(r.text)

#########################################


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常"


# if __name__ == "__main__":
    # url = "http://www.baidu.com/s"
    # kv = {'wd': 'Python'}
    # r = requests.get(url, params=kv)
    # r.encoding = r.apparent_encoding
    # print(r.text[:1000])
    url = "https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2184669578,\
        2405818199&fm=58&w=121&h=140&img.JPEG"
    path = ".\UCAS.jpg"
    r = requests.get(url)
    print("ha")
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close
