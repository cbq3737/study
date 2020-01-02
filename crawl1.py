# #웹 크롤링파일을 f.open,f.close하는 파일관리로 바꿔보자 -> 안돌아감.
# from urllib.request import Request, urlopen
# from bs4 import BeautifulSoup
#
# request =Request("https://movie.naver.com/movie/running/current.nhn")
# response = urlopen(request)
# html = response.read().decode("utf-8")
#
# bs = BeautifulSoup(html,"html.parser")
# f= open('movie.txt','w',encoding='utf-8')
# titles = bs.select(".tit>a")
# for title in titles :
#     f.write(title.txt+"\t"+title['href']+"\n")
#     print(title.text, title['href'])
# f.close()


# from urllib.request import Request, urlopen # 더더 간단한 방법을 바꾼것, 하지만 urllib을 이용한 정보를 긁어오는 방식은 login이 걸려있다거나 bot이 확인하는 방식에선 긁어오지못한다.
# from bs4 import BeautifulSoup
#
# request =Request("https://movie.naver.com/movie/running/current.nhn")
# response = urlopen(request)
# html = response.read().decode("utf-8")
# #print(html)
#
# bs = BeautifulSoup(html,"html.parser")
# #current_movies = bs.select(".ls_detail_t1>li")
#
# #for movie in current_movies:
# #titles = bs.select(".ls_dsc >.tit>a")#이정도면 과하게 적어준것
# titles = bs.select(".tit>a")# 요정도만 적어줘도 된다.
# for title in titles :
#     print(title.text, title['href'])



# from urllib.request import Request, urlopen #더 간단한 방법을 바꾼것
# from bs4 import BeautifulSoup
#
# request =Request("https://movie.naver.com/movie/running/current.nhn")
# response = urlopen(request)
# html = response.read().decode("utf-8")
# #print(html)
#
# bs = BeautifulSoup(html,"html.parser")
# #current_movies = bs.select(".ls_detail_t1>li")
#
# #for movie in current_movies:
# titles = bs.select(".ls_dsc >.tit>a")
#
# for title in titles :
#     print(title.text, title['href'])


# from urllib.request import Request, urlopen #네이버 영화 긁어오는것
# from bs4 import BeautifulSoup
#
# request =Request("https://movie.naver.com/movie/running/current.nhn")
# response = urlopen(request)
# html = response.read().decode("utf-8")
#
# bs = BeautifulSoup(html,"html.parser")    #이 부분부터 parsing단계(분석 및 추출)
# current_movies = bs.select(".ls_detail_t1>li") #페이지검사로 페이지의 코드를 보니 영화리스트를 다 포함하는 .ls_detail_t1 안에 li들을 모두 긁어와라
#
# for movie in current_movies:  #그리고 그 긁어온것에 대해서
#     titles = movie.select(".ls_dsc >.tit>a") # 각각 리스트의 원소들의.ls_dsc부분의 .tit부분중 그 아래 a태그 부분을 긁어와라
#
#     for title in titles :
#         print(title.text, title['href']) #그 긁어온것을 텍스트로 ,그리고 url을 표시해라.


# from urllib.request import Request, urlopen #파이참같은곳에서 제공하는게 아니라 , 파이썬 콘솔이나 쉘 등 뼈대만 제공하는곳에는 돌아간다.  # urllib.request가 파일을 긁어오는거
# from bs4 import BeautifulSoup #분석&추출
# req = urlopen("http://www.daum.net")
# print(req.getcode())
# if req.getcode()==200:
#     html = req.read()
#     print(html)ㄴ
#     html = html.decode("utf=8")
#     print(html)
# else:
#     print("HTTP ERROR")
# 
# soup = BeautifulSoup(html, "html.parser")
# print(soup.title)
# print(soup.title.text)


# import urllib.request
#
# page= urllib.request.urlopen("http://www.gutenberg.org/cache/epub/12429/pg12429.txt")
# print(page.read(100))#100글자만 불러오자
# encoded = page.read().decode("utf-8")
#
# print(encoded)
# print(encoded[:100])
