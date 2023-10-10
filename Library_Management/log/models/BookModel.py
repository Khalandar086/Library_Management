

from flask_login import UserMixin

from util.db import DBConnection

from util.queries import GET_USER_BY_ID,GET_USER_BY_TITLE,INSERT_BOOKS,GET_BOOKS,GET_BOOK_BY_ID,update_book




class BookModel(UserMixin):

    def __init__(self,id,title,author,total_copies,available_copies=None,bought_on=None,created_by=None):
        self.id=id
        self.title = title
        self.author = author
        self.total_copies=total_copies
        self.available_copies=available_copies
        self.bought_on=bought_on
        self.created_by=created_by

    @staticmethod
    def create_book(title,author,total_copies,current_user_id):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(INSERT_BOOKS, (title, author, total_copies,total_copies,current_user_id))
            conn.commit()
            curr.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Exception Handled in employee_registration POST block- {e}")
            return False

    @classmethod
    def get_books(cls):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(GET_BOOKS)
            data=curr.fetchall()
            curr.close()
            conn.close()
            books = []
            for book in data:
                b=BookModel(book[0],book[1],book[2],book[3],book[4],book[5],book[6])
                books.append(b)
            return books
        except Exception as e:
            print(f"Exception Handled in employee_registration POST block- {e}")
            return False

    @classmethod
    def GET_BOOK_BY_ID(cls,id):
        conn=DBConnection.get_conn()
        curr=conn.cursor()
        curr.execute(GET_BOOK_BY_ID,(id,))
        books=curr.fetchone()
        b=None
        if books:
            b = BookModel(id,books[0], books[1], books[2])
        curr.close()
        conn.close()
        return b

    @staticmethod
    def update_book(title, author, total_copies,current_user_id):
        conn = DBConnection.get_conn()
        curr = conn.cursor()
        curr.execute(update_book, (title, author, total_copies,current_user_id))
        conn.commit()
        curr.close()
        conn.close()
        return True










