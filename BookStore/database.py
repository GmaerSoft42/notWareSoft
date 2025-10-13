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
            SURNAME text
        );""")    
    def add_members(self, name, surname):
        self.cursor.execute("""INSERT INTO members
                            (NAME, SURNAME)
                            values (?, ?)        
                            """, (name, surname, ))
        self.connection.commit() # If your database stops working for no explaiable reason, make sure you commit your changes
    #def update_members(self, borrowed, name):
    #    self.cursor.execute("""UPDATE members 
    #        SET BORROWED = ?
    #    WHERE NAME LIKE ?;""", (borrowed, name))
    #    self.connection.commit()
    def fetch_member(self, name):
        self.cursor.execute(f"""SELECT member_id FROM members
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
    def add_borrow_list(self, member_id, book_id, borrowed_date, returndate, return_status,):
        self.cursor.execute("""SELECT RETURN_STATUS FROM borrowed
                            WHERE book_id like ?
                            """, (book_id,))
        rows = self.cursor.fetchall()
        print("DEBUG: VARIABLES IN DATABASE.PY ADD BORROW LIST FUNC TION")
        print(book_id)
        print(rows)
        if (0,) in rows:
            print("You ain't supposed to borrow that kid!")
            return "You ain't supposed to borrow that kid!"
        self.cursor.execute("""INSERT INTO borrowed
                            (member_id, book_id, BORROWED_DATE, RETURNDATE, RETURN_STATUS)
                            values (?, ?, ?, ?, 0)     
                            """, (member_id, book_id, borrowed_date, returndate, ))
        self.connection.commit() # Will have to change to make it the correct values
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
        self.cursor.execute("""SELECT 1 FROM books
                    WHERE NAME = ?
                            """, (name,))
        rows = self.cursor.fetchall()
        if not rows:
            self.cursor.execute("""INSERT INTO books
                                (NAME, AUTHOR, ISBN, EDITION, IS_BORROWED)
                                values (?, ?, ?, ?, 0)     
                                """, (name, author, isbn, edition))
            self.connection.commit() # Will have to change to make it the correct values
    def member_borrowed_books(self, name):

        self.cursor.execute("""SELECT member_id FROM members
                                WHERE NAME LIKE ? 
                            """, (name,))
        rows = self.cursor.fetchall()
        if not rows:
            return
        else:
            member_id = rows[0][0]
        self.cursor.execute("""SELECT book_id FROM borrowed
                                WHERE member_id LIKE ? and RETURN_STATUS is 0
                            """, (member_id,))
        rows = self.cursor.fetchall()
        return rows

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
        self.cursor.execute(f"""SELECT book_id FROM books
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