import os

from flask import jsonify, render_template, request

from backend import app, db
from backend.functions import addDescription, addQuestion, addSolution,queryQuestion,jsonifyData


@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html',route = os.getcwd())


@app.route('/addQuestion',methods=["POST"])
def add_question():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            dataPoint = addQuestion(data["data"])
            db.session.add(dataPoint)
            db.session.commit()
            status = True
        except Exception as exception :
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status,Id=dataPoint.Id)
        

@app.route('/queryQuestion',methods=["POST"])
def query_question():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            queryResult = queryQuestion(modelType = data["modelType"],queryType = data["queryType"])
            # print(queryResult)
            status = True
        except Exception as exception :
            print(f"Exception {exception = }")
            return jsonify(status=status)
        finally:

            return jsonify(status=status,data=queryResult)
        
    

@app.route('/addDescription',methods=["POST"])
def add_description():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            dataPoint = addDescription(data["data"])
            db.session.add(dataPoint)
            db.session.commit()
            status = True
        except Exception as exception :
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status,Id=dataPoint.Id)
        


@app.route('/addSolution',methods=["POST"])
def add_solution():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            dataPoint = addSolution(data["data"])
            db.session.add(dataPoint)
            db.session.commit()
            status = True
        except Exception as exception :
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status,Id=dataPoint.Id)
        



@app.route('/classify',methods=["POST"])
def classifyApi():
    if request.method == "POST":
        # data = request.args['data']
        
        return jsonify({"pred" : True,"data" : True})
