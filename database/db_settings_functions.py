from database import db_connection
from mysql import connector
from database import db_settings_querries


def selectSettingsTable(table):
    sql_command = db_settings_querries.querryText_settingsSelect(table)
    select_result = execute_SQL_command(sql_command,None,1)
    if select_result == False:
        return False
    else:
        return select_result

def insertSettingsRecord(table, values):
    sql_command = db_settings_querries.querryText_settingsInsert(table)
    if execute_SQL_command(sql_command,values, 0):
        return True
    else:
        return False

def getNewRecordID(table):
    sql_command = db_settings_querries.querryText_settingsNewRecordID(table)
    newId = execute_SQL_command(sql_command, None, 2)
    if newId == False:
        return False
    else:
        return newId

def deleteSettingsRecord(table, record_id):
    sql_commad = db_settings_querries.querryText_settingsRecordDelete(table)
    values = (record_id,)
    if execute_SQL_command(sql_commad,values, 0):
        return True
    else:
        return False

def updateSettingsRecord(table, values):
    sql_command = db_settings_querries.querryText_settingsUpdate(table)
    if execute_SQL_command(sql_command,values, 0):
        return True
    else:
        return False

def execute_SQL_command(sql_command, values, operationType):
    mydb = db_connection.db_connect()
    if mydb == 0:
        # Place to initiate dialog with connection error
        print("errororo")
    else:
        try:
            dbCoursor = mydb.cursor()
            if operationType == 1 or operationType == 2:
                dbCoursor.execute(sql_command)
                select_result = dbCoursor.fetchall()
                dbCoursor.close()
                mydb.close()
                if operationType == 1:
                    print(select_result)
                    return select_result
                elif operationType == 2:
                    print(select_result[0][0])
                    return select_result[0][0]
            else:
                dbCoursor.execute(sql_command,values)
                mydb.commit()
                dbCoursor.close()
                mydb.close()
                return True
        except connector.Error as err:
            print(f"Connection error: {err.msg}")
            return False