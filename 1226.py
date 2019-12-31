# # #확장 치환문:산술,비교 연산자 등을 치환문과 함께 사용할 수 있다. +=,-=,*=,/=%=,//= 등등
# # #문자열은 항상 ""로 묶고, 문자는 '로 묶음, 여려줄의 문자열을 입력할땐  몇줄이 됐건 """로 묶어 주면 되지만 ""쓰면서 문자열이 다음줄로 넘어갈때 \을 해주면 서로 연결되어있다는 뜻이다.
# str3="""asdsadsadsadasdasd
# asdasdsad
# sadasdsad"""
# str2 ="asdad" \
#       "asda" \
#       "asdwd" \
#       "sd"



# # abs:절대값,int:정수변환,float:실수변환, complex, divmod:나눗셈 몫과 나머지 pow:제곱  함수
# # 비트연산자: 다른자료는 안되고 정수형자리형에게만 적용이 가능하다.<<:비트왼쪽시프트,>>:오른쪽 시프트,&은 비트AND, |은 비트OR,^은 비트 XOR, - 비트 NOT을 의미
# a = 13
# print(a << 1)
# print(a)
# print(a >> 1)
# b = 0b00101
# c = 0b11111
# print(b & c) #비트 연산은 2진수를 넣든 10진수를 넣든 상관없다.
# print(b | c)
# print(b ^ c)
# print(-b)


#수치형 복소수형
# cpx = 4+5j
# print(type(cpx))
# print(isinstance(cpx,complex))


#수치형 실수형
# a=1.2
# print(type(a))
# print(isinstance(a,float))
# a.is_integer()#타입판별이 아니라 실수의 값이 정수인지  -> 그래서 false가 나옴
#
# b= 3e3//3*e3 즉 3*10의 3승
# c = -0.2E-4
# print(a,b,c)

#수치형 정수형
# a= 2017
# print(bin(a))#2진수로
# print(oct(a))#8진수로
# print(hex(a))#16진수로 바꿔주는 함


#수치형 : 정수형, 실수형,복소수형
#정수형 : 2진,8진,16진으로 표현
# a =23
# print(type(a))
# print(isinstance(a,int))#이거 그냥 a가 int형인지 알아보자.
# 
# b = 0b1101#2진수
# c= 0o23#8진수
# d= 0X23#16진수
# print(a,b,c,d)#10진수로 표현

#논리합(or), 논립곱(and), 논리부정(not)

#자료형의 분류:int,float,bool..  매핑:dict, 시퀀스: bytes,str,list,tuple
#시퀀스: 인덱싱과 슬라이싱으로 일부분의 데이터만 가져다가 쓸 수 있다.  ex)[2:5],[:3],[3:],  len():길이 반환,in:데이터나 문자열이 포함되어있는지에 대한 여부
# a=1
# print(a>10)
# b=a==1 # a==1는 할당이 아니라 비교임 그러므로 맞으므로 True값이 나옴으로 b = True값이라고 볼 수 있다.
# print(type(b))
# print(b+10)
# print(True+True)#True는 1로 판단, 사실상 False는 0을 의미하고 , 나머지는 다 True값
# c ="Hello Python!"
# d ="Hello"
# print(len(c))
# print(d in c)#문자열로 Hello를 줘도 True


#type : 어떤종류인지 알아보고자 할 때 쓰는  변수,true false를 적을땐 반드시 맨앞이 대문자여야 한다.
# print(type(1))
# print(type(1.243))
# print(type(1+2j))
# print(type(True))
# print(type("Hello World"))
# print(type(False))


#비교연산자,값 비교할때 사용->결과는 항상 boolean으로 나온다.
# print(12 > 34)
# print(12 >= 34)
# print(12 == 34)
# print(12 <= 34)
# print(12 < 34)
# print(12 != 34)


#변수명은 문자 숫자 언더바의 조합으로 구성,하지만 시작은 문자로하는게 좋음,기존에 있던 예약어들은 x
# 값을 다중으로 담아 줄 수 있음.
# e,f = 3.5, 5.3
# x=y=z=10
# print(e,f)
# print(x,y,z)
# e,f = f,e  #이런식으로 스왑가능
# print(e,f)


# 변수, 다른 언어는 변수의 타입을 선언해주고 할당해야대는데 파이썬은 바로 변수에 값을 할당 시켜줌.파이썬은 변수의 타입이 고정되지 않은 동적 타입의 언어
# 변수에 담을 때 a=10일 때 같다가 아니라 담으라는 의미
# price =120000
# vat = 0.1
# final_price = price+(price*vat)
# print(final_price)


# #복소수:실수부+허수부, 허수부는 j혹은 J로 표기
# type(3-4j)
# print((3-4j).real) #실수부
# print((3-4j).imag) #허수부
# print((3-4j).conjugate()) #켤레 복소수 변환


#산술연산자, //:몫,%:나머지,/:나눗셈 **:제곱 주의
# print(1+2)
# print(3-2)
# print(3*2)
# print(4/3)
# print(4//3)
# print(4%3)
# print(2**3)


# print(calendar.month(2022,2)) #캘린더 라이브러리를 사용하여 달력을 보여줄 수 있음. 지금은 그냥 스크립트 실행 방식을 보여주기 위함.
# import calendar


# a =2
# if(a>1):
# print("big")    #이렇게 되면 들여쓰기가 먹지않아서 오류가 뜸.
#     print("Really")


#입력함수
# name = input("What is your name?:  ")
#
# print("Hello",name)


# x= 0.2
# s ="Hello"
# print(x, s ,sep =',',end='\n') #sep 즉 분리하는 객체사이 표시하는 문자를 , 로 해라, 그리고 끝에 출력을 \n로 해라


# print(1)
#
# print("Hello","python")
#
# x= 0.2
# s ="Hello"
# print(str(x)+s) #서로 자료형이 맞지않아서 오류가 뜸, x를 문자열로 바꿔주어서 s에 문자열을 이은 형태가 된 것.
