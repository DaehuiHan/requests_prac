import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# headers의 역할은 브라우저에서 검색한 것 처럼 해주는 기능을 한다.

data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 항상 이렇게 기본 코드를 붙여넣고 시작하자
# 코딩 시작

# print(soup) 이렇게 하면 브라우저 전체가 나오게 된다.

# FIXME: bs4의 사용 방법 1 (select_one으로 원하는 정보 한개만 가져오기)
# 괄호 안에 들어가는 것은 개발자 도구 -> 해당 dom -> copy -> copy selector
title = soup.select_one(
    '#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')

print(title)

# FIXME: bs4의 사용 방법 2
# 가져온 html 태그 안의 text를 가지고 오고 싶을때
print(title.text)
# 가져온 html 태그의 속성을 가지고 오고 싶을때
print(title['href'])

# FIXME: bs4의 사용 방법 2 (select로 공통된 정보 모두 가져오기)
# 페이지에 들어가서 보면 정보를 어떻게 가져올 것인지 전략을 세우고
# old_content > table > tbody > tr:nth-child(2)
# old_content > table > tbody > tr:nth-child(3)
# 이런식으로 큰 단락을 나눠주는 부분을 copy selector해주고 공통된 부분을 제외하고 모두 지운다.
# 그럼 공통된 부분에 해당하는 애들이 다 나온다.
trs = soup.select('#old_content > table > tbody > tr')
# select는 결과가 리스트로 나오기 때문에 for문으로 돌려준다.
for tr in trs:
    print(tr)
    # select_one과 혼용해서 사용도 가능하다.
    # 여기서 괄호는 원하는 태그를 복사 해본다음에 trs에서 찾지 않은 공통되지 않은 부분을 넣어준다
    a_tag = tr.select_one('td.title > div > a')
    print(a_tag)
    # 이렇게 하면 처음에 select_one하는 것처럼 정보가 나올 것이고 , 거기서 원하는 부분을 빼오면 된다.
    # 그런데 여기서 제목을 빼오기 위해 .text를 하면 줄들(None) 때문에 에러가 난다
    if a_tag is not None:
        print(a_tag.text)
