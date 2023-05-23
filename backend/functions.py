"""

This file contains all the functions that can / will be used within the routes

"""
from backend.dbModels import *
from backend.supportingFunctions import *


def addQuestion(data: dict):
    return Questions(**data)


def addDescription(data: dict, question: db.Model):
    return Description(**data, questions=question)


def addSolution(data: dict, question: db.Model):
    return Solutions(**data, questions=question)


def queryQuestion(modelType: list[str], queryType: list[str], query: list[dict] = {"id":  1}, **kwargs):
    """
    Dynamic Querying for all the class models that we have in the database
    it will search through any of the models using the keywords 

    Keyword arguments:

    first argument is the modelType - 

                    - "questions": Questions,

                    - "description": Description, 

                    - "solutions": Solutions


    Second argument is query type =

                - all: THis queries all the available datapoints for the class 

                - first: This return the first item in the class 





    Return: return_description
    """

    modelDict = {"questions": Questions,
                 "description": Description,
                 "solutions": Solutions}

    queryDict = {"all": query_all,
                 "first": query_first,
                 # "filterBy": query_filterBy,
                 # "filter": query_filter
                 }

    # converting to lists if not already a list
    if not isinstance(query, list):
        query = [query]
    if not isinstance(modelType, list):
        modelType = [modelType]
    if not isinstance(queryType, list):
        queryType = [queryType]

    resultArr = []

    for queries in query:
        for model in modelType:
            for type in queryType:
                res = queryDict[type](modelDict[model], **queries)
                if res:
                    res = [elements.toDict() for elements in res]
                    for i in res:
                        calculateUTC(i)
                    resultArr.append(res)
    if len(resultArr) == 1:
        resultArr = resultArr[0]
    return resultArr


def jsonifyData(data):
    for i in data[0]:
        print(i)
        
        
def deleteQuestion(modelType:db.Model,**Query):
    """Deletes the item from selected model but rn can only delete one element at a time ( can be turned to work on batches too *future work) and returns the status of the delete

    Returns:
        dict{str:bool`}: Returns the status of the delete operation
    """
    modelDict =     {"questions": Questions,
                    "description": Description,
                    "solutions": Solutions}
    delElement = query_filterBy(modelDict[modelType],**Query)
    status = False
    if delElement:
        try :
            db.session.delete(delElement)
            db.session.commit()
            status = True
        except Exception as e:
            print(e)
            
        return {"status":status}
