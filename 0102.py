
# from peewee import *
# db = SqliteDatabase('peewee1.db')
#
# class Book(Model):
#     no = IntegerField(primary_key=True)
#     title = CharField()
#     price = IntegerField()
#
#     class Meta:
#         database = db
# db.connect()
# db.create_tables([Book])
#
# b1= Book.create(no=1, title = "Python",price = 20000)
# b1.save()
# b1 = Book.create(no=2, title ="C++",price = 30000)
# b1.save()
# for book in Book.select():
#     print("%5d %10s %8s"%(book.no,book.title,book.price))
# db.close()


# import sqlite3
# from SQLiteC import C
# from SQLite import Select
# from SQLiteInsert import insert
#
# conn = sqlite3.connect("test1.db")
# a = C()
# insert.IN1(11, 'C#', 20000)
#
# f = open("asdf1.txt",'w',encoding='utf-8')
# cursor = Select.SEL()   #cursor로 배열을 넘겨줌,
#
# for i in cursor:
#
#     f.write(str(i)+"\n")
# conn.close()
# f.close()


# import sqlite3
# from sqlite3 import Error
# conn = sqlite3.connect("test1.db") #db에 연결
# conn.execute("CREATE TABLE book(no integer primary key autoincrement,title text not null, price integer)") #book이라는 테이블을 갖는 테이블을 만드는데 거기안에 필드명을 정해준다.필드명 마다 어떤값이 오는지 어떤 속성인지 적어줌
# conn.execute("INSERT INTO book(no,title,price) VALUES (4,'C++',20000)") #테이블에 필드에따라 필드값을 삽입시켜 넣어줌.
# conn.execute("INSERT INTO book(no,title,price)VALUES (5,'python',30000)") #이 코드를 또 넣을거라면 위에 생성해주는 코드를 주석해준뒤 삽입시키면 된다.
# conn.commit()#제출
#
# #여기까지가 테이블을 만들고 값을 집어넣은것.
# cursor = conn.execute("SELECT * FROM book")#book테이블에서 무엇을찾을지 알려줌.
# for book in cursor.fetchall():
#     print(book)
#
# conn.close()


# 웹크롤링:수집->분석->추출->가공->저장, crawl1파일->IDLE


# 사각형의 넓이와 학생의 나이를 더해보자, 아예 클래스 내부의 형태가 서로 다르더라도 __add__에 같은 변수만 통한다면 서로 더해줄수 있다.
# from Shape import * #만일 뒤에 import에 일부만 갖고오고싶다면 class는 class전체를 갖고가야됌,그 안에 있는 함수만 따로 나눌수 없다. 하지만 함수가 독립적으로 정의되어있다면 그 함수는 가져올수 있다.
# class Student:
#     def __init__(self,name,snumber,major,age):
#         self.name = name
#         self.snumber = snumber
#         self.age =age
#         self.major= major
#
#     def __str__(self):
#           return "이름: %s , 학번: %d ,학과: %s,나이: %d" %(self.name,self.snumber,self.major,self.age)
#
#     def info(self):
#         print(self)
#
#     def __add__(self, other):
#         return self.age + other.area
#
# s1 = Student("최범규",201455050,"ICT",25) #25
# r1 = Rect(10,20) #200
# print(s1+r1)


# myadd_import.py
# Shape클래스 사용
# from Shape import * #각각 다른 클래스들끼리의 합
# 
# r1 =Rect(10, 20) #200
# r2 =Rect(10, 10) #100
# 
# t1 = Tri(10, 20) #100
# t2 = Tri(10, 10) #50
# 
# if __name__ =="__main__":   #이렇게 되면 만일 이 0102파일이 직접 실행되는 경우 __name__에 __main__이 저장되고, 다른 모듈에서 0102파일을 import를 할 경우엔 __name__이름에 0102의 이름값이 저장된다.
#     print(r1+r2)
# 
# print(t1+t2)
# print(r1+t2)
