from selenium import webdriver
import time
import urllib
import os
import sys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# 存圖位置
local_path = 'pic'
# 爬取頁面網址
url = 'http://pic.sogou.com/pics?ie=utf8&p=40230504&interV=kKIOkrELjboMmLkElbkTkKIMkbELjbgQmLkElbcTkKILmrELjb8TkKIKmrELjbkI_65458625&query=%E6%9F%AF%E5%9F%BA&'
# 目標元素的xpath
# xpath = '//div[@id="imgid"]/ul/li/a/img'
xpath = '//div[@class="figure-result-wrap"]/div[@class="figure-result"]/ul/li/div/a/img'
# 一些瀏覽器設定
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 使瀏覽器不會自動關閉
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 忽略不必要的錯誤訊息
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
driver = webdriver.Chrome(
    options=options, service=Service("D:\\python_class\\selenium網路爬蟲\\chromedriver.exe"))  #

# 最大化窗口，因為每一次爬取只能看到視窗内的圖片
driver.maximize_window()
# 紀錄下載過的圖片網址，避免重複下載
img_url_dic = {}
# 瀏覽器打開爬取頁面
driver.get(url)
# 模擬滾動視窗瀏覽更多圖片
pos = 0
m = 0  # 圖片編號
for i in range(100):
    pos += i * 500  # 每次下滾500
    # javascript的知識
    js = "document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)
    for element in driver.find_elements(By.XPATH, xpath):
        time.sleep(1)
        try:
            img_url = element.get_attribute('src')
            # 保存圖片到指定路徑
            if img_url != None and not img_url in img_url_dic:
                img_url_dic[img_url] = ''
                m += 1
                # print(img_url)
                ext = img_url.split('/')[-1]
                # print(ext)
                filename = str(m) + 'kerGee' + '_' + ext + '.jpg'
                print(filename)
                print(os.path.join(local_path, filename))
                # 保存圖片
                urllib.request.urlretrieve(
                    img_url, os.path.join("D:\\python_class\\selenium網路爬蟲\\pic\\", filename))
        except OSError as err:
            print('發生OSError!')
            print(pos)
            print(err)
            break
driver.close()
