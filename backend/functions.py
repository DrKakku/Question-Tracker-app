"""

This file contains all the functions that can / will be used withen the routes

"""
from backend.dbModels import *

def addQuestion(data:dict):
    x = Questions(**data)
    return x

