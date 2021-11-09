# -*- coding:utf-8 -*-
import os
import re
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

js_code = 'var timeTable=[["8:20-9:40","8:30-9:50","8:40-10:00"],["10:10-11:20","10:20-11:40","10:40-12:00"],["13:50-15:10","14:00-15:20","14:10-15:30"],["15:40-16:50","15:50-17:10","16:10-17:30"],["18:10-19:30","18:10-19:30","18:10-19:30"],["19:40-21:00","19:40-21:00","19:40-21:00"]];function addTimeShow(){var list=document.querySelectorAll("td");list=Array.from(list);for(var i=list.length-1;i>=0;--i){if(list[i].children.length<1){list.splice(i,1)}}var re=[new RegExp("第一大节"),new RegExp("第二大节"),new RegExp("第三大节"),new RegExp("第四大节"),new RegExp("第五大节"),new RegExp("第六大节")];var idx=0;for(var i=0;i<list.length;++i){var o=list[i];if(idx<6&&re[idx].test(o.innerHTML)){idx++}else{var content=o.children[0].innerHTML;if(new RegExp("敏学楼-D").test(content)||new RegExp("敏学楼-C").test(content)){o.children[0].innerHTML+="<br>"+timeTable[idx-1][0]}else{if(new RegExp("敏学楼-B").test(content)||new RegExp("微机基础室").test(content)||new RegExp("多媒体教室").test(content)){o.children[0].innerHTML+="<br>"+timeTable[idx-1][1]}else{o.children[0].innerHTML+="<br>"+timeTable[idx-1][2]}}}}};addTimeShow();'

word = re.sub('<script type="text/javascript">', '<script type="text/javascript">' + js_code, str(response.text))
word = re.sub('text-align: left', 'text-align: center', word)
word = re.sub('style="width: .*%;"', 'style="width: 10%;"', word)
word = re.sub('#tooltip:before.*}', '', word)
word = re.sub('#tooltip{.*}', '#tab1{width: 1200px;height: 500px;}tr{width: 1200px;height: 30px;text-align: center;}td{height: 10px;border: 1px solid red;text-align: center;}', word)
word = '<meta charset="UTF-8">' + word


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


mkdir("course")

file = open('course/index.html', 'w', encoding="utf-8")
file.write(word)
