from bs4 import BeautifulSoup
from urllib.request import urlopen


class Model():
    def exec(self, input_url):
        url = urlopen(input_url)

        soup = BeautifulSoup(url, 'lxml')
        cnt_artist = 0
        cnt_title = 0


        for link1 in soup.find_all(name = "p", attrs=({"class": "artist"})):
            cnt_artist += 1
            print(str(cnt_artist) + " 위")
            print(" 아티스트 : " + link1.find("a").text)

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

        for link2 in soup.find_all(name = "p", attrs=({"class": "title"})):
            cnt_artist += 1
            print(str(cnt_artist) + " 위")
            print(" 노래제목 : " + link2.find("a").text)

