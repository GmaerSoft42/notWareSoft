import database
import datetime
import os
data = database.DataBase()
today = datetime.datetime.now()
today = today.strftime("%d/%m/%Y")
def clear():
    #return # uncomment this line if you want to debug
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
class Member():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #self.borrowed = borrowed
        #self.member_id = member_id
        data.create_table_members()
    def list_members(self):
        lists = data.fetch("members")
        return lists
    def add_member(self):
        data.add_members(self.name, self.surname)
    #def update_member(self):
    #    data.update_members(self.borrowed, self.name)
    def get_member_id(self):
        fetchmember = data.fetch_member(self.name)
        if fetchmember:
            return fetchmember
        else:
            return "Get Member ID hasn't returned anything :("
    def get_borrowed_books(self):
        fetchbooks = data.member_borrowed_books(self.name)
        return fetchbooks
class Books():
    def __init__(self, title, author, olid, edition):
        self.title = title
        self.author = author
        self.olid = olid
        self.edition = edition
        self.status = self.get_status()
        data.create_table_books()
    def list_books(self):
        lists = data.fetch("books")
        return lists
    def get_book_id(self):
        getbookid = data.fetch_book_id(self.title)
        if getbookid:
            return getbookid[0][0]
    def add_book(self):
        data.add_books(self.title, self.author, self.olid, self.edition)
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
        data.update_books(self.title, self.author, self.olid, self.edition, self.status)        
def check_member(name):
    if data.fetch_member(name) == 1:
        return False
    else:
        return True
def check_book(title):
    if data.fetch_book_id(title) == 1:
        return False
    else:
        return True
def check_availability(title):
    if data.fetch_status(title) == 1:
        return False
    else:
        return True
while True:
    try:
        #clear()
        print("*** BOOK SORTING SYSTEM ***")
        print("© GmaerSoft42 and the GmaerSoft42 Porcoration")
        print("[1] Sign up a member")
        print("[2] Sign in a member")
        print("[3] Select a book")
        print("[4] Borrow selected book")
        print("[5] Return selected book")
        print("[6] Clear borrowed table")
        print("[7] List all books")
        print("[8] Quit program")
        option = input("Please select an option: ")
        if option == "1":
            name = input("Please enter the name of the upcoming member: ")
            surname = input("Please enter the surname of the upcoming member: ")
            if not check_member(surname):
                data.add_members(name, surname)
                input("Added member successfully (don't forget to sign in). Press ENTER to continue...")
            else:
                input("Member already exists (did you mean sign in?)! Press ENTER to continue")
        if option == "2":
            name = input("Please enter the member's name: ")
            surname = input("Please enter the member's surname: ")
            if check_member(surname):
                memb = Member(name, surname)
                input("Successfully signed in member. Press ENTER to continue...")
            else:
                input("Cannot find member in database! Make sure the member is signed up for the library, then try again. Press ENTER to continue...")
        if option == "3":
            title = input("Please enter the title of the book: ")
            if check_book(title):
                if check_availability(title):
                    book = Books(title, "None", "None", "None")
                    input("Selected book successfully. Press ENTER to continue...")
                else:
                    input("Book is already borrowed! Please return this book and/or select another book. Press ENTER to continue")
            else:
                input("Cannot find book in database! Make sure you typed the title of the book correctly, alternatively this book may not be present in this library. Press ENTER to continue...")
        if option == "4":
            if not check_member(memb.name):
                input("You are not signed in! Please sign-in first before any operations. Press ENTER to continue...")
            else:
                add_to_history = data.add_borrow_list(str(memb.get_member_id()), str(book.get_book_id()), today, input("Enter return date (in DD/MM/YYYY): "), False,)
                if add_to_history == 1:
                    input("This book is already borrowed! Please select another book. Press ENTER to continue...")
                else:
                    book.update_status()
                    book.update_book()
                    input("Book borrowed. Press ENTER to continue...")
        if option == "5":
            if not check_member(memb.name):
                input("You are not signed in! Please sign-in first before any operations. Press ENTER to continue...")
            else:
                book.update_status()
                book.update_book()
                data.return_borrow_list(book.get_book_id())
                input("Returned book successfully. Please select another book or exit this program. Press ENTER to continue...")
        if option == "6":
            confirmation = input("This will COMPLETELY ERASE the BORROWED table in the DATABASE. Are you sure? [Y/N]: ")
            if confirmation == "Y":
                data.clear_borrowed()
                input("Cleared borrowed table. Press ENTER to continue...")
        if option == "7":
            for x in data.fetch("books"):
                print(x)
            input("Press ENTER to continue...")
        if option == "8":
            exit()
    except (KeyboardInterrupt, EOFError, SystemExit):
        print("User has chosen to exit. Exiting...")
        exit()
    except Exception as e:
        print(f"STOP: 0281\nAn error has occured in this program. Review the GamerSoft24/Software PySoft error chart and the Python manual for more information about this error using the error details as guidance, and try again. If problems persist, contact the program vendor.\nDetails: {e}")
        input("Press ENTER to return to the program. For stability, you should re-sign-in your member and re-select your book.")