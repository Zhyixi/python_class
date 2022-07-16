from selenium import webdriver
from selenium.webdriver.common.by import By

import time
driver_path = 'chromedriver.exe'
# 以ChromeOptions傳遞瀏覽器設定參數，將不會自動打開瀏覽器
headless = webdriver.ChromeOptions()
headless.add_argument("headless")
# 建立Chrome瀏覽器物件
browser = webdriver.Chrome(executable_path=driver_path, options=headless)
browser.maximize_window()  # 將瀏覽器視窗放到最大

print(type(browser))
target_urls = ['C:\\Users\\sean\\Desktop\\python授課資料(基礎)\\selenium_pandas_project\\index.html']
# 'http://aaa.24ht.com.tw'
# 'https://developer.mozilla.org/zh-TW/docs/Learn/Getting_started_with_the_web/HTML_basics'
# 'http://aaa.24ht.com.tw'
# 'http://www2.me.ncu.edu.tw/teacher/Teacher-35/DASD_serve/first.htm'
for idx, url in enumerate(target_urls,start=1):
    print("*" * 100)
    print("第{}個網頁".format(idx))
    browser.implicitly_wait(5)  # 等待網頁載入

    browser.get(url)  # 網頁下載至瀏覽器
    print("瀏覽器名稱:\n{}".format(browser.name))
    print("瀏覽器標題:\n{}".format(browser.title))
    print("目前網址:\n{}".format(browser.current_url))
    print("網頁連線ID:\n{}".format(browser.session_id))
    print("瀏覽器功能設定，以dict形式顯示:\n{}".format(browser.capabilities))
    print("網頁原始碼:------\n{}".format(browser.page_source))
    print("------")
    # tag = browser.find_element_by_xpath('//bpdy/section/h1')  # 可找到符合指定相對Xpath的第一個元素內容
    tag0 = browser.find_element(by=By.XPATH, value='//body/section/p')  # 可找到符合指定相對Xpath的第一個元素內容
    tag1 = browser.find_element(by=By.XPATH, value='//body/section/p[1]')  # 當有重複元素的時候以索引指定(注意這邊索引編號的方式)
    tag2 = browser.find_element(by=By.XPATH, value='//body/section/p[2]')  # 當有重複元素的時候以索引指定(注意這邊索引編號的方式)
    tag3 = browser.find_element(by=By.XPATH, value="//body/section/p[@class='price']")  # 以元素屬性指定
    pic = browser.find_element(by=By.XPATH, value="//body/section/img[@class='picture']")  # 以元素屬性指定照片
    print("指定XPATH找到的文字:\n{}".format(tag1.text))
    print("指定XPATH找到的文字:\n{}".format(tag2.text))
    print("指定XPATH找到的文字(以屬性指定):\n{}".format(tag3.text))
    print("指定XPATH找到的照片路徑(以屬性指定):\n{}".format(pic.get_attribute('src')))
    print("*"*100)
    # time.sleep(10)