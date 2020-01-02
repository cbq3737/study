#사각형의 넓이와 학생의 나이를 더해보자, 아예 클래스 내부의 형태가 서로 다르더라도 __add__에 같은 변수만 통한다면 서로 더해줄수 있다.
from Shape import * #만일 뒤에 import에 일부만 갖고오고싶다면 class는 class전체를 갖고가야됌,그 안에 있는 함수만 따로 나눌수 없다. 하지만 함수가 독립적으로 정의되어있다면 그 함수는 가져올수 있다.
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
        return self.age + other.area

s1 = Student("최범규",201455050,"ICT",25) #25
r1 = Rect(10,20) #200
print(s1+r1)


#myadd_import.py
#Shape클래스 사용
# from Shape import * #각각 다른 클래스들끼리의 합
#
# r1 =Rect(10, 20) #200
# r2 =Rect(10, 10) #100
#
# t1 = Tri(10, 20) #100
# t2 = Tri(10, 10) #50
#
# print(r1+r2)
# print(t1+t2)
# print(r1+t2)
#
