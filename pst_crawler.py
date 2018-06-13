from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep

mypst_path = 'http://mypst.com.br'
mypst_page = urlopen(mypst_path)

soup = BeautifulSoup(mypst_page, 'html.parser')

while True:
    divs = soup.find_all('a', attrs = {'class': 'lnk19'})
    for div in range(len(divs)):
        if div % 2 == 0:
            new_page_game = urlopen(mypst_path + divs[div]['href'])
            user_page = BeautifulSoup(new_page_game, 'html.parser')
            print(user_page)
        else:
            new_page_user = urlopen(mypst_path + divs[div]['href'])
        #print(div.text.strip())
    sleep(10)
