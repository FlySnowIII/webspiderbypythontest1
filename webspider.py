# coding=utf-8

import requests
import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')

hpDomain = "http://www.asahi.com"
page = requests.get('http://www.asahi.com/apital/medicalnews/focus/list.html?iref=com_api_med_focustop')

page.encoding = 'utf-8'

ulList = re.findall('<ul class="List">(.*?)</ul>', page.text, re.S)
liList = re.findall('<li>(.*?)</li>', ulList[0], re.S)

for li in liList:

    titles = re.findall('>(.*?)<span class="Time">', li, re.S)

    aUrl = re.findall('<a href="(.*?)">', li, re.S)

    times = re.findall('<span class="Time">(.*?)</span>', li, re.S)

    print("-----------------------------------------------------------------------------------------")
    print("ニュースタイトル: {0}".format(titles[0]))
    print("URL: {0}{1}".format(hpDomain, aUrl[0]))
    print("公開時間: {0}".format(times[0]))
