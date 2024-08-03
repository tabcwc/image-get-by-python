import requests
import time
#import browser
file_path = 'Bing每日图片 '+time.asctime()+'.jpg'
URL = 'https://dailybing.com/api/v1'
h = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
r = requests.get(url=URL,headers=h)
#r.encoding = r.apparent_encoding
info = r.content
f = open(file_path,'wb')

f.write(info)
f.close()
