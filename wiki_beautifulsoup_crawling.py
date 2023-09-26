from urllib import parse
from urllib.request import urlopen
from bs4 import BeautifulSoup
keyword='한국어'
URL='https://ko.wikipedia.org/wiki/'+parse.quote(keyword)
bs=BeautifulSoup(urlopen(URL),'html.parser')
toc=bs.find('ul',id='mw-panel-toc-list')
for i in toc.find_all('div')[1:]:
    print(i.get_text())

body=bs.find('div',id='bodyContent')
paragraph=body.find_all('p')
paragraph

for p in paragraph:
    print(p.get_text())
    
import pathlib  
folder='data'

filename='heo/machinelearning_homework/wiki-korean.txt'

with open(filename, mode='w') as file: 
    for p in paragraph:
        file.write(p.text+'\n')
    else:
        print(f"수집한 데이터를 '{filename}'로 저장하였습니다.")