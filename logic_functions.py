from books import books
from validation_input import valid_int,valid_str


def display_books():
    for book in books:
        print(book)

def search_book_by_name(books, name):
    found_books = []
    for book in books:
        if book['name'][:len(name)].lower() == name.lower():
            found_books.append(book)
    return found_books

def search_book_by_id(books, user_id):
    for book in books:
        if book ['id'] == user_id:
            return book



def play_search_book():
    name = valid_str('Enter the book name: ')
    book = search_book_by_name(books,name)
    if book:
        print(book)
    else:
        print('The book not found.')

def uniq_id():
    max_book = max(books,key= lambda b:b['id'])
    return max_book['id'] +1

def add_book(books, name, author, year):
    try:
        book = {"id": uniq_id(), "name": name, "author": author, "year": year, "available": True}
        books.append(book)
        return True
    except Exception as e:
        print(e)
        return False

def book_is_exist(name,author):
    for book in books:
        if book['name'] == name and book['author'] == author:
            return True
        
def play_add_book():
    name = valid_str('Enter Tha book name: ')
    author = valid_str('Enter the author name: ')
    year = valid_int ('Enter the year the book was written: ')
    if book_is_exist(name,author):
        print('Book already exist.')
    else:
        add_book_check = add_book(books,name,author,year)
        if add_book_check:
            print('Book added successfully.')
        else:
            print('Cannot add book')

def borrow_book(books, book_id):
    try:
        book = search_book_by_id(books,book_id)
        if book:
            book ['available'] = False
            return True
        else:
            print('Book not founded')
    except Exception as e:
        print(e)
        return False

def play_borrow_book():
    book_id = valid_int('Enter book id: ')
    borrow_book_check = borrow_book(books,book_id)
    if borrow_book_check:
        print('The book borrowed successfully')
    else:
        print('cannot borrowed this book')


def return_book(books, book_id):
    try:
        book = search_book_by_id(books,book_id)
        if book:
            book ['available'] = True
            return True
        else:
            print('Book not founded')
    except Exception as e:
        print(e)
        return False
    
def play_return_book():
    book_id = valid_int('Enter book id: ')
    borrow_book_check = borrow_book(books,book_id)
    if borrow_book_check:
        print('The book returned successfully')
    else:
        print('cannot return this book')

def get_available_books():
    available_books = []
    for book in books:
        if book['available']:
            available_books.append(book)
    return available_books

def get_books_by_author(books, author):
    books_list = []
    for book in books:
        if book['author'].lower() == author.lower():
            books_list.append(book)
    return books_list
    
def play_book_by_author():
    author = valid_str('Enter the author name: ')
    print(get_books_by_author(books,author))

