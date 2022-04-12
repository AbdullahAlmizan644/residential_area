from website.__init__ import app_create


app=app_create()

if __name__=="__main__":
    app.run(debug=True)



