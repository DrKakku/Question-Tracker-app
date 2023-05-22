"""

This file contains all the functions that can / will be used within the routes

"""
from backend.dbModels import *
import datetime


def addQuestion(data: dict):
    return Questions(**data)


def addDescription(data: dict, question: db.Model):
    return Description(**data, questions=question)


def addSolution(data: dict, question: db.Model):
    return Solutions(**data, questions=question)


def queryQuestion(modelType: list[str], queryType: list[str], query: list[dict] = {"id" :  1}, **kwargs):
    """
    Dynamic Querying for all the class models that we have in the database
    it will search through any of the models using the keywords 

    Positional argumnets:
    first argument is the modelType = 
                    - "questions": Questions,
                    - "description": Description, 
                    - "solutions": Solutions
    
    Second argument is query type =
                - all: THis queries all the availabe datapoints for the class 
                - first: This return the first item in the class 
                


    Keyword arguments:
    argument -- description
    Return: return_description
    """

    modelDict = {"questions": Questions,
                "description": Description, 
                "solutions": Solutions}
    
    queryDict = {"all": query_all,
                "first": query_first,
                # "filterBy": query_filterBy, 
                # "filter": query_flter
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
    return resultArr


# if query possible then return result else just return nothing
def query_all(modelType: db.Model, **kwargs):
    try:
        result = modelType.query.all()
        return result

    except Exception as e:
        pass


def query_first(modelType: db.Model, **kwargs):
    try:
        result = modelType.query.first()
        return [result]

    except Exception as e:
        pass


def query_filterBy(modelType: db.Model, **query):
    try:
        result = modelType.query.filter_by(**query)
        return result

    except Exception as e:
        pass

def query_flter(modelType: db.Model, **kwargs):
    try:
        result = modelType.query.all()
        pass

    except Exception as e:
        pass

def calculateUTC(i):
    try:
        sDate = i["StartDate"]
        sTime = i["StartTime"]
        eDate = i["EndDate"]
        eTime = i["EndTime"]
        if sDate and sTime:
            utctime = datetime.datetime.combine(sDate,sTime)
            i["StartUTC"] = datetime.datetime.timestamp(utctime)
        
        if eDate and eTime:
            utctime = datetime.datetime.combine(eDate,eTime)
            i["EndUTC"] = datetime.datetime.timestamp(utctime)
        else:
            i["EndUTC"] = None
    except:
        pass
