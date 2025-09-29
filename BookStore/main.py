import database
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
class Books():
    def __init__(self, title, author, isbn, edition):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.edition = edition
        data.create_table_books()
    def list_books(self):
        lists = data.fetch("books")
        return lists
    def add_book(self):
        data.add_books(self.title, self.author, self.isbn, self.edition)
    def update_book(self):
        data.update_books(self.title, self.author, self.isbn, self.edition)        
book = Books("Les Misérables", "Victor Hugo", "978-2-211-23864-5", "Édition de Référence")
book.add_book()
book.title = 'Les Mis'
input("Press ENTER to continue...")
book.update_book()
memb = Member("Jean", "France", "Paul-Sartre Jean: L'être et le néant.")
memb.add_member()
memb.update_member()