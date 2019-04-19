import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "New.settings")# project_name 项目名称
django.setup()
from app1.models import Movietreu
from  datetime import *
from time import sleep
import urllib.request
from bs4 import BeautifulSoup
import re
num=0
url="https://movie.douban.com/top250?start="
MovieList = []
_id = 0
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
while num <= 225:
    request = urllib.request.Request(url+str(num), headers = ua_headers)
    response =urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    onenodes=soup.select("div .item")
    for onenode in onenodes:
        movie = Movietreu()
        titles=onenode.find("div",class_="info")
        print(titles.find("p").text.split()[1])
        movie.actor=titles.find("p").text.split()[1]
        movie.imgsrc=onenode.find("div",class_="pic").find('img')['src']
        title1s=titles.find_all("span",class_="title")
        title2=titles.find_all("span",class_="other")[0].text
        for i in range(len(title1s)):
            title2=title1s[i-len(title1s)+1].text+title2
        print(title2)
        movie.mname=title2
        movie.data = datetime(year=2017,month=3,day=24)
        try:
            print(titles.find("p",class_="quote").text)
            movie.content = titles.find("p", class_="quote").text
        except:
            print("无")
            movie.content = "暂无"
        print(_id)
        _id += 1
        # movie.save()
    num=num+25
    sleep(2)

