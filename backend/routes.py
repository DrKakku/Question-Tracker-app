from flask import jsonify, render_template,request

from backend import app,db
import os
from backend.functions import addQuestion


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html',route = os.getcwd())


@app.route('/saveData',methods=["GET","POST"])
def saveData():
    if request.method == "POST":
        form = request
        data = form.json
        x = addQuestion(data["data"])
        db.session.add(x)
        db.session.commit()

        return jsonify(data=True,hello="this is my hellow",bro="dont joke around bro",local="this is indeed local stuff",need="to add more random stuff")

@app.route('/classify',methods=["POST"])
def classifyApi():
    if request.method == "POST":
        # data = request.args['data']
        
        return jsonify({"pred" : True,"data" : True})
