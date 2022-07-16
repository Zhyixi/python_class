from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # 使瀏覽器不會自動關閉
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option(
    'excludeSwitches', ['enable-logging'])  # 忽略不必要的錯誤訊息

options.add_experimental_option('useAutomationExtension', True)
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
global browser
browser = webdriver.Chrome(
    options=options, service=Service("D:\\python_class\\selenium網路爬蟲\\chromedriver.exe"))  #
url = "https://www.youtube.com/watch?v=zdMUJJKFdsU&t=8880s"
browser.get(url)  # 將網頁下載至瀏覽器
# print(browser.page_source) # 打印網頁原始碼
