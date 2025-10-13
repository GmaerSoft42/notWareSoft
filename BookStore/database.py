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
    def add_members(self, name, surname):
        self.cursor.execute("""INSERT INTO members
                            (NAME, SURNAME, BORROWED)
                            values (?, ?, ?)        
                            """, (name, surname, None))
        self.connection.commit() # If your database stops working for no explaiable reason, make sure you commit your changes
    def update_members(self, borrowed, name):
        self.cursor.execute("""UPDATE members 
            SET BORROWED = ?
        WHERE NAME LIKE ?;""", (borrowed, name))
        self.connection.commit()
    def fetch_member(self, name):
        self.cursor.execute(f"""SELECT ID FROM books
                            WHERE NAME LIKE ?;
        """, (name,))
        rows = self.cursor.fetchall()
        return rows
    def create_table_borrowed_books(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS borrowed (
            id integer primary key autoincrement,
            member_id integer,
            book_id integer,
            BORROWED_DATE text, 
            RETURNDATE text,
            RETURN_STATUS int,
            FOREIGN KEY(member_id) REFERENCES members(member_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
        );""")  # BORROWED = date when it was borrowed
    def create_table_books(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS books (
            book_id integer primary key autoincrement,
            NAME text,
            AUTHOR text,
            ISBN text,
            EDITION text,
            IS_BORROWED integer default 0
        );""")      
    def add_books(self, name, author, isbn, edition):
        self.cursor.execute("""INSERT INTO books
                            (NAME, AUTHOR, ISBN, EDITION, IS_BORROWED)
                            values (?, ?, ?, ?, 0)     
                            """, (name, author, isbn, edition))
        self.connection.commit() # Will have to change to make it the correct values
    def update_books(self, name, author, isbn, edition, status):
        self.cursor.execute("""UPDATE books 
            SET NAME = ?,
                AUTHOR = ?,
                ISBN = ?,
                EDITION = ?,
                IS_BORROWED = ?
        WHERE NAME LIKE ?;""", (name, author, isbn, edition, status, name))
        self.connection.commit()
    def fetch_book_id(self, name):
        self.cursor.execute(f"""SELECT ID FROM books
                            WHERE NAME LIKE ?;
        """, (name,))
        rows = self.cursor.fetchall()
        return rows        
    def fetch_status(self, name):
        self.cursor.execute(f"""SELECT IS_BORROWED FROM books
                            WHERE NAME LIKE ?;
        """, (name,))
        rows = self.cursor.fetchall()
        return rows
    def fetch(self, tablename):
        self.cursor.execute(f"""SELECT * FROM {tablename}
        """)
        rows = self.cursor.fetchall()
        return rows