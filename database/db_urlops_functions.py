from database import db_connection
from mysql import connector
from database import db_urlops_querries

def checkActualAgreement(workerID):
    print("checkActualAgreement")
    sql_command = db_urlops_querries.urlopQuerryText_selectAgreement()
    values = (workerID,)
    receivedValue = executeCommand(sql_command,values,1)
    print('Agreement ID',receivedValue)
    if parseToInt(receivedValue,None):
        return True
    else:
        return False


def checkWorkHistory(urlopType,workerID):
    print('checkWorkHistory')
    sql_command = db_urlops_querries.urlopQuerryText_workHistory(urlopType)
    values = (workerID,)
    count = executeCommand(sql_command,values,1)
    if parseToInt(count,None):
        return count[0][0]
    else:
        return False

def checkUsedUrlop(urlopType, workerID):
    print('checkUsedUrlop')
    sql_command = db_urlops_querries.urlopQuerryText_usedDaysCount()
    values = (workerID, urlopType)
    count = executeCommand(sql_command,values,1)
    print("COUNT",count)
    if parseToInt(count,None):
        return count[0][0]
    else:
        return False

def checkUsedPaidUrlop(workerID):
    print('checkUsedPaidUrlop')
    sql_command = db_urlops_querries.urlopQuerryText_usedDaysPaidUrlop()
    values = (workerID,)
    count = executeCommand(sql_command,values,1)
    print('Dni wykorzystane: ',count)
    if parseToInt(count,None):
        return count[0][0]
    else:
        return False

def getWorkerUrlopDays(workerID):
    mydb = db_connection.db_connect()
    if mydb == 0:
        # Place to initiate dialog with connection error
        print("errororo")
    values = (workerID,)
    print('nr pracwonika',values)
    dbCoursor = mydb.cursor()
    sql_command = """call UrlopLimits(%s);"""
    dbCoursor.execute(sql_command,values)
    print("Procedure executed")
    select_result = dbCoursor.fetchall()
    print("LIMIT URLOPU: ", select_result[0][0])
    return select_result[0][0]

def checkWorkerChilds(workerID):
    print('checkWorkerChilds')
    #GET WORKER CHILDS COUNT
    sql_command = db_urlops_querries.querryText_workerChildsCount()
    values = (workerID,)
    count = executeCommand(sql_command,values,1)
    # GET URLOPS DAYS LIMIT
    sql_command = db_urlops_querries.querryText_urlopAnnualDays()
    values = (2,)
    limit = executeCommand(sql_command, values, 1)
    if parseToInt(count,limit):
        days = count[0][0] * limit[0][0]
        return days
    else:
        return False

def checkRequestedUrlopDateAmmount():
    print('checkRequestedUrlopDateAmmount')
    sql_command = db_urlops_querries.querryText_urlopAnnualDays()
    values = (3,)
    limit = executeCommand(sql_command, values, 1)
    if parseToInt(limit, None):
        return limit[0][0]
    else:
        return False

def getDisabilityWorkerList(workerID):
    print('getAllIndexFromDisabilityCard')
    sql_command = db_urlops_querries.querryText_getDisabilityIndex()
    values = (workerID,)
    indexList = executeCommand(sql_command,values,1)
    if indexList is None:
        return False
    else:
        return indexList

def getDisabilityDays(workerID, lastIndex, newIndex):
    print('GetDisabilityDays ')
    mydb = db_connection.db_connect()
    if mydb == 0:
        # Place to initiate dialog with connection error
        print("errororo")
    dbCoursor = mydb.cursor()
    sql_command = """call calculateDisabilityUrlop(%s,%s,%s);"""
    values = (workerID,lastIndex,newIndex)
    dbCoursor.execute(sql_command, values)
    print("Procedure executed - niepelnosprawnosc")
    select_result = dbCoursor.fetchall()
    print('select result: ',select_result)
    print("LIMIT DODATKOWEGO URLOPU : ", select_result[0])
    return select_result[0][0]


def parseToInt(arg1,arg2):
    print('Parsing values: ',arg1,arg2)
    if arg2 == None:
        try:
            check = arg1[0][0]
            if int(check):
                return True
        except:
            return False
    else:
        try:
            if int(arg1[0][0]) and int(arg2[0][0]):
                return True
        except:
            print('Brak danych w tabeli')
            return False

def executeCommand(sql_command, values,returnMode):
    mydb = db_connection.db_connect()
    if mydb == 0:
        # Place to initiate dialog with connection error
        print("errororo")
    else:
        try:
            dbCoursor = mydb.cursor()
            dbCoursor.execute(sql_command, values)
            if returnMode == 1:
                querry_result = dbCoursor.fetchall()
                mydb.commit()
                dbCoursor.close()
                mydb.close()
                return querry_result
            else:
                mydb.commit()
                dbCoursor.close()
                mydb.close()
                return True
        except connector.Error as err:
            print(f"Connection error: {err.msg}")
            return False