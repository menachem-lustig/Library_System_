from logic_functions import display_books,play_search_book,play_add_book,play_book_by_author,play_borrow_book,play_return_book,get_available_books


def menu():

    print("""
================================
       LIBRARY MANAGEMENT
================================

1. Display all books
2. Search book by name
3. Add new book
4. Borrow a book
5. Return a book
6. Display available books
7. Display books by author
8. Exit

Choose an option:
""")

def main():
    is_active = True
    while  is_active:
        menu()
        choice =  input('Enter your option: ')
        if choice == '1':
            display_books()
        elif choice =='2':
            play_search_book()
        elif choice == '3':
            play_add_book()
        elif choice == '4':
            play_borrow_book()
        elif choice == '5':
            play_return_book()
        elif choice == '6':
            get_available_books()
        elif choice == '7':
            play_book_by_author()
        elif choice == '8':
            print('Goodbye')
            is_active = False
        else:
            print('Invalid choice,try again')




main()



