import sqlite3
class Select:
    def SEL():
        conn = sqlite3.connect("test1.db")
        cursor = conn.execute("SELECT * FROM book")
        a= cursor.fetchall()
        for book in a:
            print(book)
        return a