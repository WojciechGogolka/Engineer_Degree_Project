def downloadComboBox(viewType):
    if viewType == 'agreements':
        sql_command = """SELECT
                            agreement_name
                        FROM
                            agreement_types
                        ORDER BY agreement_id;"""

    elif viewType == 'city':
        sql_command = """SELECT
                            city_name
                        FROM
                            cities
                        ORDER BY city_id;"""

    elif viewType == 'urlop':
        sql_command = """SELECT
                                urlop_name
                            FROM
                                urlop_types
                            ORDER BY urlop_id;"""

    elif viewType == 'education':
        sql_command = """SELECT 
                                education_name
                            FROM
                                education_degrees
                            ORDER BY education_id"""

    elif viewType == 'invalid':
        sql_command = """SELECT 
                                disability_name
                            FROM
                                disability_degrees
                            ORDER BY disability_id"""
    return sql_command

def getComboID(comboType):
    if comboType == 'agreements':
        sql_command = """SELECT
                            agreement_id
                        FROM
                            agreement_types
                        WHERE 
                            agreement_name = %s"""
    elif comboType == 'invalid':
        sql_command = """SELECT
                            disability_id
                         FROM 
                            disability_degrees
                        WHERE
                            disability_name = %s"""
    elif comboType == 'city':
        sql_command = """SELECT
                            city_id
                         FROM 
                            cities
                        WHERE
                            city_name = %s"""
    elif comboType == 'education':
        sql_command = """SELECT
                            education_id
                         FROM 
                            education_degrees
                        WHERE
                            education_name = %s"""
    elif comboType == 'urlop':
        sql_command = """SELECT
                            urlop_id
                         FROM 
                            urlop_types
                        WHERE
                            urlop_name = %s"""
    return sql_command