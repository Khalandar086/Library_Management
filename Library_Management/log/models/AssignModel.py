from flask_login import UserMixin

from util.db import DBConnection
from util.queries import INSERT_Assign

class AssignModel(UserMixin):

    def __init__(self,student_id,book_id,issued_date=None,return_date=None,emp_id=None):
        self.student_id=student_id
        self.book_id=book_id
        self.issued_date =issued_date
        self.return_date=return_date
        self.emp_id=emp_id

    @staticmethod
    def create_assign(student_id,book_id):
        try:
            conn = DBConnection.get_conn()
            curr = conn.cursor()
            curr.execute(INSERT_Assign, (student_id,book_id))
            conn.commit()
            curr.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Exception Handled in employee_registration POST block- {e}")
            return False