def querryText_settingsSelect(table):
    if table == 'cities':
        sql_command = """SELECT * FROM cities order by city_id"""
    elif table == "education":
        sql_command = """SELECT * FROM education_degrees ORDER BY education_id"""
    elif table == "agreements":
        sql_command = """SELECT * FROM agreement_types ORDER BY agreement_id"""
    elif table == "invalids":
        sql_command = """SELECT * FROM disability_degrees ORDER BY disability_id"""
    elif table == "urlops":
        sql_command = """SELECT * FROM urlop_types ORDER BY urlop_id"""
    return sql_command

def querryText_settingsInsert(table):
    if table == 'cities':
        sql_command = """INSERT INTO 
                            cities(city_name) 
                        VALUES(%s);"""
    elif table == 'education':
        sql_command = """INSERT INTO 
                            education_degrees(education_name,education_yearsWorkHist) 
                        VALUES(%s,%s);"""
    elif table == 'agreements':
        sql_command = """INSERT INTO 
                            agreement_types(agreement_name, agreement_countToUrlop) 
                        VALUES(%s,%s);"""
    elif table == 'invalids':
        sql_command = """INSERT INTO 
                            disability_degrees(disability_name,disability_addUrlop) 
                        VALUES(%s,%s);"""
    elif table == 'urlops':
        sql_command = """INSERT INTO 
                            urlop_types(urlop_name,urlop_yearlyLimit) 
                        VALUES(%s,%s);"""
    return sql_command

def querryText_settingsNewRecordID(table):
    if table == 'cities':
        sql_command = """SELECT city_id 
                            FROM cities 
                            ORDER BY city_id 
                            DESC LIMIT 1;"""

    elif table == 'education':
        sql_command = """SELECT education_id 
                            FROM education_degrees 
                            ORDER BY education_id 
                            DESC LIMIT 1;"""
    elif table == 'agreements':
        sql_command = """SELECT agreement_id 
                            FROM agreement_types 
                            ORDER BY agreement_id 
                            DESC LIMIT 1;"""
    elif table == 'invalids':
        sql_command = """SELECT disability_id 
                            FROM disability_degrees 
                            ORDER BY disability_id 
                            DESC LIMIT 1;"""
    elif table == 'urlops':
        sql_command = """SELECT urlop_id 
                            FROM urlop_types 
                            ORDER BY urlop_id 
                            DESC LIMIT 1;"""
    return sql_command

def querryText_settingsRecordDelete(table):
    if table == 'cities':
        sql_command = """DELETE 
                            FROM cities 
                            WHERE city_id = %s;"""
    elif table == 'education':
        sql_command = """DELETE 
                            FROM education_degrees 
                            WHERE education_id = %s;"""
    elif table == 'agreements':
        sql_command = """DELETE 
                            FROM agreement_types 
                            WHERE agreement_id = %s;"""
    elif table == 'invalids':
        sql_command = """DELETE 
                            FROM disability_degrees 
                            WHERE disability_id = %s;"""
    elif table == 'urlops':
        sql_command = """DELETE 
                            FROM urlop_types 
                            WHERE urlop_id = %s;"""
    return sql_command

def querryText_settingsUpdate(table):
    if table == 'cities':
        sql_command = """UPDATE cities 
                            SET  
                                city_name = %s 
                            WHERE city_id = %s;"""
    elif table == 'education':
        sql_command = """UPDATE education_degrees 
                            SET education_name = %s, 
                                education_yearsWorkHist = %s 
                            WHERE education_id = %s;"""
    elif table == 'agreements':
        sql_command = """UPDATE agreement_types 
                            SET agreement_name = %s, 
                                agreement_countToUrlop = %s 
                            WHERE agreement_id = %s;"""
    elif table == 'invalids':
        sql_command = """UPDATE disability_degrees 
                            SET disability_name = %s, 
                            disability_addUrlop = %s 
                        WHERE disability_id = %s;"""
    elif table == 'urlops':
        sql_command = """UPDATE urlop_types 
                            SET urlop_name = %s, 
                            urlop_yearlyLimit = %s 
                        WHERE urlop_id = %s;"""
    return sql_command
