from flask import jsonify, render_template,request

from backend import app
import os


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html',route = os.getcwd())


@app.route('/saveData',methods=["GET","POST"])
def saveData():
    if request.method == "POST":
        form = request.form
        data = form["data"]
        print(data)
        return jsonify(data=True)

@app.route('/classify',methods=["POST"])
def classifyApi():
    if request.method == "POST":
        data = request.args['data']
        
        return jsonify({"pred" : True,"data" : True})
