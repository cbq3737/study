import sqlite3
class insert:
    def IN1(no,title,price):
        conn = sqlite3.connect("test1.db")
        conn.execute("INSERT INTO book(no,title,price) VALUES (%d,'%s',%d)" %(no,title,price))
        conn.commit()