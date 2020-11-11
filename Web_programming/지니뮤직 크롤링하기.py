from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img

for tr in trs:
    rank_tag = tr.select_one('td.ac > img')
    title_tag = tr.select_one('td.title > div > a')
    point_tag = tr.select_one('td.point')

    if rank_tag is not None:
        rank = rank_tag['alt']
        title = title_tag.text
        point = point_tag.text
        
        doc = {
            'rank': rank,
            'title':title,
            'point':point
        }
        db.movies.insert_one(doc)

