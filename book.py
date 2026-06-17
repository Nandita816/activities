class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def issue_book(self):
        if self.is_issued:
            print("Book is already issued.")
        else:
            self.is_issued = True
            print("Book issued successfully.")

    def return_book(self):
        if not self.is_issued:
            print("Book was not issued.")
        else:
            self.is_issued = False
            print("Book returned successfully.")

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("----------------------")