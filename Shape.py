import math
class Rect:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.area = height*width

    def __str__(self):
        return "넓이는 %s, 높이는 %s, 넓이는 %d"% (self.width,self.height,self.area) #이 초기화때 각각의 클래스의 넓이를 변수에 할당해주었으므로 다른 클래스끼리의 넓이 합도 가능하다.

    def info(self):
        print(self)

    def __add__(self,other):
        return "넓이의 합은 %d"%(self.area+other.area)

class Tri:
    def __init__(self,a1,a2):
        self.a1 = a1;
        self.a2 = a2;
        self.area = a1 * a2 * 1/2

    def info(self):
        print(self)

    def __str__(self):
        return "높이는 %s, 밑변 %s, 넓이는 %d" % (self.a1, self.a2,self.area )

    def __add__(self,other):
        return"넓이의 합은 %d"%(self.area+other.area)

class Circle:
    def __init__(self,r1):
        self.r1 = r1;
        self.area =(self.r1 **2) * math.pi

    def info(self):
        print(self)

    def __str__(self):
        return "반지름는 %s, 넓이는 %d" % (self.r1,self.area )

    def __add__(self,other):
        return "넓이의 합은 %d"%(self.area+other.area)