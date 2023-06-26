import os

from flask import jsonify, render_template, request
from backend import app, db
from backend.functions import manageDependencies, addDescription, addQuestion,updateQuestion , addSolution, queryQuestion, deleteQuestion,profileDump,preprocessInputData



@app.route('/')
@app.route('/home')
def home():
    # print(app.config['SQLALCHEMY_DATABASE_URI'])
    # print(os.system("pwd"))
    return render_template('homepage.html', route=os.getcwd())


@app.route('/addQuestion', methods=["POST"])
def add_question():
    if request.method == "POST":

        data = request.json
        status = False
        try:
            QuestionData ,_,_= preprocessInputData(data["data"])
            # print(f"{QuestionData = }")
            dataPoint = addQuestion(data=QuestionData)
            print(dataPoint)
            db.session.add(dataPoint)
            db.session.commit()
            # print(dataPoint)
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception in addQuestion {exception = }")
        finally:

            return jsonify(status=status)

@app.route('/delQuestion', methods=["POST"])
def del_question():
    if request.method == "POST":

        data = request.json
        status = False
        # print("entered")
        try:
            # print(data)
            status = deleteQuestion(**data) #this needs model type and query based on which we are selecting the items to be deleted

        except Exception as exception:
            db.session.rollback()
            print(f"Exception {exception = }")
        finally:

            return jsonify(status=status)


@app.route('/updateQuestion', methods=["POST"])
def update_Question():
    if request.method == "POST":

        data :dict = request.json
        status = False
        try:
            # print(1)
            QuestionData,DescriptionData,SolutionData = preprocessInputData(data["data"])
            # print(2)

            queryResult = queryQuestion(
                    modelType="questions", queryType="filterBy",query={"Id":QuestionData.get("Id",None)},toDict=False)

            manageDependencies(queryResult,DescriptionData,SolutionData)

            dataPoint,_ = updateQuestion(queryResult,QuestionData)

            db.session.add(dataPoint)
            db.session.commit()
            # print(dataPoint)
            status = True
        except Exception as exception:
            db.session.rollback()
            print(f"Exception in UpdateQuestion {exception = }")
        finally:

            return jsonify(status=status)


@app.route('/queryQuestion', methods=["POST"])
def query_question():
    if request.method == "POST":

        data :dict = request.json
        status = False
        try:

            queryResult = queryQuestion(
                    modelType=data.pop("modelType"), queryType=data.pop("queryType"),query=data.get("query",{}))
            # print(f"{queryResult = }")

            queryResult = [queryResult] if type(queryResult) != list else queryResult


            status = True
        except Exception as exception:
            print(f"Exception {exception = }")
            return jsonify(status=status)
        finally:
            return jsonify(status=status, data=queryResult)

