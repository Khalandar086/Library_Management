



GET_USER_BY_ID = "SELECT * from EMPLOYEE WHERE id=%s;"

GET_USER_BY_EMAIL = "SELECT * from EMPLOYEE WHERE email=%s;"

GET_USER_BY_TITLE="SELECT * from Books Where title=%s;"

INSERT_EMPLOYEE = "INSERT INTO EMPLOYEE(name, email, password) VALUES(%s, %s, %s);"

INSERT_BOOKS = "INSERT INTO BOOKS(title,author,total_copies,available_copies,created_by) VALUES (%s,%s,%s,%s,%s);"

GET_BOOKS="select b.id,title,author,total_copies,available_copies,bought_on,e.name from books as b inner join employee e on e.id=b.created_by;"
GET_BOOK_BY_ID="select title,author,total_copies from books where id=%s;"
update_book="update Books set title=%s,author=%s,total_copies=%s where id=%s;"

INSERT_STUDENT = "INSERT INTO STUDENT(name,email,reg_no,created_by) VALUES (%s,%s,%s,%s);"

get_students="select id,name,email,reg_no from  student;"

INSERT_Assign = "insert into borrowedbook(student_id,book_id) values (%s,%s);"

