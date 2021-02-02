from flask import Flask,render_template,request,redirect,url_for
from flask import jsonify
from flask_pymongo import PyMongo
import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/hels"
mongo = PyMongo(app)


@app.route("/",methods=['GET','POST'])
def home():
    data=mongo.db.hd.find()
    return render_template("home.html",data=data)



@app.route("/add",methods=['POST'])
def add():
    name=request.form['fname']
    age=request.form['age']
    mongo.db.hd.insert({"name":name,"age":age})
    return redirect(url_for('home'))
    

    
@app.route("/adduser",methods=['GET'])
def data():
    return render_template("add.html")


@app.route("/edit/<names>",methods=['GET','POST'])
def edit(names):
    date=mongo.db.hd.find({"name":names})
    if request.method=="POST":
        name=request.form['fname']
        age=request.form['age']
        temp={"name":names},{"$set":{"name":name,"age":age}}
        mongo.db.hd.update_one(*temp)
        return redirect(url_for('home'))

    return render_template("edit.html",data=date)







@app.route("/delete/<name>",methods=['GET','POST'])
def delete(name):
    data=mongo.db.hd.delete_one({"name":name})
    return redirect(url_for('home'))




if __name__=="__main__":
    app.run(debug=True)
