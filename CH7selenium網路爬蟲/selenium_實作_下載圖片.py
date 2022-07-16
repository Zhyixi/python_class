from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
import time
import urllib
import os

# 存圖位置
local_path = 'pic'
# 爬取頁面網址
url = 'http://pic.sogou.com/pics?ie=utf8&p=40230504&interV=kKIOkrELjboMmLkElbkTkKIMkbELjbgQmLkElbcTkKILmrELjb8TkKIKmrELjbkI_65458625&query=%E6%9F%AF%E5%9F%BA&'
# 目標元素的xpath
xpath = '//div[@class="img-layout"]/a/img'
# 啟動chrome瀏覽器
chromeDriver = 'chromedriver.exe'  # chromedriver檔案放的位置
driver = webdriver.Chrome(chromeDriver)
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
    #  滑動滾輪
    js = "document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1)

    for element in driver.find_elements(by=By.XPATH, value=xpath):
        try:
            img_src = element.get_attribute('src')
            # 保存圖片到指定路徑
            if img_src != None and not img_src in img_url_dic:
                img_url_dic[img_src] = ''
                m += 1
                # print(img_url)
                ext = img_src.split('/')[-1]
                # print(ext)
                filename = str(m) + 'kerGee' + '_' + ext + '.jpg'
                print(filename)
                # 保存圖片
                urllib.request.urlretrieve(img_url, os.path.join(local_path, filename))

        except OSError:
            print('發生OSError!')
            print(pos)
            break;

driver.close()