import sqlite3
class C:
    def __init__(self):
        conn = sqlite3.connect("test1.db")
        conn.execute("CREATE TABLE book(no integer primary key autoincrement,title text not null, price integer)")
        conn.commit()

