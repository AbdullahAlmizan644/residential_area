from flask import Flask 
from flask_mysqldb import MySQL

db=MySQL()

def app_create():
    UPLOAD_FOLDER = '/home/ares/monirul-project/website/static/image'
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}



    app=Flask(__name__)
    app.config['SECRET_KEY']='monirul'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    app.config["MYSQL_HOST"]='127.0.0.1'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']=''
    app.config['MYSQL_DB']='residential_area'
    db.init_app(app)

    from .view import view
    from .auth import auth
    from .admin import admin

    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')
    
    return app
