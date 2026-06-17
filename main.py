from book import Book
from library_utils import (
    search_book,
    count_available_books,
    display_all_books
)

book_list = []

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Count Available Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        new_book = Book(book_id, title, author)
        book_list.append(new_book)

        print("Book added successfully!")

    elif choice == "2":

        display_all_books(book_list)

    elif choice == "3":

        book_id = int(input("Enter Book ID to issue: "))

        book = search_book(book_list, book_id)

        if book:
            book.issue_book()
        else:
            print("Book not found.")

    elif choice == "4":

        book_id = int(input("Enter Book ID to return: "))

        book = search_book(book_list, book_id)

        if book:
            book.return_book()
        else:
            print("Book not found.")

    elif choice == "5":

        book_id = int(input("Enter Book ID to search: "))

        book = search_book(book_list, book_id)

        if book:
            print("\nBook Found")
            print("----------")
            book.display()
        else:
            print("Book not found.")

    elif choice == "6":

        available_books = count_available_books(book_list)

        print("Available Books:", available_books)

    elif choice == "7":

        print("Thank you for using Library Management System.")
        break

    else:

        print("Invalid choice! Please try again.")