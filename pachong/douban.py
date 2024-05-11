import requests
from bs4 import BeautifulSoup
import json


for page in range(20,200,20):

    cot = 0
    totol = 0
    url = 'https://movie.douban.com/subject/30367734/comments?percent_type=&start={}&limit=20&status=P&sort=time&comments_only=1'.format(page)



    headers = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }

    web_text = requests.get(url=url,headers=headers)

    web_text = web_text.json()


    web_text = web_text["html"]

    print(web_text[1:0])

    


    #print(web_text)


    

    


 



    soup = BeautifulSoup(web_text,'lxml')

    #print(soup)
    title_list = soup.select('p > span')

    star = soup.select('.comment-info > .rating')

    #print(star)

    #print(web_text)

    length = len(title_list)

    for i in range(length):
        cot += 1
        try:
            print(star[i].get("class")[0][7:8])
            totol += int(star[i].get("class")[0][7:8])
        except:
            print("无评分")
        print(title_list[i].text)




print(totol)
print(cot)
print((totol / cot) * 2)


