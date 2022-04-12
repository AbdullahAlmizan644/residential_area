from flask import Blueprint, redirect,render_template,request, session
from .settings import info
from .__init__ import db

admin = Blueprint('admin',__name__)


@admin.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method=="POST":
        email=request.form.get('email')
        password=request.form.get('password')

        if email==info['admin_email'] and password==info['admin_password']:
            session['admin']=email
            return redirect("/dashboard")

    return render_template("admin/signin.html")



@admin.route("/dashboard")
def dashboard():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        cur.close()

        cur=db.connection.cursor()
        cur.execute("SELECT COUNT(sno) FROM users")
        total_users=cur.fetchone()
        cur.close()


        cur=db.connection.cursor()
        cur.execute("SELECT * FROM rent_house_post")
        rent_posts=cur.fetchall()
        cur.close()


        cur=db.connection.cursor()
        cur.execute("SELECT COUNT(post_id) from rent_house_post")
        total_rent=cur.fetchone()
        cur.close()



        return render_template('admin/index.html',users=users,rent_posts=rent_posts,total_users=total_users,total_rent=total_rent)
    else:
        return redirect("/admin_login")


@admin.route("/user")
def user():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users")
        users=cur.fetchall()
        cur.close()

        cur=db.connection.cursor()
        cur.execute("SELECT COUNT(sno) FROM users")
        total_users=cur.fetchone()
        cur.close()
        return render_template("admin/user.html",users=users,total_users=total_users)
    else:
        return redirect("/admin_login")



@admin.route("/rent_post")
def rent_post():
    if "admin" in session:
        cur=db.connection.cursor()
        cur.execute("SELECT * FROM rent_house_post")
        posts=cur.fetchall()
        cur.close()


        cur=db.connection.cursor()
        cur.execute("SELECT COUNT(post_id) from rent_house_post")
        total=cur.fetchone()
        cur.close()
        return render_template("admin/rent_post.html",posts=posts,total=total)
    else:
        return redirect("/admin_login")