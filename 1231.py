class Student:
    def __init__(self,name,snumber,major,age):
        self.name = name
        self.snumber = snumber
        self.age =age
        self.major= major

    def __str__(self):
          return "이름: %s , 학번: %d ,학과: %s,나이: %d" %(self.name,self.snumber,self.major,self.age)

    def info(self):
        print(self)

    def __add__(self, other):
        return self.age + other.age

s1 = Student("최범규",201455050,"ICT",25)
s2 = Student("박성무",201340400,"기계",26)

s1.info()
s2.info()

print("둘 나이의 합: %d" % (s1+s2))

# 도형그리기
# import turtle as t
# t.shape("turtle")
# t.penup()
# t.goto(-200,-50)
# t.pendown()
# t.begin_fill()
# t.color("red")
# t.circle(40,steps=3) #삼각형 그리기
# t.end_fill()
#
# t.penup()
# t.goto(-100, -50)
# t.pendown()
# t.begin_fill()
# t.color("orange")
# t.setheading(45)
# t.circle(40, steps = 4) # 사각형 그리기
# t.end_fill()
#
# t.penup()
# t.goto(0,-50)
# t.pendown()
# t.begin_fill()
# t.color("purple")
# t.setheading(45)
# t.pensize(5)
# t.circle(100)    #원그리기
# t.end_fill()
#
# t.penup()
# t.goto(100, -50)
# t.pendown()
# t.begin_fill()
# t.color("orange")
# t.setheading(45)
# t.circle(40, steps = 9) # 사각형 그리기
# t.end_fill()

#다른 파일에서 만든 클래스를 만들어서 삼각형,사각형,원의 정보를 불러온것.
# import Shape
# 
# r1 =Shape.Rect(10, 20)
# r2 =Shape.Rect(10, 10)
# 
# t1 = Shape.Tri(10, 20)
# t2 = Shape.Tri(10, 10)
# 
# c1 = Shape.Circle(20)
# c2 = Shape.Circle(20)
# 
# r1.info()
# r2.info()
# 
# t1.info()
# t2.info()
# 
# c1.info()
# c2.info()
# 
# #r1.__add__(r2) #add연산자가 진즉에 있었는데 오버로딩 한 것 임. -> 이 함수를 다시 재정의함으로써 '+'라는 연산의 의미가 달라짐.
# 
# print(r1+r2) #이렇게 해주면 +는 위에 __add__로 인해 오버라이딩 되어서 이제 넓이끼리 더함이 가능해진다.
# print(t1+t2)
# print(c1+c2)
# print(r1+t2)# 다른 클래스끼리 넓이의 합

#클래스:멤버와 메소드를 가지는 객체, 인스턴스: 클래스를 호출하여 만들어지는 객체(사용하려는 변수),멤버:클래스가 갖는 객체, 메소드:클래스 내에 정의된 함수, 속성(어트리뷰트) == 쿨래스의 멤버 : 멤버+메소드
#클래스의 예:은행계좌(소유주이름,계좌잔고 등으로 표현할 수 있는 가장 대표적인 이해하기 쉬운 예)
# class Acount:#만일 __init__에 init으로만 되어 있다면 인자는 두개만 받고, 두개 만 받기 때문에 인스턴스를 생성을 못하므로 인스턴스를 따로 Acount()로 생성해준 뒤에 그다음에 인자를 넘겨줘야한다.
#     def __init__(self,name,amount): #생성자 , 인수로 name과 계좌 ,self 주의, self를 빼면 인스턴스가 생성이안됨
#         self.name = name    #계좌 정보의 초기화, self는 생략 가능하지만 있는게 좋음.
#         self.balance = amount #balance는 잔고임, 계좌의 정보를 받아와서 클래스의 멤버 값들을 초기화 시켜줌.
#         print("%s님 계좌가 걔설되었습니다."% self.name, end =" ")
#         print("%s 님의 잔고는 %d 입니다." % (self.name, self.balance)) #두개 이상의 멤버를 줄 땐 괄호를 씌워줘야한다.
#         print()
#
#     def __str__(self): #스트링이 들어가야할 부분을 이렇게 정의했다고 생각하면 될 듯, __이 없으면 public이고 __있어야지만 private이다.
#         return  "%s님의 계좌잔고는 %d입니다." % (self.name, self.balance) #스트링을 리턴하게 된다.
#
#     def deposiot(self,amount):#이것도 치면 바로 self가 생성됨, 인스턴스임, 입금 함수인듯
#         self.balance += amount
#         print("%s님의 계좌에 %d 입급되었습니다."%(self.name,amount))
#         print("%s님의 계좌잔고는 %d입니다."%(self.name,self.balance))
#         print()
#
#     def info(self): #잔액조회
#        # print("%s님의 계좌잔고는 %d입니다." % (self.name, self.balance))
#         print(self) #스트링을 반환하는 함수를 호출
#         print()
#
#     def withdraw(self,amount):    #출금
#         self.balance -= amount
#         print("%s님의 계좌에 %d 출금되었습니다."%(self.name,amount))
#         print("%s님의 계좌잔고는 %d입니다."%(self.name,self.balance))
#         print()
#
# a1 = Acount("홍길동",10000) #다른 언어처럼 new로 생성하지 않고 바로 클래스의 이름을 주어 생성, 클래스에서 넘겨받은 self은 a1임, 즉 생성하고자하는 인스턴스, 즉 참조객체
# b1 = Acount("홍길녀",50000) #만일 클래스에서 self를 없애버리면 인스턴스가 생성이안되서 아무리 또 다른 애들을 생성하려해도 생성이안되서 오류는 안뜨지만 홍길녀것만 생길것.
# c1 = Acount("최범규",100000)
# b1.deposiot(500000)
#
# c1.deposiot(100000)  #두가지 모습으로 다 접급할 수 잇다.
# Acount.deposiot(c1,100000) #두 모습 다 결과는 같지만 이 방법이 훨씬 더 정석의 방법이다.
# c1.withdraw(50000)
# Acount.withdraw(c1,50000)
#
# a1.info()
# b1.info()
# b1.withdraw(20000)


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
