# from flask import Flask,render_template,request,redirect,url_for
# from flask import jsonify
# from flask_mongoengine import MongoEngine
# import json


# app = Flask(__name__)
# app.config["MONGODB_SETTINGS"]={
#     "db":"hels",
#     "host":"localhost",
#     "port":27017
# }


# db=MongoEngine()
# db.init_app(app)


# class Hd(db.Document):
#     name=db.StringField()
#     age=db.StringField()



# @app.route("/",methods=['GET','POST'])
# def home():
#     data=Hd.objects.all()
#     return render_template("home.html",data=data)


# @app.route("/adddata")
# def adddata():
#     return render_template("add.html")
    

# @app.route("/add",methods=['POST'])
# def add():
#     name=request.form['fname']
#     age=request.form['age']
#     datas=Hd(name=name,age=age)
#     datas.save()
#     return redirect(url_for('home'))



# if __name__=="__main__":
#     app.run(debug=True)
