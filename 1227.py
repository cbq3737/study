# #함수의 인수:기본값이 필요하면 선언이 가능할 뿐더러, 필요한 개수만큼 선언할 수 도 있다.
# def sum(a,b):
#     return a+b
# def incr(a,step=  1): #두번쨰 인자의 기본값은 1이라고 지정
#     return a + step
#
# print(sum(2,3))
# print(incr(10))
# print(incr(10,2)) #이렇게 두번째 인자를 직접 지정도 가능


# #스코핑 룰 예제
# x =1 #전역변수 =global
# def func(a):
#     return a+x
# def func2(a):
#     x=2 #지역변수 =local
#     return a+x
# print(func(10))
# print(func(10))
# print(x) #전역변수
# #전역변수 바꾸는 방법
# g =1
# def func3(a):
#     global g #전역변수를 전역변수로라고 알려주었으므로 객체의 값을 변경이 가능하다.
#     g=3
#     return a+ g
# print(func3(10))
# print(g)


# # 함수의 인수전달: 기본적으로 참조에 의한 호출
# def g(t):
#     t[0]=0
#
# a =[1,2,3]
# g(a)    # 파이썬에서 중요하게 생각하는것중에 하나가 자료형에따라 변경 가능한 타입,불가능한 타입이 있기에 주의해야한다. list는 변경 가능타입
# print(a)

# b =(2,3,4) #튜플
# g(b) #튜플이므로 원소변경이 불가능해서 오류뜸
# print(b)


# #return문 활용
# def swap(a,b): #파이썬에선 어차피 주소인 참조객체를넘겨주는것이기에 이렇게 가능함.
#     return b,a
# print(swap(10,20)) #결과값은 튜플로 반환된다.

# #함수만들기
# def dummy():
#     pass #실행할 내용이 없을때 pass라는 키워드를 써주면 됌.
# def my_function():
#     print("Hello World")
#
# def times(a,b):
#     return a*b
#
# def do_nothing():
#     return
#
# dummy()
# my_function()
# print(times(1,2))
# print(do_nothing())
#
# t= times# 함수도 객체다.함수도 객체이므로 함수도 변수에 담을 수 있음. 자바스크립트를 기억
# print(t(10,10))
# print(t,times,end=" ") #객체이므로 이런식으로 호출하면 주소가 나옴.


# #while 예제,while문에서 무한루프 나올 시 ctrl+c를 눌러주셈됨
# i =0
# while i<100:
#     i +=1;
#     if i<5:
#         continue
#     print(i,end =" ")
#     if i>10:
#         break
# else:
#     print("이블록은 실행되지 않을것임.") #원래는 이 else문도 while문 끝나고 실행이 되는데 while문 블록중 하나라고 취급되어서 위에 break;로 인해 탈출됨.



# #list 내포: for문을 한줄로 요약해서 사용하는것.]
# # while문 반드시 break문이 들어가야한다.
# count = 1
# while count <11:
#     print(count,end =" ")
#     count+=1
# else :  #while문도 다 끝나면 else문으로 들어감.
#     print(" ")
# ### 1~100까지 정수 합 구하기
# sum,i = 0,1
# while i<=100:
#     sum += i
#     i+=1
# print(sum)


# #break문: 수행중 만나면 무조건 빠져나옴
# list =[1,3,5,7,9,11,13,15,16,19]
# for x in list:
#     if x % 2 ==0:
#         break
#     elif x > 10: #여기서 11이 들어왔을때 이 구문으로 들어오는데 continue이므로 다시 올라감 그래서 아래 else로 빠지지않기때문에 출력이 안됌.
#         continue
#     else:
#         print(x)
# #continue: 얘를 만나면 이후 구문을 실행하지 않고 처음으로 이동한다.


# #반복문 enumerate :해당 list의 인덱스와 value값을 같이 뽑아줌.
# colors =["red","orange","yellow","green","pink","blue"]
# for index,color in enumerate(colors):
#     print(index,color)


# for x in range(1,10):
#     for y in range(1,10):
#         print("{0}*{1}= {2}".format(x,y,x*y))
#     print()


# #반복문 for문이 정상적으로 끝나면 아래 else가 잇다면 else가 실행됨.
# animals = ["cat","cow","tiger"]
# for animal in animals:
#     print(animal,end =" ")
#
# for x in range(1,10,3):
#     print(x,end="\n")
#
# data =[1,2,10,11,9]
# for xi in data:
#     if xi>10:
#         break
#     else:
#         print("10보다 큰 수없음")

#in, not in , 뒤에 오는값에 포함이 되는지 포함안되는지 ex) x in 튜플, x in 리스트, x in 문자열


# # 조건 표현식 , 한줄로도 표현이 가능하다. 삼항 연산자
# money = 8500
# print("by taxi" if money>10000 else "bybus") #if 참이라면 bytaxi 아니라면 else, 잘 사용하진 않음. 참, 조건, else 거짓 이 형태임.


# #조건문
# n= -2
# if n >0:
#     print("양수")
# elif n<0:
#     print("음수")
# else:
#     print("0")


# #객체의 값복사 , 전체를 가르키는 [:]를 사용하여 복사
# x = [1,2,3]
# y =x[:]# y라는 객체에 이 값들을 할당한다는 의미이므로 y=x와 같은 주소를 넣는다는 개념이 아니므로 값복사가 가능하다.
# print(y)
# print(x is y) #false가 나오는건 값 복사가 된것
# x[1] = 4
# print(y)#값 역시 바꼇는지 안바꼇는지 확인하는것
# #객체의 값복사2 :copy모듈 사용
# import copy
# x =[8,9,10]
# y = copy.copy(x) #앞에가 모듈, 뒤에 copy가 메소드
# print(x is y)
# x[1] = 4
# print(y)
# #객체의 값복사3 : 2차원 리스트 이상일 경우,deepcopy함수 이용
# import copy
# a = [1,2,3]
# b = [4,5,a] #[4,5,[1,2,3]]
# x = [a,b,100]#[[1,2,3],[4,5,[1,2,3]],100]  이럴경우 카피는 deepcopy를 사용, 이차원 리스트 이상일땐 deepcopy사용
# y = copy.deepcopy(x)
# print(y)


# #객체의 복사, 레퍼런스 복사: 참조하는 주소만 복사하는것
# x =[1,2,3]
# y = x #y가 x가 가르키는 [1,2,3] 리스트객체를 가르키는것.
# print(y)
#
# print(hex(id(x)),hex(id(y))) #주소가 복사된건지 확인하려고
# x[1] = 4
# print(y)#x의 값을 변경해줘도 y의값도 바뀜


# # 객체 ID: id()함수를 이용하면 객체의 주소를 식별할 수 있다. 만일 두 객체의 ID가 동일하면, 같은 객체를 참조하고 있는것.
# i1 = 10 # 각각 i1,i2가 10을 가지 객체를 만드는게 아니라, 같은 값이 있으면 그냥 그 객체로 받아들여짐.그래서 같은걸 가르킴
# i2 = 10
# print(hex(id(i1)),hex(id(i2))) #같은걸 가르킴
#
# l1 =[1,2,3]
# l2 =[1,2,3]
# print(hex(id(l1)),hex(id(l2))) #리스트는 별개로 생김
#
# s1= "hello"
# s2= "hello"
# print(hex(id(s1)),hex(id(s2))) #문자열도 같은것을 가르킴
#
# print(i1 is i2)
# print(l1 is l2)
# print(s1 is s2)


# #레퍼런스 카운트와 쓰레기 수집 : 레퍼런스 카운트 : 객체를 참조하는 참조 수, 레퍼런스 카운트가 0이되면 사용하지 않는 객체로 판단하여 자동으로 사라짐, 이 자동으로 사라지는 작업을 가비지 콜렉터에 의해서 쓰레기 수집이 이뤄짐.
# import sys
# x = object()#x가 객체가됨, 그냥 아무 object()형을 담은것.
# print(sys.getrefcount(x)) #2나온다는건 객체 자기 자신과 참조객체가 가르키고있기때문에 2가나오는것
#
# y= x #이렇게 되는순간 y가 x가 가르키는 객체를 똑같이 가르키게 되므로 참조가 하나 더 늘어나는것.
# print(sys.getrefcount(x))
#
# print(sys.getrefcount(y))
#
# del(x)
# print(sys.getrefcount(y))


# #객체:파이썬에서 모든 자료들은 객체의 형태로 저장된다. 심볼테이블: 변수의 이름과 젖아된 데이터의 주소를 저장하는 테이블
# g_a = 1
# g_b = "symbol"
# def f():
#     l_a = 2
#     l_b ="table"
#     print(locals())#지역변수에 대한 정보
# f() #dict타입의 객체로 반환함.안에 참조객체와 실제객체의 이름이 dict형태로 들어가있음
# print(globals())#전역변수에 대한 정보


## 순차자료형 내장 함수: range,  range로 인하여 값을 생성할 수 있다.
# seq = range(10)
# print(seq,type(seq))
# print(seq[0:])
# print(len(seq))
# 
# for i in seq:
#     print(i)
# 
# seq2 = range(5,15) #5이상 15미만의 순차적 정수 목록
# for i in seq2:
#     print(i)
# 
# seq3 = range(0,-10,-1) #0부터 -10까지 -1만큼
# for i in seq3:
#     print(i)


# # 사전 순회 다양한 방법
# d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
# for key in d:
#     print(str(key) + ":" + str(d[key]),end =' ') #키를 문자열화해서 출력, d[key]은 키에 대응하는 value값을 의미
# else:
#         print()
# for key in d.keys():
#     print("{0}:{1}".format(key,d[key]),end =' ') #format으로 인하여 그 자리에 값을 맞춰넣어주고, end로 인하여 공백을 넘어줌으로써 한줄로 출력이 가능
# else:
#     print()
# for key,value in d.items():
#     print("{0}:{1}".format(key,value),end= ' ')
# else:
#     print()


# # # 사전의 메소드
# d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
# d['volleyball'] = 6
#
# print(d.keys())# keys():사전내 키 목록을 dict_key객체로 튜플안에 리스트형으로 반환
# print(d.values())# values():사전내 값 목록을 dict_value객체를 튜플안에 리스트형으로 반환
# print(d.items())# items():사전내 키:값 쌍으로 묶인 튜플을 반환
#
# #x = d['handball'] #키 중에 handball이 없기때문에 키 에러가 난다
# x = d.get('handball') #키중에 handball을 가져와라 없으면 none이 뜸
# print(x)
#
# del d['soccer']
# print(d)
#
# d.clear()
# print(d)


# #사전의 키, 사전의 키는 해싱해야하기 때문에 수정 불가능한 객체여야 한다.
# d ={}
# print(d)
#
# d[True]= 'true'
# d[10] = '10'
# d["twenty"] ='20'
# d[(1,2,3)] = '6' #그냥 키가 튜플형임
#
# print(d)
#
# #d[[1,2,3]]='6'#타입에러 발생


# # #사전 생성방법
# d = dict() #빈 사전 생성
# print(d)
# 
# d = dict(one = 1, two = 2) #각각 key와 value를 할당
# print(d)
# 
# d = dict([('one',1),('two',2)]) #연속되는 자료형 list안에 튜플로 키값과 value를 주어서 dict형태로 만들어준것.
# print(d)
# 
# keys = ('one','two','three')
# values = (1,2,3)
# d = dict(zip(keys,values))#키와 값을 별도로 튜플로 생성한후에 zip메소드로 합쳐줌
# print(d)
# 
# print(list(zip([1,2,3],[4,5,6])))#zip은 동일한 자리에 있는 원소들끼리 묶어준다
# 

# # 사전(dict), 키 기반으로 값을 저장하고, 연결형 자료형이 아니므로, len(), in,not in정도만 사용 가능, 얘 역시 순서를 안갖고잇으며 키와 value가 쌍으로 이루어져있어서 원하는값이 있으면 key로 인해 찾을 수 있음.묶는것 set처럼 {}로 묶어준다.
# d ={'basketball':5,'soccer':11,'baseball':9}
# print(d,type(d))
#
# print(d['baseball'])
#
# d['volleyball'] = 6 #dict에 추가  dict["key"] =value
# print(d)
#
# print(len(d))
# print('soccer' in d)
# print('volleyball' not in d)



# #unpacking시 왼쪽 변수가 부족하면 에러가 발생한다.
# t = (1,2,3,4,5,6)
# a, *b = t #a는 한개만 꺼내고, b는 여러개를 꺼낸다는 의미(갯수에 맞춰서 들어간다),
# print(a,b)
#
# *a,b = t # *a같은 확장 unpacking은 왼쪽 변수가 적을때 사용하며 묶어진것들은 리스트로 묶어진듯?
# print(a,b)
#
# a,b,*c = t
# print(a,b,c)
#
# a,*b,c = t
# print(a,b,c)


# #튜플의 packing:나열된 객체를 튜플에 넣는 행위, unpacking:튜플, 리스트안에 객체를 변수로 할당하는것
# t = 10, 20,30,"Python"
# print(type(t))
#
# a,b,c,d, = t #언팩킹 튜플
# print(a,b,c,d)
#
# a,b,c,d = [10,20,30,"python"] #언팩킹 리스트, 하나하나 나누어준 상태에서 할당하는것.
# print(a,b,c,d)


# 리스트:[] 원소 변경가능
# 세트:{}
# 튜플:() 원소 변경 불가능
# 사전:{} key:value

#튜플 : 리스트와 비슷하지만 연결형임.튜플은 ()로 생성, 원소값을 바꿀 수가 없음, 튜플은 딕션너리의 키로 사용이 가능, append나 insert등 과 같은 함수가 없음. 
# t = (1,2,3)
# print(t,type(t))
# #튜플로 사용하려고 할 시 값이 한개여도 (1,) 이런식으로 반드시 콤마를 적어줘야한다 그래야지 튜플로 사용 가능
# t = 1,2,"python" #이런식으로 ()을 생략하고도 생성가능, 원소가 변경이 안되므로 이런식으로 아예 튜플을 다시 재정의는 가능하다.
# print(t,type(t))
#
# print(t[-2],t[-1],t[0],t[1],t[2]) #인덱스와 비슷하므로 이렇게 인덱싱과 슬라이싱이 가능하다.
# print(t[1:3])
# print(t[:])
#
# print(t*2) # 반복
# print(t+(3,4,5)) #이런식으로 연결이 가능
# print(len(t))#요소 개수
# print(5 in t)#내부에 있는지 확인


# #교집합: s1&s2역시 가능, 합집합: s1|s2, 차집합 : s1-s2
# s1 ={1,2,3,4,5,6,7,8,9,10}
# s2 ={10,20,30}
# s3 = s1.union(s2)#합집합
# #s3 = s1 | s2
# print(s3)
#
# s4 = s1.intersection(s2) #교집합
# #s4 = s1 & s2
# print(s4)
#
# s4 = s1.difference(s2)#차집합, s1 -s2도 가능
# print(s4)
#
# s5 = s1.symmetric_difference(s2)#대칭자(둘 모두 속하지 않은 원소 집합)
# print(s5)
#
# print(s1.issuperset(s4))#확대 집합이냐고 묻는것
# print(s5.issuperset(s1))
# print(s2.issubset(s3))#부분 집합이냐고 묻는것


#set에 value 추가 또는 제거
# a ={1,2,3}
#
# a.add(4)# add(x):세트에 x를 추가
# print(a)
# a.remove(3)# remove(x):x를 제거 없으면 오류
# print(a)
# a.discard(2)# discard(x):세트에서 x를 제거, 없으면 무시
# print(a)
# a.update({2,3})# update({set}):세트에 여러개의 값을 추가 , add는 한개지만 세트를 넣으므로 여러개를 넣을 수 있음, 넣은 set안에 값은 알아서 정렬되서 들어감
# print(a)
# a.clear()
# print(a)


# set자료 구조, 순서가 없음->그래서 인덱스로 값을 참조할 수 없으므로 리스트 나 튜플로 변환해서 값을 받을 수 있어야 한다. ,{}로 정의, len(),in,not in 사용,수학의 집합을 사용할 때 사용하는 자료 구조 **중복을 허용하지 않음
#순서가 없기에 sort는 안댐
# set1 ={1,1,2,3} #중복이 안되기에 1,2,3만 뜸
# print(set1)
# 
# print(len(set1))
# print(2 in set1)
# print(2 not in set1)
# 
# set2 ={[4,5,6]} #이런식으로 set안에 리스트를 넣어서 사용 가능 -> 형변환을 명시적으로 해줘야한다.
# print(set2)
# #
# set3 ={"Hello"}#원래는 안에 l이 두개이므로 중복이 안떳는데 이제는 상관없이 뜸
# set3 =set('Hello')#그래서 이렇게 set의 함수를 사용하면 중복이 안뜸
# print(set3)


# # 키값 기반 사용자 정의 정렬
# list =[10,2,22,9,8,33,4,11]
# list1 =['a','A','b','B',"abc",'c',"bc"]
# list.sort(key = str) #문자의 코드로써 1부터 점차 커지기 때문에 문자열 기반 오름차순
# print(list)
# list1.sort(key =str)#아스키코드를 기준으로 오름차순
# print(list1)
#
# list2 =["가","라","하","가가","라라"] #ㄱㄴㄷㄹ기준으로 오름차순
# list2.sort(key = str)
# print(list2)
#
# list.sort(key= int)#정수 숫자로써 오름 차순
# print(list)


# # sort메소드 활용 = 오름 차순인데 reverse를 true로 해주면 내림 차순이됨.
# list =[1,5,3,9,5,8,4,2]
# list.sort()
# print(list)
#
# list.sort(reverse = True)
# print(list)

##리스트의 스택과 큐 활용
# stack =[]
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
#
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack)
#
# queue = []
# queue.append(100)
# queue.append(200)
# queue.append(300)
# print(queue)
#
#
# print(queue.pop(0)) #큐 형태이므로 맨앞의 인덱스를 뽑기위해서 맨앞의 인덱스를 줌.
# print(queue.pop(0))
# print(queue.pop(0))
# print(queue)

# #중요
# a =[1,2,3]
# print(a)
# a.append(5)# append(x) :마지막에 x추가, ex) a.append([5])면 5가 아니라 5를 가진 리스트가 추가됨. ex) [1,2,3,[5,6,7]]이면 이 리스트의 인덱스 갯수는 4임
# print(a)
# a.insert(3,4)# insert(i,x):인덱스 위치에x추가
# print(a)
# a.reverse()# reverse: 역순으로
# print(a)
# a.sort()# sort:순서대로 정렬
# print(a)
# a.remove(3)# remove(i):인덱스 요소를 제거
# print(a)
# a.extend([6,7,8])# extend(l):마지막에 리스트1을 추가
# print(a)
# print(a.index(6))# index(x):없으면 -1반환해서 오류, 인데스 내에 x가있으면 인덱스값 반환
# print(a.count(2))# count(x):x가 몇개가있는지 반환


# # 슬라이스를 이용한 삭제와 삽입
# a =[1,12,123,1234]
# a[1:2] = []
# print(a)
# a[0:]=[]
# print(a)
# #슬라이스를 이용한 삽입
# a =[1,12,123,1234]
#
# a[1:1]=['a']
# print(a)
# a[5:]=[12345]
# print(a)
# a[:0]=[-12,-1,0] #거꾸로 0까지이므로 맨앞에 있는 0인덱스 뒤에 달겟다.
# print(a)


# # 항목의 변경 및 슬라이슬 이용한 치환
# ap = ["apple","banana",10,20]
# ap[2] = ap[2]+90
# print(ap)
# #슬라이스를 이용한 치환의 예
# aa =[1,12,123,1234]
# aa[0:2] = [10,20]
# print(aa)
#
# aa[0:2] = [10] #인덱스 0번째 1번째를 묶어서 10이라고 치환한듯,리스트 슬라이스를 이용했기에 정수가 올 수 없고 오로지 리스트만 올 수 있음.
# print(aa)
#
# aa[1:2] = [20]
# print(aa)
#
# aa[2:3] = [30]
# print(aa)


# #리스트, 연결형인 문자열과는 다르게 자료형이므로 수정,추가,삭제가 가능하다.
# list= [1,2,"python"]
#
# print(list[-2],list[-1],list[0],list[1],list[2])
# print(list[1:3])
# print(list * 2)
# print(list + [3,4,5])#리스트끼리만 더할수있음
# print(len(list))
# print(2 in list)
#
# del(list[1])
# print(list)


# #고급 문자열 포매팅, .format() :문자열의 format을 지정할 수 잇음.
# s = "I have {} apples, and i Ate {} apples."
# print(s.format(5,3)) #얜 빈칸에 순서대로 들어간다는 의미
# s2 = "I have {total} apples, and I ate {num} apples."
# print(s2.format(total = 5, num =3))
# s3 = "I have {total} apples, and I ate {num} apples."
# print(s3.format_map({"total" : 5, "num" : 3}))#얘는 format map이라고 해서 "이름:값" 이 형식으로 값을 줄 수 있음.


#문자열 메서드 :print문을 형식화하여 사용하는 방법, ex)%2.4:정수부 2자리, 소수4자리
# s ="I have %d apples" % 5
# print(s)
# s1 ="interest rate is %f" % 1.24 #float형이므로 소수부 6자리
# print(s1)
# s2 ="interest rate is %2.4f" %1.24 #2,4f : 정수부 2자리, 소수부 4자리
# print(s2)


# #문자열 판별 관련 메소드
# print("1234".isdigit()) #문자열이 숫자로 되어있는가를 여부를 반환, 결과는 boolean값으로
# print('abcd'.isalpha()) #문자열이 알파벳이냐
#
# print('1234'.isalpha())
# print('abcd'.isdigit())
#
# print('abcd'.islower())#문자열이 소문자냐
# print('ACCD'.isupper())#문자열이 대문자냐
#
# print("\n\n".isspace())#공백이냐
# print(" ".isspace())
# print("".isspace())#여긴 공백 x


#문자열 분리 나누기
# s ="spam and ham"
# t =s.split() # 문자열을 공백문자 또는 지정된 문자로 분리, split으로 나눠진 문자들은 리스트 형태로 들어감.
# print(t)
# t = s.split('and' )
# print(t)
#
# s2 = ":".join(t)#지정된 기호로 합침
# print(s2)
#
# s3 = "one:two:three:four:five"
# print(s3.split(":",2))#2개만 나눠 보겠다
# print(s3.rsplit(":",2))#오른쪽부터 2개만 나눔
#
# lines = '''lst line
# 2nd line
# 3rd line
# '''
#
# print(lines.splitlines())#라인 단위로 문자열을 나눔


# #문자열 정렬
# s ="Alice and the Heart Queen"
#
# print(s.center(60))#문자열 가운데로 정렬, 인자로 넓이를 지정,채울 문자 선택가능
# print(s.center(60,'-'))#문자열 가운데로 정렬, 인자로 넓이를 지정,채울 문자 선택가능
#
# print(s.rjust(60,'-'))#우측 정렬
# print(s.ljust(60,'-'))#좌측 정렬
# print('20'.zfill(5))#자리수를 지정하고 빈공간을 0으로 채울 (정렬 기능)
# print('1234'.zfill(5))


# #문자열 공백
# s = " spam and ham "
# print(s.strip()) #문자열내 좌우 공백문자 제제
# print(s.rstrip()) #문자열 내 오른쪽 공백 제거
# print(s.lstrip())#문자열 내 왼쪽 공백 제거
#
# s="<><abc><><defg><><>"
# print(s.strip("<>")) #인자로 패턴을 주면 문자열 앞뒤로 들어있으면 조합해서 지워버림
#
# s = "Hello Java"
# print(s.replace("Java", "Python")) #문자열의 단어를 대체


# #검색관련 메소드
# s= "I Like Python, I Like Java Also"
#
# print(s.count("Like")) #문자열 내 검색어 갯수 반환
# print(s.find("Like",5)) # 문자열 내 첫번쨰 검색된 위치의 인덱스 반환,  요건 인덱스 5부터 검색
# print(s.find("JS"))#없으니까 -1을 반환한듯
# print(s.rfind("Like"))
#
# print(s.index("Java")) #문자열 내 검색된 위치의 인덱스 반환
# print(s.rindex("Like"))#오른쪽부터 인덱스 검색
#
# print(s.startswith("I Like"))#starswith : 특정문자열로부터 시작
# print(s.startswith("Like",2))
# print(s.endswith("Also"))#이 값으로 끝나는지
# print(s.endswith("Java",0,26))

#문자열 변환 메소드
# s = "I like Python"
# print(s.upper()) #모두다 대문자
# print(s.lower()) #모두다 소문자
# print(s.swapcase())#대문자는 소문자로 소문자는 대문자
# print(s.capitalize()) #맨 첫번째만 대문자
# print(s.title()) #각 단어으이 첫번째들만 대문자로


# #문자열 인덱싱,슬라이싱, 시퀀스형 자료형은 인덱스하나하나를 바꾸지 못함 ex)str[0] ="l" 이게 불가능
# str ="Life is too short, You need Python!"
# print(len(str))
# #[a:b] : a이상 b미만, 거꾸로는 끝에서부터 -1로 세면됨.
# print(str[2])
# print(str[8:11])
# print(str[-7:-1])
# print(str[5:])
# print(str[-3:])
# print()
# # str2 ="헬로 월드"
# # print(str2[0:2])#파이썬은 한글이라고 유니코드처럼 끊는거 없이 잘 출력됨


#문자열은 연결(+) , 반복(*) 연산이 가능,  문자열 객체와 수치형 객체는 + 연산을 할 수 없다. ex) "python" + 3
# firstname = "seung Kyun"
# lastname = "Nam"
# fullname = firstname + " " + lastname #  " "은 한칸 띄어준것.
# print(fullname)
# print(firstname,lastname)
#
# laugh = "Ha"
# print(laugh * 3)


# str3="""asdsadsadsadasdasd
# asdasdsad
# sadasdsad"""
# str2 ="asdad" \
#       "asda" \
#       "asdwd" \
#       "sd"
# print(str3)