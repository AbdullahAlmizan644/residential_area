from multiprocessing import connection
from os import curdir
from unicodedata import name
from flask import Blueprint,render_template,redirect,flash,request, session
from .__init__ import db,app_create
from datetime import datetime
import os
from werkzeug.utils import secure_filename



auth=Blueprint('auth',__name__)


app=app_create()

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form.get("name")
        password=request.form.get("password")

        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where username=%s and password=%s",(name,password))
        user=cur.fetchone()

        if user:
            session['username']=name
            flash("Login successfully!", category="success")
            return redirect("/profile")
        else:
            flash("Wrong username or password!", category="error")

    return render_template("auth/login.html")



@auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        name=request.form.get('name')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')

        # cur=db.connection.cursor()
        # cur.execute("SELECT * FROM users where username=%s",(name))
        # data=cur.fetchone()

        # if data=='':
        #     flash('username already exist!', category='error')
        if len(name)<5:
            flash('name must be greater than 5 words', category='error')
        
        elif len(email)<5:
            flash('email must be greater than 5 words', category='error')

        elif len(password1)<8:
            flash('password must be greater than 7 numbers', category='error')

        elif password1!=password2:
            flash("password doesn't match", category='error')

        else:
            cur = db.connection.cursor()
            cur.execute('''INSERT INTO users(username,email,password,date) VALUES(%s,%s,%s,%s)''',(name,email,password1,datetime.now()))
            db.connection.commit()
            cur.close()
            flash('account created successfully',category="success")
            return redirect("/login")
    return render_template("auth/signup.html")




@auth.route("/profile", methods=["GET","POST"])
def profile():
    if "username" in session:
        if request.method=="POST":
            image = request.files['image_file']
            if image.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:

                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
                cur=db.connection.cursor()
                cur.execute("UPDATE users SET image=%s where username=%s",(image.filename,session["username"]))
                db.connection.commit()
                return redirect(request.url)



        cur=db.connection.cursor()
        cur.execute("SELECT * FROM users where username=%s",(session["username"],))
        users=cur.fetchone()


        cur=db.connection.cursor()
        cur.execute("SELECT COUNT(post_id) from rent_house_post where writer=%s",(session["username"],))
        total=cur.fetchone()
        cur.close()
        return render_template("auth/profile.html",users=users,total=total)

    else:
        return redirect("/login")


@auth.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/")