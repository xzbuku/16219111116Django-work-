import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "New.settings")# project_name 项目名称
django.setup()
from app1.models import Phone
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class getphoneinfo(object):
    def __int__(self):
        chrome_opt = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_opt.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Administrator\AppData\Local\google\Chrome\Application\chromedriver.exe',chrome_options=chrome_opt)
        self.url='https://www.jd.com/'
        self.phones=[]
        self.q=1
    def read(self):
        self.driver.get(self.url)
        search = self.driver.find_element_by_xpath('//*[@id="key"]')
        search.click()
        search.clear()
        search.send_keys('手机')
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        sleep(5)
        js = "var q=document.documentElement.scrollTop=10000"  # documentElement表示获取根节点元素
        self.driver.execute_script(js)
        sleep(5)
    def getdata(self):
        content = self.driver.page_source.encode('utf-8')
        soup = BeautifulSoup(content, 'lxml')
        alls = soup.find_all("div", attrs={"class": "gl-i-wrap",})
        soup.find("li",)
        for i in alls:
            pa=Phone()
            try:
                print(i.find("img").attrs["src"])
                pa.imgsrc=str(i.find("img").attrs["src"])
            except:
                print(i.find("img").attrs["data-lazy-img"])
                pa.imgsrc = "https:"+str(i.find("img").attrs["data-lazy-img"])
            print(i.find("div",class_="p-price").find('i').text)
            pa.price=i.find("div",class_="p-price").find('i').text
            print(i.find("i",attrs={"class": "promo-words"}).text)
            pa.title=i.find("i",attrs={"class": "promo-words"}).text
            print(self.q)
            self.phones.append(pa)
            self.q += 1
            # pa.save()
if __name__=="__main__":
    jsup = "var q=document.documentElement.scrollTop=10000"
    jsclic = "var q=document.getElementsByClassName('pn-next')[0].click()"
    ph=getphoneinfo()
    ph.__int__()
    ph.read()
    ph.getdata()
    for i in range(0,11):
        ph.driver.execute_script(jsclic)
        sleep(2)
        ph.driver.execute_script(jsup)
        sleep(2)
        ph.getdata()



