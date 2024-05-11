import requests
from bs4 import BeautifulSoup
import json


for page in range(20,200,20):

    cot = 0
    totol = 0
    url = 'https://www.toutiao.com/article/v4/tab_comments/?aid=24&app_name=toutiao_web&offset={}&count=20&group_id=7367556701073146383&item_id=7367556701073146383'.format(page)



    headers = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    web_text = requests.get(url=url,headers=headers)

    web_text = web_text.json()


    web_text = web_text["data"]

    for i in web_text:
        print(i["comment"]["text"])
        

    


    #print(web_text)


    

    


 








