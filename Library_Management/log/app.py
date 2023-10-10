
from flask import Flask, render_template, request, redirect

from flask_login import LoginManager, login_required, login_user, current_user, logout_user

import bcrypt
from util.db import DBConnection

from util.queries import GET_BOOK_BY_ID,GET_USER_BY_TITLE,INSERT_BOOKS,INSERT_STUDENT,get_students

from models.UserModel import UserModel
from models.BookModel import BookModel
from models.StudentModel import Studentmodel
from models.AssignModel import AssignModel

BCRYPT_SALT = b'$2b$12$91.eXPD2irVqBkzL/NLvc.'

app = Flask("library-management")
app.config["SECRET_KEY"] = "2323%$#Secret75%$&#"


login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(id):
    return UserModel.get_user_by_id(id)


@app.route("/employee/register", methods=["GET", "POST"])
def employee_registration():
    if request.method == "GET":
        return render_template("registration.html")
    else:
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        pw_hash = bcrypt.hashpw(password.encode("utf-8"), BCRYPT_SALT)
        pw_hash = pw_hash.decode("utf-8")

        try:
            UserModel.register_employee(name, email, pw_hash)
        except Exception as e:
            print(f"Exception Handled in employee_registration POST block- {e}")

        return redirect("/employee/register")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["password"]
        password = password.encode("utf-8")
        password_hash = bcrypt.hashpw(password, salt=BCRYPT_SALT).decode("utf-8")
        auth_message = UserModel.authenticate_user(email, password_hash)
        if auth_message["success"]:
            login_user(auth_message["user"])
            return redirect("/")
        else:
            return redirect("/login?login=failed")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/")
@login_required
def home():
    book=BookModel.get_books()
    student=Studentmodel.get_student()
    return render_template("home.html", current_user=current_user,books=book,student=student)


@app.route("/add/book", methods=["GET", "POST"])
@login_required
def add_book():
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        title = request.form["title"].title()
        author = request.form["author"].title()
        total_copies = int(request.form.get("total_copies", 0))
        created = BookModel.create_book(title, author, total_copies, current_user.id)
        if created:
            return redirect("/")
        else:
            return render_template("add_book.html", error=True)

@app.route("/add/student", methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "GET":
        return render_template("student.html")
    else:
        name = request.form["name"]
        email = request.form["email"]
        reg_no= request.form["reg_no"]
        created = Studentmodel.create_student(name,email,reg_no,current_user.id)
        if created:
            return redirect("/stu")
        else:
            return render_template("student.html", error=True)

@app.route("/stu")
def student_home():
    student=Studentmodel.get_student()
    return render_template("home1.html",current_user=current_user,student=student)

@app.route("/book/<int:id>/edit")
@login_required
def edit_book(id):
    books=BookModel.GET_BOOK_BY_ID(id)
    return render_template("edit_book.html",book=books)


@app.route("/assign/book",methods=["GET","POST"])
def assign_book():
    if request.method=="GET":
        student = Studentmodel.get_student()
        book = BookModel.get_books()
        return render_template("assign.html", current_user=current_user, books=book, student=student)
    else:
        student_id = request.form["student_id"]
        book_id = request.form["book_id"]
        AssignModel.create_assign(student_id, book_id)
        return redirect("/assign/book")




if __name__ == "__main__":
    app.run(debug=True)
