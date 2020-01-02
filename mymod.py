#mymod.py

def myadd(a,b):
    return a+b
#from mymod import myadd로 해주면 앞에 모듈이름 안쓰고 함수이름으로만 사용이 가능하다.
# def Adda(a,b):
#     return a+b
#
# if __name__== '__main__' :#모듈은 각각 이름이 있는데 그중에 첫번째 모듈?은 이름이 __main__이다.
#         print(myadd(2,3))

#from a import Adda #a.py 안에 Adda함수
 # Work디렉토리 아래에있는 b.py의 Addb함수, 하위디렉토리인 work디렉토리에서 b.py를 갖고옴
# from a import Adda
# from Work.B import Addb
#
# print(Adda(1,6))
# print(Addb(2,8))
