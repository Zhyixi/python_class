from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
# 一些瀏覽器設定
options.add_experimental_option("detach", True)  # 使瀏覽器不會自動關閉
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 忽略不必要的錯誤訊息
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
global browser
browser = webdriver.Chrome(
    options=options, service=Service("D:\\python_class\\selenium網路爬蟲\\chromedriver.exe"))  #
url = "D:\\python_class\\selenium網路爬蟲\\pratice_example.html"
browser.get(url)
time.sleep(5)
tag = browser.find_element(By.XPATH, '//h4')
print(tag.text)
