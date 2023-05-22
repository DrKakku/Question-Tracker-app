import sqlite3
from sqlite3 import Error

def connectDb(Path:str) -> bool:
    
    """This function creates a database if it does not exist already and connects to it. if successfull it returns true else false
    
    Keyword arguments:
    path -- The path to the database object
    Return: bool representing the success of the operation
    """

    conn = None
    try:
        conn = sqlite3.connect(Path)
        print(sqlite3.version)

    except Error as e:
        print(e)
    
    

    return conn


