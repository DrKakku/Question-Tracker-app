import os

from flask import jsonify, render_template, request
from flask_cors import cross_origin
from backend import app, db
from backend.functions import addDescription, addQuestion,updateQuestion , addSolution, queryQuestion, deleteQuestion,profileDump,preprocessInputData



@app.route('/')
@app.route('/home')
@cross_origin(origin='*')
def home():
    return render_template('homepage.html', route=os.getcwd())


@app.route('/addQuestion', methods=["POST"])
@cross_origin(origin='*')
def add_question():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            QuestionData = preprocessInputData(data["data"])
            dataPoint = addQuestion(QuestionData)
            db.session.add(dataPoint)
            db.session.commit()
            print(dataPoint)
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception in addQuestion {exception = }")
        finally:

            return jsonify(status=status)
        
@app.route('/delQuestion', methods=["POST"])
@cross_origin(origin='*')
def del_question():
    if request.method == "POST":

        data = request.json
        status = False
        print("entered")
        try:
            print(data)
            status = deleteQuestion(**data) #this needs model type and query based on which we are selecting the items to be deleted

        except Exception as exception:
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status)
        
        
@app.route('/updateQuestion', methods=["POST"])
@cross_origin(origin='*')
def update_Question():
    if request.method == "POST":

        data :dict = request.json
        status = False
        try:
            print(1)
            QuestionData = preprocessInputData(data["data"])
            print(2)
            queryResult = queryQuestion(
                    modelType="questions", queryType="filterBy",query={"Id":QuestionData.get("Id",None)},toDict=False)
            dataPoint,_ = updateQuestion(queryResult,QuestionData)
            db.session.add(dataPoint)
            db.session.commit()
            print(dataPoint)
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception in UpdateQuestion {exception = }")
        finally:

            return jsonify(status=status)


@app.route('/queryQuestion', methods=["POST"])
# @profileDump
def query_question():
    if request.method == "POST":

        data :dict = request.json
        status = False
        try:
            
            queryResult = queryQuestion(
                    modelType=data.pop("modelType"), queryType=data.pop("queryType"),query=data.get("query",{}))
            print(f"{queryResult = }")
            status = True
        except Exception as exception:
            print(f"Exception {exception = }")
            return jsonify(status=status)
        finally:
            return jsonify(status=status, data=queryResult)


@app.route('/addDescription', methods=["POST"])
@profileDump
def add_description():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            dataPoint = addDescription(data["data"])
            db.session.add(dataPoint)
            db.session.commit()
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status, Id=dataPoint.Id)


@app.route('/addSolution', methods=["POST"])
@profileDump
def add_solution():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            dataPoint = addSolution(data["data"])
            db.session.add(dataPoint)
            db.session.commit()
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status, Id=dataPoint.Id)


@app.route('/classify', methods=["POST"])
@profileDump
def classifyApi():
    if request.method == "POST":
        # data = request.args['data']

        return jsonify({"pred": True, "data": True})
