#클래스:멤버와 메소드를 가지는 객체, 인스턴스: 클래스를 호출하여 만들어지는 객체(사용하려는 변수),멤버:클래스가 갖는 객체, 메소드:클래스 내에 정의된 함수, 속성(어트리뷰트) == 쿨래스의 멤버 : 멤버+메소드
#클래스의 예:은행계좌(소유주이름,계좌잔고 등으로 표현할 수 있는 가장 대표적인 이해하기 쉬운 예)
class Acount:#만일 __init__에 init으로만 되어 있다면 인자는 두개만 받고, 두개 만 받기 때문에 인스턴스를 생성을 못하므로 인스턴스를 따로 Acount()로 생성해준 뒤에 그다음에 인자를 넘겨줘야한다.
    def __init__(self,name,amount): #생성자 , 인수로 name과 계좌 ,self 주의, self를 빼면 인스턴스가 생성이안됨
        self.name = name    #계좌 정보의 초기화, self는 생략 가능하지만 있는게 좋음.
        self.balance = amount #balance는 잔고임, 계좌의 정보를 받아와서 클래스의 멤버 값들을 초기화 시켜줌.
        print("%s님 계좌가 걔설되었습니다."% self.name, end =" ")
        print("%s 님의 잔고는 %d 입니다." % (self.name, self.balance)) #두개 이상의 멤버를 줄 땐 괄호를 씌워줘야한다.
        print()

    def deposiot(self,amount):#이것도 치면 바로 self가 생성됨, 인스턴스임, 입금 함수인듯
        self.balance += amount
        print("%s님의 계좌에 %d 입급되었습니다."%(self.name,amount))
        print("%s님의 계좌잔고는 %d입니다."%(self.name,self.balance))
        print()

    def info(self):
        print("%s님의 계좌잔고는 %d입니다." % (self.name, self.balance))
        print()

    def withdraw(self,amount):    #출금
        self.balance -= amount
        print("%s님의 계좌에 %d 출금되었습니다."%(self.name,amount))
        print("%s님의 계좌잔고는 %d입니다."%(self.name,self.balance))
        print()

a1 = Acount("홍길동",10000) #다른 언어처럼 new로 생성하지 않고 바로 클래스의 이름을 주어 생성, 클래스에서 넘겨받은 self은 a1임, 즉 생성하고자하는 인스턴스, 즉 참조객체
b1 = Acount("홍길녀",50000) #만일 클래스에서 self를 없애버리면 인스턴스가 생성이안되서 아무리 또 다른 애들을 생성하려해도 생성이안되서 오류는 안뜨지만 홍길녀것만 생길것.
b1.deposiot(500000)
a1.info()
b1.info()
b1.withdraw(20000)


# for 변수 in iterables(반복 가능한 객체), for 변수 in 컨테이너 값/변수
# for weather in '@#$%^&*(': #뒤 객체 부분에 값들의 집합인 컨테이너가 와도 범위라고 생각하고 찍는다. -> 파이썬이기에 가능한 일
#     print('*',end="")
# print()
# t =[1,8,2,2,3,4,5,2,3,4]
# for freeze in t:
#     print('#', end="")
# print()
# print(len(t))

#하나이상의 값을 받는 애들을 컨테이너(용기,그릇)라고 부른다.
#컨네이너에 공통으로 적용할 수 있는 연산: indexing / slicing : 한 인덱스를 찝어서 알 수있는것/범위로써 인덱스의 범위를 잡아주어 알 수있는것,ex)list[x] / list[:3], list[7::2]는 인덱스 증가폭을 2로 지정하면 됨.
#강사님이 내주신걸 나만의 방식으로 해보기, 자료형 : number,boolean, list,set,dict,tuple
# for i in range(1,4):
#     if i == 2:
#          print("Hello world")
#          continue
#     for j in range(1,12):
#         if i == 1:
#             print('*',end="")
#         elif i == 3:
#             print('=',end="")
#         else:
#             continue
#     print()
# print("\n")

# # *을 10개찍는 방법
# print('**********')
# print('*'*10) #프로그램사이즈를 줄이라고 치면 이게 정답이라고 볼 수 있다. 곱셈을 이용한방법
#
# for i in range(1,11):
#     print('*',end="")
#덧셈으로 *을 10개를 찍어라
# print('*****'+'*****')#이런식으로 하면 더 단순하다. 아직까지 변수는 쓰지않았음.
# s = '*'
# print(s*10) #변수를 써서 하는 방법, 이거 말고도 함수를 쓰는방법, 다른 자료형,등등 쓰는 방법이 많다.
# for i in range(1,5):
#     print('*'+'*',end="")
