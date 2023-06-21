"""

This file contains all the functions that can / will be used within the routes

"""
from backend.dbModels import *
from backend.supportingFunctions import *

import cProfile
import pstats

import os
from datetime import datetime
from pytz import timezone


def addQuestion(data: dict):
    print(data)
    return Questions(**data)


def addDescription(data: dict, question: db.Model):
    return Description(**data, questions=question)


def addSolution(data: dict, question: db.Model):
    return Solutions(**data, questions=question)


def queryQuestion(modelType: list[str], queryType: list[str], query: list[dict] = {"id":  1},toDict = True , **kwargs):
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
                
                -filterBy: gets one or none item based on the query string passed should be in the same format expected by the function





    Return: return_description
    """

    modelDict = {"questions": Questions,
                 "description": Description,
                 "solutions": Solutions}

    queryDict = {"all": query_all,
                 "first": query_first,
                 "filterBy": query_filterBy,
                 # "filter": query_filter
                 }
    try:
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
                    # print(f"{queries = }, {query = } , {type = }")
                    res = queryDict[type](modelDict[model], **queries)
                    
                    if res:
                        if toDict:
                            res = [elements.toDict() for elements in res]
                            for i in res:
                                calculateUTC(i)
                        resultArr= resultArr + res
        # print(f"{resultArr = }")
        if len(resultArr) == 1:
            resultArr = resultArr[0]
        return resultArr
    except Exception as e:
        print(f"Query Question {e = }")
    
    return None 


# def jsonifyData(data):
#     for i in data[0]:
#         # print(i)
        
        
def deleteQuestion(modelType:db.Model,**Query):
    """Deletes the item from selected model but rn can only delete one element at a time ( can be turned to work on batches too *future work) and returns the status of the delete

    Returns:
        dict{str:bool`}: Returns the status of the delete operation
    """
    modelDict =     {"questions": Questions,
                    "description": Description,
                    "solutions": Solutions}
    delElement = query_filterBy(modelDict[modelType],**Query)
    # print(type(delElement))
    status = False
    if delElement:
        try :
            for items in delElement:
                db.session.delete(items)
            db.session.commit()
            status = True
        except Exception as e:
            print(f"deleteQuestion {e = }")
            
        return {"status":status}
    
def profileDump(func):
    def profiler(*args,**kwargs):
        # print("profilled")
        with cProfile.Profile() as profile:
            opt = func(*args,**kwargs)
        results = pstats.Stats(profile)
        results.sort_stats(pstats.SortKey.TIME)
        results.dump_stats(os.path.join("profilerDump",f"{func.__name__}.pstats") )
        return(opt)
    profiler.__name__ = func.__name__
    return profiler

def preprocessInputData(data:dict)->tuple[dict,list,list]:
    
    # print(data)

    try:
        # print(data["startDateTime"])
        # print("Enter here")
        if data.get("StartDate",False) and data.get("StartTime",False) and data.get("startDateTime",False) :
            startTimeObj = datetime.fromtimestamp(int(data["startDateTime"]/1000))
            startTimeObj = startTimeObj.astimezone(timezone('Asia/Kolkata'))
            data["StartDate"]     = startTimeObj.date()
            data["StartTime"]     = startTimeObj.time()
            # print("Enter if 1")

        
        if data.get("EndDate",False) and data.get("EndTime",False) and data.get("endDateTime",False) :
            endTimeObj = datetime.fromtimestamp(int(data["endDateTime"]/1000))
            endTimeObj = endTimeObj.astimezone(timezone('Asia/Kolkata'))
            data["EndDate"]     = endTimeObj.date()
            data["EndTime"]     = endTimeObj.time()            
            # print("Enter if 2")         

        del data["endDateTime"]
        del data["startDateTime"]

        DescriptionData = data.pop("Description",[])
        SolutionData = data.pop("Solution",[])
            
    except Exception as e:
        print(f"Preprocess Input data {e = }")
        raise(e)
    

    return data , DescriptionData, SolutionData



def updateQuestion(questionObj:db.Model,updateData:dict)->db.Model :
    status = False
    try:
        # print(f"{questionObj = }  \n\n\n {updateData = }" )
        for fieldName,fieldValue in updateData.items():
            # print(f"{fieldName = }, {fieldValue = }")
            setattr(questionObj,fieldName,fieldValue)
        # print(questionObj)
        status = True
        return questionObj , status
    except Exception as e:
        print(f"update Question {e = }")
    
    return status
        

def manageDependencies (QuestionObj,DescriptionData,SolutionData):

    #description management

    allDes = QuestionObj.Description.copy()
    for des in allDes:
        if len(des.Description) > 0:
            QuestionObj.Description.remove(des)
    del allDes
    
    for des in DescriptionData:
        QuestionObj.Description.append(Description(Description=des))


    
    allSol = QuestionObj.Solution.copy()
    for sol in allSol:
        if len(sol.Solution) > 0:
            QuestionObj.Solution.remove(sol)
    del allSol

    for sol in SolutionData:
        QuestionObj.Solution.append(Solutions(Solution=sol))




