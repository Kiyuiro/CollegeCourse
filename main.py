import os
import requests
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
}

data = {
    "userAccount": "04140210090",
    "encoded": "MDQxNDAyMTAwOTA=%%%MTY3Mjk5Mjk3V2FuZw=="
}

url = "http://jiaowu.cswu.cn/jsxsd/xk/LoginToXk"

session = requests.Session()
session.post(url, headers=headers, data=data)

d = datetime.datetime.now()
year = str(d.year)
month = str(d.month)
day = str(d.day)
if len(month) < 2:
    month = "0" + month
if len(day) < 2:
    day = "0" + day
date = year + '-' + month + '-' + day

response = session.get('http://jiaowu.cswu.cn/jsxsd/framework/main_index_loadkb.jsp?rq=' + date, headers=headers)


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


mkdir("course")

file = open('course/course.html', 'w')
file.write(response.text)


