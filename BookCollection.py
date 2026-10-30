#Author: Leala Laukkonen
#Date: October 10th, 2026
TITLE="title"
AUTHOR="author"
GENRE="genre"
ISBN="isbn"
TAGS="tags"

collection=[]

def add_book(collection, title, author, genre, isbn, tags):
    isbn_check=False
    for book in collection:
        if book[ISBN]==isbn:
            isbn_check=True
            break
    if isbn_check:
        print("This ISBN already exists.")
        return
    book={}
    book[TITLE] = title
    book[AUTHOR] = author
    book[GENRE] = genre
    book[ISBN] = isbn
    book[TAGS] = set(tags)
    collection.append(book)
                                                                                                            #examples for testing
add_book(collection, "The Hunger Games", "Suzanne Collins", "Dystopian", "9780439023528", {"sci-fi", "political", "violence"})
add_book(collection, "The Hobbit", "JRR Tolkien", "Fantasy", "9780547928227", {"epic", "high fantasy", "classic"})
add_book(collection, "A Game of Thrones", "George RR Martin", "Fantasy", "9780553381689", {"long", "violence", "political"})
add_book(collection, "IT", "Stephen King", "Horror", "9781501142970", {"long", "classic", "coming-of-age"})
add_book(collection, "Pride and Prejudice", "Jane Austen", "Romance", "9781435159631", {"historic", "classic"})
add_book(collection, "The Murderbot Diaries", "Martha Wells", "Science Fiction", "9781250389824", {"comedic", "mystery", "action"})

def tags_to_books(collection, tags):
    books=[]
    for book in collection:
        if tags.issubset(book[TAGS]):
            books.append(book[TITLE])
    return books

def get_book(collection, isbn):
    for book in collection:
        if book[ISBN] == isbn:
            return book[TITLE], book[AUTHOR]
    return()


add_book(collection, "IT", "Stephen King", "Horror", "9781501142970", {"long", "classic", "coming-of-age"})
assert len(collection)==6                                                                                  #no errors
assert get_book(collection, "123456")==()
assert get_book(collection, "9781501142970")==("IT", "Stephen King")
assert tags_to_books(collection, {"sci-fi", "political"})==["The Hunger Games"]
assert tags_to_books(collection, {"3rd-person"})==[]

