from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver_path = 'chromedriver.exe'
# 以ChromeOptions傳遞瀏覽器設定參數，將不會自動打開瀏覽器
headless = webdriver.ChromeOptions()
headless.add_argument("headless")
# 建立Chrome瀏覽器物件
browser = webdriver.Chrome(executable_path=driver_path)  # options=headless
browser.maximize_window()  # 將瀏覽器視窗放到最大

print(type(browser))
target_urls = ['https://deepmind.com.tw/']
# 'http://aaa.24ht.com.tw'
# 'https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/HTML_basics'
# 'http://www2.me.ncu.edu.tw/teacher/Teacher-35/DASD_serve/first.htm'
for idx, url in enumerate(target_urls, start=1):
    print("*" * 100)
    print("第{}個網頁".format(idx))
    browser.implicitly_wait(5)  # 等待網頁載入
    browser.get(url)  # 網頁下載至瀏覽器
    ele_link = browser.find_element(by=By.LINK_TEXT, value="精選書摘")
    print(type(ele_link))
    # exit()

    time.sleep(5)
    print('click')
    ele_link.click()
    print("*" * 100)