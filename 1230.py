# # 10자리의 난수를 만드는 수를 argv로 보내서 파일로 만들어보자
# import sys
# import random
#
# f = open(sys.argv[1],'w',encoding="utf-8")
# for i in range(1,3):
#      for j in range(0,5):
#           a = random.randint(1,10) #1부터 10사이의 난수 발생
#           f.write(str(a)+"")  #file에 쓰는것이기에 f.write가 영향이 가고 ,print는 영향이 가지 않음.
#      f.write("\n")
# f.close()
#
# random.randrange(1,100,3) # 1~100사이의 3간격의 수 중에서 난수 발생
# seqvar = ["짬뽕","짜장면","짬짜면"]
# random.shuffle(seqvar)# 시퀀스 자료형 섞기
# random.choice(seqvar)#시퀀스 자료형 중 임의로 한개의 값 반환


#파이썬 모듈에 대한 설명 -> import re 정규식(웹페이지를 파싱할때 필요한 모듈)
#모듈, OS import -> os.system("cls")간단한 모듈 만들기 -> mymod로 ->mymodule.


#test6에서 파일 write해서 터미널에서 test5방법과 비슷한방법으로 실행했을때 파일이 생성되는지?
#test5 터미널로 해서 인수 넘어간느거 확인

#commandline argument:프로그램을 실행하고 argument를 주는게 아니라 실행하면서 argument를 주자.
# a = int(input())    #input은 항상 문자열로 받으니까 형변환시켜줘야함.
# b= int(input())
# print("result:%d" % (a+b))  #가장 기초적인 argument 예제 :1
#만일 한줄로 줄이고싶다면 :2
# a,b=  input().split(' ') #한칸띄고 입력하겠다.
# a = int(a)
# b = int(b)
# print("result:%d" % (a+b))
# #아예 한칸으로 쓰는 방법 : 3
# a,b = map(int,input().split(' '))#map함수는 리스트를 int로 변환,결과는 맵객체인데 맵객체는 변수 여러개에 저장할 수 있음.
# print("result:%d" % (a+b))
#

# #import datetime:datetime모듈을 이용해  data,time객체를 이용가능하다.
# import datetime
# current = datetime.datetime.now()
# print(current)
# past = datetime.datetime(1999,12,13) #이렇게 주는것도 가능함.
# print(past)


#append는 write와 공통은 파일이 없으면 새롭게 만드는데 write는 계속 새롭게 쓴다, 있으면 override를 하고, append는 거기에 추가를 한다.
#using pickle:파일로 저장하는데 메모리에 직렬화 시키는 애, 메모리에 직렬로 나란히 쌓아두고, 메모리에 있는 내용을 그대로 순차적으로 읽어들일때 사용하며 정보를 그대로 보고받으므로 통신에서 직렬,직렬화,직렬화 통신이라고 불리는걸로 알아
# 놓으면 좋다., dump(data,file[,protocol]):data객체 프로토콜을 이용해 메모리에 저장.
#pickle은 단순 텍스트 저장이 아닌 스트림 직렬화를 이용한것 이므로 파일 모드는 반드시  b모드(wb/rb)로 지정되어야 한다.


#seek: 사용자가 원하는 위치로 파일 포인터 이동(레코드 헤더처럼 왔다가갔따암), tell : 현재 파일에서 어디까지 읽고 썻는지 위치를 반환(현재 파일의 위치를 return해줌)
#with-as :파일 입출력을 수행하면 수동으로 파일을 close안해도됌.  open,close부분을 맞꾸면됌. 중요함.
# with open("test1.txt",'r') as f_as:
#     for line in f_as.readlines():
#         print(line,end="")
#     print(f_as.closed)
# f_as.close()
# print(f_as.closed)


# #바이너리 파일이있어야지 결과가 적용되는지 확인가능함.  음성,명상,그림 => 바이너리 파일
# f_src = open("image.jpg","rb")#바이너리 읽기 모드
# data= f_src.read()
# f_src.close()
#
# f_dest = open("image_copy.jpg","wb")#바이너리 쓰기 모드 -> 바이너리 파일을 읽어서 가져온 데이터를 가지고 새로운 복사본 파일을 만듬
# f_dest.write(data)
# f_dest.close()


#readlines 예외 적용
# try:
#     f = open("test1.txt","r",encoding="utf-8")
# except Exception as e:
#     print(e)
# else:
#     lines = f.readlines()
#     for line in lines:  # 바로 위에 줄 주석치고, for line in f.readlines()해도 큰 문제없음.
#         print(line,end="")
#     f.close()
# finally:
#     print("----------------------------------")
#     print("end programming")



#readlines: 모든 라인을 불러 리스트로 제공한다. 리스트의 형태로 제공한다.
# f = open("test1.txt",'r',encoding="utf-8")
# lines =f.readlines()#아래는 루프문으로 한줄한줄 읽는데 이 lines는 한꺼번에 이미 읽어놓은 상태임.
# print(lines) #리스트형태로 출력된다.
#
# for line in lines: #리스트에서 인덱스를 한개씩 빼는 행동
#     print(line)
# f.close()


# #만일 전에 했던 그 파일에 예외를 넣는다면
# try:
#     f = open("test1.txt",'r') #일부러 에러를 일으키기 위해 test3를 줌.
# except Exception as e:
#     print("Exception occurred")
#     print(e)
# else:
#     line = f.read() #한줄로 할꺼라면 print(f.read())로 써주면 한줄로 표현이 가능
#     print(line)
#     f.close() #여기에 finally를 안주는이유는 있지도 않은 애를 close자체를 시킬수없기에 실행이 안됨. 그래서 만약에 일부러 굳이 finally문을 넣을려면 아래에 이렇게 넣어주면 됨.
# finally:
#     print("----------------------------------")
#     print("end of programm")


#read:얘는 파일의 내용을 전부다 읽어들이는 특징, readLine:한줄만 읽음.그래서 루프를 이용하여 한줄 두줄 세줄 네줄..이런식으로 이어짐 그러다가 만일 다읽어서 not line상태가 되면 if문안으로 들어가서 break시켜줌,
# f = open("test1.bnk.txt",'r')#원래 예제는 multilines라는 파일을 따로 생성하여 사용함.
# while True:
#     line = f.readline()#읽어들인 줄에도 다음줄 줄바꿈이 생기는데, 아래 print를 해줌으로써 또 다음칸으ㅏㅗ 줄바꿈 생기므로 넓은 차이가 난다. 얘는 한줄씩읽기때문에 루프를 돌리는 거지 루프를 돌리기 싫다면 한번에 읽어버리는 read를 사용하면 됌.
#     if not line:#다읽은 상태로
#         break
#     print(line,end='')#근데 만약 두칸씩 줄바꿈하여 나오는걸 싶어한다면 end=" "하면 되는거
# f.close()
# ##test1의 백업파일 생성
# fb = open("test1.bnk.txt",'w',encoding="utf-8")
# for i in range(1,10):
#     fb.write("%d: Life11 is too short, YOu need Python\n " % i)
#
# fb.close()


# #FileWrite, 내가 이걸로 test.txt와 test1.txt란 파일을 두개 생성함.
# f = open("test1.txt",'w',encoding="utf-8")
# for i in range(1,10):
#     f.write("%d: Life is too short, YOu need Python\n " % i)
# f.close
# #FileRead
# f= open("test1.txt",'r',encoding="utf-8")
# text = f.read() #f.read말고도 읽어내는 함수가 3가지가 있따. readLine,read,readLines 3가지가 있다.
# print(text)
# f.close


# #파일 I/O에 대해서
# #파일입출력 : 파일 객체= open(파일명,파일모드,encoding="인코딩"), r :읽기모드,w:쓰기모드,a:추가모드(파일의 마지막에 새로운 내용을 추가할때 사용,append라는 의미),그리고 open했으면 반드시 끝에 close를 해줘야한다.둘이 쌍으로 가는애들
# f=  open("test.txt",'w',encoding ="utf-8") #이 순서에 이 형태는 많이 쓰이므로 외우는게 훨씬 편하다
# write_size = f.write("Life is too short,You need Python")#콘솔에쓰는거는 print지만 파일이기에 write이다.
# print(write_size)
# f.close()


#try,except,else,finally구문을 1,2,3,4로 정하고 몇번몇번만 싫행하겠다는 시뮬레이션을 통해서 공부해봐라.
# f = open("result.txt","r")
# try:
#     print(f.read())
# finally: #얘는 무조건 발생하는 애, 예외가 발생했건 안했건 무조건 발생되는 구문
#     f.close()
#

# try:
#     f = open("noteexists.txt","r")
# except FileNotFoundError as e:
#     print(e)    #현재 이 구문에서 발생하는 구체적인 오류 내용을 출력
# else:   # 예외가 발생하지 않은 경우 실행,만일 try,excepy,else중 한 구문만 실행시키고 싶다면 "pass"라는 키워드를 씀으로써 그 구문으로 넘겨서 수 있다.만일 except를 실행시키지않을거라면 그냥 예외가 발생안되면 됨.
#     data = f.read()
#     f.close()


#다른 예외의 예, 예외 형태3
# try: 4/0
# except ZeroDivisionError: #구체적인 예외 상황이 zeroDivisionError임
#     print("Error occureded")


# except 이후 아래 else 구문: 예외가 발생하지 않은 경우에 실행, 예외 형태2
# try: 4/0
# except Exception as e:#예외가 발생했을시 생겨난 메시지를 출력하는것
#     print("Error occureded")
#     print(e)#에러의 종류


#try: 예외가 일어날 가능성이있을때 무엇을 한번 해봐라, except:오류가 일어날 경우 이 행동을 하여라.예외 형태1
# try:4/0
# except: print("오류 발생")#try다음에 오류가 낫기때문에 이 구문이 발생됨.


#예외 처리 : 프로그램의 오류로 인해 잘못 작동되는것을 막기위함.
#container 변수/데이터
# list = []
# list[0]
# 
# test = "Try convert me to int"
# number = int(test)
# 
# result = 4/0 #오류뜸
#
