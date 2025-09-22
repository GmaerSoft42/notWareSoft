import sqlite3
class DataBase():
    def __init__(self,):
        self.cursor, self.connection= self.connect()
        self.create_table_members()
        self.create_table_books()
        self.create_table_borrowed_books()
    def connect(self):
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        return cursor,connection
    def create_table_members(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS members (
            member_id integer primary key autoincrement,
            NAME text,
            SURNAME text,
            BORROWED text
        );""")    
    def create_table_borrowed_books(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS borrowed (
            id integer primary key autoincrement,
            member_id integer,
            book_id integer,
            BORROWED text,
            RETURNDATE text,
            RETURNED int,
            FOREIGN KEY(member_id) REFERENCES members(member_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
        );""")  # RETURNED = if book has been returned
    def create_table_books(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books (
            book_id integer primary key autoincrement,
            NAME text,
            ISBN text,
            EDITION text
        );""")      
    def fetch(self, tablename):
        self.cursor.execute(f"""SELECT * FROM {tablename}
        """)
        rows = self.cursor.fetchall()
        return rows