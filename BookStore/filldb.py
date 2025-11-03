from olclient import OpenLibrary
import database
import requests
data = database.DataBase()
ol = OpenLibrary()
print("*** DATABASE FILLING PROGRAM ***")
print("This program will fill the database with random books for the demo of the BOOKSTORE")
search = ol.Author.search("Victor Hugo")
for x in search:
    print(x)
search1 = ol.Work.search("Les Misérables")
search3 = ol.get(f"/isbn_139782211238645")
#search2 = ol.Edition.get("9782211238645")
print("UP ")
print(search1)
print(search3)
print(search1.authors)
limit = int(input("How many books? "))
offset = int(input("Offset? "))
params = {
        'q': 'language:fre',
        'limit': limit,
        'offset': offset,
        'fields': 'title,author_name,first_publish_year,key,edition_count'
    }
resp = requests.get('https://openlibrary.org/search.json', params=params).json()
#subjects = [ "french"]
#for subject in subjects:
#    data = requests.get(f"https://openlibrary.org/search.json?q=language:fre&limit=100&offset=0&fields=title,author_name,first_publish_year,key,edition_count").json()
print(resp)
input("Press ENTER to continue... [2]")
for x in resp:
    print(x)
input("Press ENTER to continue... [3]")
#search1 = ol.Work.search("Les Misérables")
#title = search1.title
#author = search1.authors[0]['name']
#olid = search1.authors[0]['olid']
#print("DOWN")
#print(title)
#print(author)
#print(olid)
authorstr = ""
for doc in resp["docs"]:
    authorstr = ""
    print(doc["author_name"])
    print(doc["key"][7:]) #OLID
    print(doc["title"])
    authors = doc["author_name"]
    if len(authors) > 1:
        for x in doc["author_name"]:
            authorstr += f"{x}, "
    else:
        authorstr = doc["author_name"][0]
    data.add_books(doc["title"], authorstr, doc["key"][7:],"Standard Edition")
    print("END OF CURRENT BOOK, NEXT LINE IS ANOTHER BOOK")
