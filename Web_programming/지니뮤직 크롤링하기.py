import requests # Request package 사용
from bs4 import BeautifulSoup # BeautifulSoup4 package 사용

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# Genie에서 정보를 가져옴
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 음악 리스트
musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

# 음악 하나하나마다
for music in musics:
    # 순위 부분에 있는 순위변동부분(span 태그)를 decompose()로 없애버림
    music.select_one('td.number').span.decompose()

    rank = music.select_one('td.number').text.strip() # 순위, 앞 뒤 여백 strip()으로 제거
    title = music.select_one('td.info > a.title.ellipsis').text.strip() # 노래 제목, 앞 뒤 여백 strip()으로 제거
    artist = music.select_one('td.info > a.artist.ellipsis').text # 가수 이름

    print(rank, title, artist) # 순위, 노래 제목, 가수 이름 순서대로 출력
