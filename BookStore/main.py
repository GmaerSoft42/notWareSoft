import database
import time
data = database.DataBase()



class Member():
    def __init__(self, name, surname, borrowed):
        self.name = name
        self.surname = surname
        self.borrowed = borrowed
        #self.member_id = member_id
        data.create_table_members()
    def list_members(self):
        lists = data.fetch("members")
        return lists
    def add_member(self):
        data.add_members(self.name, self.surname)
    def update_member(self):
        data.update_members(self.borrowed, self.name)
    def get_member_id(self):
        return data.fetch_member(self.name)[0][0]
class Books():
    def __init__(self, title, author, isbn, edition):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.edition = edition
        self.status = self.get_status()
        data.create_table_books()
    def list_books(self):
        lists = data.fetch("books")
        return lists
    def get_book_id(self):
        return data.fetch_book_id(self.title)[0][0]
    def add_book(self):
        data.add_books(self.title, self.author, self.isbn, self.edition)
    def get_status(self):
        return data.fetch_status(self.title)
    def update_status(self):
        if self.get_status()[0][0] == 0:
            print("the status has been correctly verified")
            self.status = 1
        else:
            self.status = 0
    def update_book(self):
        print("the book has been updated (at least in theory from the user main.py side)")
        data.update_books(self.title, self.author, self.isbn, self.edition, self.status)        
book = Books("Les Misérables", "Victor Hugo", "978-2-211-23864-5", "Édition de Référence")
book.add_book()
print(book.get_status())
input("Press ENTER to continue...")
book.update_status()
#input("Press ENTER to continue...")
book.update_book()
memb = Member("Jean", "France", "Paul-Sartre Jean: L'être et le néant.")
memb.add_member()
memb.update_member()
data.add_borrow_list(memb.get_member_id, book.get_book_id, time.asctime()[0:10] + " " + time.asctime()[-4:], "06/07/2027", False)