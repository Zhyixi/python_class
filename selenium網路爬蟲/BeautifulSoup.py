import bs4, requests, os
# pip install lxml
pic_save_path = "pic/"
urls = ["http://aaa.24ht.com.tw/"]

# "http://www.mcut.edu.tw"
for url in urls:

    try:
        html_file = requests.get(url=url)  # return a requests.models.Response object
        html_file.encoding = 'utf-8'  # 指定編碼，以解決中文字顯示亂碼問題
        print(html_file.encoding)
        html_file.raise_for_status()
        print("網頁獲取成功!")
        # requests.models.Response object 的重要屬性-獲取狀態
        print("網頁原碼獲取狀態碼", html_file.status_code)
        # requests.models.Response object 的重要屬性-html內容
        objSoup = bs4.BeautifulSoup(html_file.text, 'lxml')  # 將HTML參數傳遞用於解析
        # 獲取title屬性
        print(objSoup.title)
        # 獲取title屬性(不含標籤)
        print(objSoup.title.text)
        # 尋找第一個符合的標籤
        obj_tag = objSoup.find('h1')
        print(obj_tag)
        print(obj_tag.text)
        print(obj_tag.string)
        # 尋找所有符合的標籤
        obj_tag = objSoup.find_all('h1')
        print(obj_tag)
        # 尋找圖片
        pic_tag = objSoup.select('img')
        print("搜尋到的圖片數量:{}".format(len(pic_tag)))
        if len(pic_tag) > 0:
            for i in range(len(pic_tag)):
                imgUrl = pic_tag[i].get('src')
                print("圖片下載中...{}".format(imgUrl))
                figUrl = url + imgUrl
                print("圖片下載中...{}".format(figUrl))
                picture = requests.get(figUrl)
                picture.raise_for_status()
                print("圖片取得成功:{}".format(figUrl))
                pictFile = open(os.path.join(pic_save_path, os.path.basename(imgUrl)), 'wb')
                for diskStorage in picture.iter_content(10240):
                    pictFile.write(diskStorage)
                pictFile.close()
    except Exception as err:
        print("網頁獲取失敗!")
        print(err)
