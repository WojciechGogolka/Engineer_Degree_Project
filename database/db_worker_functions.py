from database import db_connection
from mysql import connector
from database import db_worker_querries
from database import db_comboBox_querries

mydb = None
global dbCoursor
global sql_command
global select_result

def load_workers_list():
    sql_command = db_worker_querries.querryText_workersList()
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command, None, 1)
    if select_result is not False:
        return select_result

def addNewWorker(workerData):
    convertList = list(workerData)
    listSize = len(convertList)
    for item in range(listSize):
        if convertList[item] == '':
            convertList[item] = None
    values = tuple(convertList)
    sql_command = db_worker_querries.querryText_addWorker()
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command, values,0):
        print("New worker added to database")
        return True
    else:
        return False

def getNewWorkerID():
    sql_command = db_worker_querries.querryText_getNewWorkerID()
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command, None, 1)
    return select_result[0][0]

def getNewFormRecordID(table):
    sql_command = db_worker_querries.querryTextForms_newRecordID(table)
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command, None, 1)
    return select_result[0][0]

def deleteWorker(record_id):
    sql_command = db_worker_querries.querryText_workerDelete()
    values = (record_id,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command,values,0) is False:
        return False
    else:
        return True
        print("Worker deleted")

def updateWorkerPersonalData(record_id, workerData):
    sql_command = db_worker_querries.querryText_workerUpdate()
    tmp_values = list(workerData)
    tmp_values.append(record_id)
    values = tuple(tmp_values)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command, values,0):
        return True
    else:
        return False
    print("Worker data updated")

def downloadWorkerFormsData(viewForm, record_id):
    sql_command = db_worker_querries.querryTextForms_select(viewForm)
    values = (record_id,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command,values,1)
    return select_result

def downloadComboBox(viewType):
    sql_command = db_comboBox_querries.downloadComboBox(viewType)
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command,None,1)
    return select_result

def getComboID(comboType, comboText):
    sql_command = db_comboBox_querries.getComboID(comboType)
    values = (comboText,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    select_result = execute_SQL_Command(sql_command,values,1)
    try:
        if int(select_result[0][0]):
            return select_result[0][0]
    except:
        print('Brak danych w tabeli')
        return False

def insertWorkerFormRecord(tableType, addList):
    convertList = list(addList)
    listSize = len(convertList)
    for item in range(listSize):
        #print(convertList[item])
        if convertList[item] == '':
            convertList[item] = None
    addList = tuple(convertList)
    values = tuple(addList)
    #SQL DATA -----------------------------------------------------------------------
    sql_command = db_worker_querries.querryTextForms_insert(tableType)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command, values, 0):
        return True
    else:
        return False

def deleteWorkerFormRecord(tableType,record_id):
    sql_command = db_worker_querries.querryTextForms_delete(tableType)
    values = (record_id,)
    # elif tableType == 'urlop':
        # sql_command = db_worker_querries.deleteWorkerFormQuerry('urlop')
        # values = (record_id,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command, values, 0):
        return True
    else:
        return False

def updateWorkerFormRecord(tableType, record_id, editList):
    convertList = list(editList)
    listSize = len(convertList)
    for item in range(listSize):
        if convertList[item] == '':
            convertList[item] = None
    convertList.pop(0)
    convertList.append(record_id)
    editList = tuple(convertList)
    #print(editList)
    # SQL DATA -----------------------------------------------------------------------
    sql_command = db_worker_querries.querryTextForms_update(tableType)
    values = tuple(editList)
    # elif tableType == 'urlop':
        # sql_command = db_worker_querries.editWorkerFormQuerry('urlop')
        # values = tuple(addList)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command,values,0):
        return True
    else:
        return False

def updateChildParent(editList):
    # SQL DATA -----------------------------------------------------------------------
    sql_command = db_worker_querries.querryTextForms_update('childParent')
    values = tuple(editList)
    print(values)
    # EXECUTE COMMAND ---------------------------------------------------------------
    if execute_SQL_Command(sql_command, values, 0):
        return True
    else:
        return False

def getParentID(newID):
    # SQL DATA -----------------------------------------------------------------------
    sql_command = db_worker_querries.querryText_checkWorkerID()
    values = (newID,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    receivedValue = execute_SQL_Command(sql_command, values, 1)
    print(receivedValue)
    try:
        parentID = receivedValue[0][0]
        #print('ParentID',parentID)
        if int(parentID):
            return parentID
        else:
            return False
    except:
        return False

def getLastAgreement(workerID):
    # SQL DATA -----------------------------------------------------------------------
    sql_command = db_worker_querries.querryText_getLastAgreement()
    values = (workerID,)
    # EXECUTE COMMAND ---------------------------------------------------------------
    receivedValue = execute_SQL_Command(sql_command, values, 1)
    print(receivedValue)
    return receivedValue[0][0]



def execute_SQL_Command(sql_command, values, returnMode):
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