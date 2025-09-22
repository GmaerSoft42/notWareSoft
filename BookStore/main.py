import database
data = database.DataBase()
#member = Member()

class Member():
    def __init__(self, name, surname, borrowed):
        self.name = name
        self.surname = surname
        self.borrowed = borrowed
    def list_members(self):
        lists = data.fetch("members")
        return lists
    
class Books():
    def __init__(self, title, isbn, edition):
        self.title = title
        self.isbn = isbn
        self.edition = edition
    def list_books(self):
        lists = data.fetch("books")
        return lists