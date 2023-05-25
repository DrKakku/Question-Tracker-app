
# if query possible then return result else just return nothing
from backend.dbModels import *
import datetime


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
        result = modelType.query.filter_by(**query).one_or_none()
        print(result)
        return result

    except Exception as e:
        pass


def query_filter(modelType: db.Model, **kwargs):
    """this is a supporting function which should be able to perform filter search on SqlAlchemy model class using a query string
        More work is needed for this     

    Args:
        modelType (): this will be the SqlAlchemy model upon which the search will be performed
    """
    try:
        result = modelType.query.all()
        pass

    except Exception as e:
        pass


def calculateUTC(i):
    try:

        sDate = datetime.date.fromisoformat(i["StartDate"])
        sTime = datetime.time.fromisoformat(i["StartTime"])
        eDate = None if i["EndDate"] is None else datetime.date.fromisoformat(
            i["EndDate"])
        eTime = None if i["EndTime"] is None else datetime.time.fromisoformat(
            i["EndTime"])
        if sDate and sTime:
            utctime = datetime.datetime.combine(sDate, sTime)
            i["StartUTC"] = datetime.datetime.timestamp(utctime)

        else:
            i["StartUTC"] = None

        if eDate and eTime:
            utctime = datetime.datetime.combine(eDate, eTime)
            i["EndUTC"] = datetime.datetime.timestamp(utctime)
        else:
            i["EndUTC"] = None
    except Exception as e:
        print(f"Exception in UTC {e = }")
        pass
