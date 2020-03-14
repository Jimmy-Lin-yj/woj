import requests
import os
from bs4 import BeautifulSoup
headers={
"Referer" : "https://www.mzitu.com/xinggan/",
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64)\
 AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/80.0.3987.132 Safari/537.36"
}
url = "https://www.mzitu.com/xinggan/page/4/"
r = requests.get(url,headers=headers)
bs = BeautifulSoup(r.text,"html.parser")
if not os.path.exists('e:\\scrape_images'):
    os.mkdir('e:\\scrape_images')
os.chdir('e:\\scrape_images')
for i in bs.find_all(class_='lazy'):
    url = i.parent['href']
    image_name=i['alt']
    html = requests.get(url,headers=headers)
    soup = BeautifulSoup(html.text,'html.parser')
    url = soup.find_all(class_='main-image')[0].img['src']
    img = requests.get(url,headers=headers)
    with open(image_name+'.jpg','wb') as fd:
        fd.write(img.content)
