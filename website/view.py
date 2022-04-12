
from flask import Blueprint,render_template,redirect,request,session,flash
from .__init__ import db,app_create
from datetime import datetime
import os
from werkzeug.utils import secure_filename

view=Blueprint('view', __name__)

app=app_create()

@view.route("/")
def index():
    cur=db.connection.cursor()
    cur.execute("select * from rent_house_post")
    posts=cur.fetchall()
    return render_template("view/index.html",posts=posts)


@view.route("/about")
def about():
    return render_template("view/about.html")




@view.route("/contact")
def contact():
    return render_template("view/contact.html")



@view.route("/pricing")
def pricing():
    return render_template("view/pricing.html")



@view.route("/rent_house")
def rent_house():

    cur=db.connection.cursor()
    cur.execute("select * from rent_house_post")
    posts=cur.fetchall()
    cur.close()
    return render_template('view/rent_house.html',posts=posts)


@view.route("/rent_details/<int:id>")
def rent_details(id):
    cur=db.connection.cursor()
    cur.execute("select * from rent_house_post where post_id=%s",(id,))
    single_post=cur.fetchone()
    cur.close()
    return render_template('view/rent_details.html',single_post=single_post)  



@view.route("/rent_post_edit", methods=["GET","POST"])
def rent_post_edit():
    if "username" in session:
        if request.method=="POST":
            # image=request.form.get('img')
            heading=request.form.get('heading')
            details=request.form.get('details')
            image = request.files['img']
            if image.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                image.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(image.filename)))
            cur=db.connection.cursor()
            cur.execute("INSERT INTO rent_house_post(name,writer,content,image,date) VALUES (%s,%s,%s,%s,%s)",(heading,session["username"],details,image.filename,datetime.now()))
            db.connection.commit()
            return redirect("/user_rent_post ")

        return render_template("view/rent_post_edit.html")

    else:
        return redirect("/login")


@view.route("/user_rent_post")
def user_rent_post():
    if "username" in session:
        cur=db.connection.cursor()
        cur.execute("select * from rent_house_post where writer=%s",(session["username"],))
        posts=cur.fetchall()
        return render_template("view/user_rent_post.html",posts=posts)

    else:
        return redirect("/login")




@view.route("/delete_rent_post/<int:id>")
def delete_rent_post(id):
    if "username" in session:
        cur=db.connection.cursor()
        cur.execute("delete from rent_house_post where post_id=%s",(id,))
        db.connection.commit()
        return redirect("/user_rent_post")


    else:
        return redirect("/login")



# @view.route("/tution")
# def tution_post():
#     return render_template("view/tution_post.html")