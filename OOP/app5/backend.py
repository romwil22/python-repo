import sqlite3

class Database:
    
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (book_id INTEGER PRIMARY KEY, title TEXT,author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        
    def insert(self,t,a,y,i):
        self.cur.execute("INSERT INTO book (title,author,year,isbn) VALUES (?,?,?,?)",(t,a,y,i))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        
        return rows

    def search(self,t="",a="",y="",i=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(t,a,y,i))
        rows = self.cur.fetchall()
        
        return rows

    def update(self,bi,t,a,y,i):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE book_id=?",(t,a,y,i,bi))
        self.conn.commit()

        
    def delete(self,i):
        self.cur.execute("DELETE FROM book WHERE book_id=?",(i,))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()


