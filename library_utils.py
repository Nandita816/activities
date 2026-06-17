def search_book(book_list, book_id):
    for book in book_list:
        if book.book_id == book_id:
            return book
    return None


def count_available_books(book_list):
    count = 0
    for book in book_list:
        if not book.is_issued:
            count += 1
    return count


def display_all_books(book_list):
    if len(book_list) == 0:
        print("No books available in library.")
        return

    print("\n===== ALL BOOKS =====")
    for book in book_list:
        book.display()