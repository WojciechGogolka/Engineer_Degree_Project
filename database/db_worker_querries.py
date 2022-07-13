def querryText_workersList():
    sql_querry = """SELECT
                        w.worker_id,
                        w.worker_name, 
                        w.worker_lastname, 
                        w.worker_birthDate,
                        IF( w.worker_isForeigner=0, "Nie","Tak") as "IsForeigner",
                        w.worker_PESEL, 
                        w.worker_address, 
                        w.worker_zipCode, 
                        c.city_name,
                        IF( isnull(w.worker_phoneNumber),'',w.worker_phoneNumber),
                        e.education_name 
                        FROM
                        worker_personal_data w LEFT JOIN cities c 
                        ON w.worker_city = c.city_id LEFT JOIN education_degrees e
                        ON w.worker_education = e.education_id
                        ORDER BY w.worker_id;"""
    return sql_querry

def querryText_addWorker():
    sql_querry = """INSERT INTO
                        worker_personal_data(
                            worker_name,
                            worker_lastname,
                            worker_birthDate,
                            worker_isForeigner,
                            worker_PESEL, 
                            worker_address,
                            worker_zipCode,
                            worker_city,
                            worker_phoneNumber,
                            worker_education)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    return sql_querry

def querryText_getNewWorkerID():
    sql_querry = """SELECT 
                        worker_id
                    FROM
                        worker_personal_data
                    ORDER BY 
                        worker_id
                    DESC LIMIT 1;"""
    return sql_querry

def querryText_checkWorkerID():
    sql_querry = """SELECT 
                        worker_id
                    FROM
                        worker_personal_data
                    WHERE 
                        worker_id = %s;"""
    return sql_querry

def querryText_workerUpdate():
    sql_querry = """UPDATE worker_personal_data
                        SET
                            worker_name = %s,
                            worker_lastname = %s,
                            worker_birthDate = %s,
                            worker_isForeigner = %s,
                            worker_PESEL = %s,
                            worker_address = %s,
                            worker_zipCode = %s,
                            worker_city = %s,
                            worker_phoneNumber = %s,
                            worker_education = %s
                        WHERE worker_id = %s;"""
    return sql_querry

def querryText_workerDelete():
    sql_querry = """DELETE 
                        FROM worker_personal_data 
                        WHERE worker_id = %s;"""
    return sql_querry


def querryTextForms_select(tableType):
    if tableType == 'agreements':
        sql_querry = """SELECT
                            a.workerAgreements_id,
                            at.agreement_name, 
                            a.workerAgreements_dateStart, 
                            a.workerAgreements_dateEnd,
                            a.workerAgreements_time
                            FROM
                            worker_agreements a LEFT JOIN agreement_types at 
                            ON a.workerAgreements_agreementType = at.agreement_id 
                            WHERE
                            a.workerAgreements_workerID = %s;"""
    elif tableType == 'child':
        sql_querry = """SELECT
                            child_id,
                            child_name,
                            child_lastname,
                            child_birthDate
                            FROM
                            worker_children
                            WHERE parent_id = %s
                            ORDER BY child_id;"""
    elif tableType == 'invalid':
        sql_querry = """SELECT
                            i.invalid_id,
                            it.disability_name,
                            i.invalid_start,
                            i.invalid_end
                            FROM
                            worker_invalid i LEFT JOIN disability_degrees it
                            ON i.invalid_disabilityID = it.disability_id 
                            WHERE invalid_workerID = %s
                            ORDER BY invalid_id;"""
    elif tableType == 'workhist':
        sql_querry = """SELECT
                            history_id,
                            history_companyName,
                            history_dateStart,
                            history_dateEnd,
                            history_urlopVacation,
                            history_urlopBaby,
                            history_urlopRequest,
                            history_urlopUnpaid,
                            history_absenceUnexcused,
                            history_equivalent
                            FROM
                            worker_workhistory
                            WHERE history_workerID = %s
                            ORDER BY history_id;"""
    elif tableType == 'urlop':
        sql_querry = """SELECT
                            u.urlop_id,
                            ut.urlop_name,
                            u.urlop_dateStart,
                            u.urlop_dateEnd,
                            u.urlop_days,
                            u.urlop_hours
                            FROM
                            worker_urlops u LEFT JOIN urlop_types ut
                            ON u.urlop_typeNumber = ut.urlop_id
                            WHERE urlop_workerID = %s
                            ORDER BY urlop_id;"""
    return sql_querry


def querryTextForms_insert(tableType):
    if tableType == 'agreements':
        sql_command = """INSERT INTO
                            worker_agreements(
                                workerAgreements_workerID,
                                workerAgreements_agreementType,
                                workerAgreements_dateStart,
                                workerAgreements_dateEnd,
                                workerAgreements_time)
                        VALUES(%s,%s,%s,%s,%s);"""
    elif tableType == 'child':
        sql_command = """INSERT INTO
                            worker_children(
                                parent_id,
                                child_name,
                                child_lastname,
                                child_birthDate)
                        VALUES(%s,%s,%s,%s);"""
    elif tableType == 'invalid':
        sql_command = """INSERT INTO
                            worker_invalid(
                                invalid_workerID,
                                invalid_disabilityID,
                                invalid_start,
                                invalid_end)
                        VALUES(%s,%s,%s,%s);"""
    elif tableType == 'workhist':
        sql_command = """INSERT INTO
                            worker_workhistory(
                                history_workerID,
                                history_companyName,
                                history_dateStart,
                                history_dateEnd,
                                history_urlopVacation,
                                history_urlopBaby,
                                history_urlopRequest,
                                history_urlopUnpaid,
                                history_absenceUnexcused,
                                history_equivalent)
                        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
    elif tableType == 'urlop':
        sql_command = """INSERT INTO
                            worker_urlops(
                                urlop_workerID,
                                urlop_typeNumber,
                                urlop_dateStart,
                                urlop_dateEnd,
                                urlop_days,
                                urlop_hours)
                        VALUES(%s,%s,%s,%s,%s,%s);"""
    return sql_command

def querryTextForms_newRecordID(tableType):
    if tableType == 'agreements':
        sql_command = """SELECT
                            workerAgreements_id
                        FROM
                            worker_agreements
                        ORDER BY workerAgreements_id
                        DESC LIMIT 1"""
    elif tableType == 'child':
        sql_command = """SELECT
                            child_id
                        FROM
                            worker_children
                        ORDER BY child_id
                        DESC LIMIT 1"""
    elif tableType == 'invalid':
        sql_command = """SELECT
                            invalid_id
                        FROM
                            worker_invalid
                        ORDER BY invalid_id
                        DESC LIMIT 1"""
    elif tableType == 'workhist':
        sql_command = """SELECT
                            history_id
                        FROM
                            worker_workhistory
                        ORDER BY history_id
                        DESC LIMIT 1"""
    elif tableType == 'urlop':
        sql_command = """SELECT
                            urlop_id
                        FROM
                            worker_urlops
                        ORDER BY urlop_id
                        DESC LIMIT 1"""
    return sql_command

def querryTextForms_delete(tableType):
    if tableType == 'agreements':
        sql_command = """DELETE FROM worker_agreements
                        WHERE workerAgreements_id = %s;"""
    elif tableType == 'child':
        sql_command = """DELETE FROM worker_children
                        WHERE child_id = %s;"""
    elif tableType == 'invalid':
        sql_command = """DELETE FROM worker_invalid
                        WHERE invalid_id = %s;"""
    elif tableType == 'workhist':
        sql_command = """DELETE FROM worker_workhistory
                        WHERE history_id = %s;"""
    elif tableType == 'urlop':
        sql_command = """DELETE FROM worker_urlops
                        WHERE urlop_id = %s;"""
    return sql_command

def querryTextForms_update(tableType):
    if tableType == 'agreements':
        sql_command = """UPDATE worker_agreements
                            SET
                                workerAgreements_agreementType = %s,
                                workerAgreements_dateStart = %s,
                                workerAgreements_dateEnd = %s,
                                workerAgreements_time = %s
                        WHERE workerAgreements_id = %s;"""
    elif tableType == 'child':
        sql_command = """UPDATE worker_children
                            SET
                                child_name = %s,
                                child_lastname = %s,
                                child_birthDate = %s
                        WHERE child_id = %s;"""
    elif tableType == 'childParent':
        sql_command = """UPDATE worker_children
                            SET
                                parent_id = %s,
                                child_name = %s,
                                child_lastname = %s,
                                child_birthDate = %s
                        WHERE child_id = %s;"""

    elif tableType == 'invalid':
        sql_command = """UPDATE worker_invalid
                            SET
                                invalid_disabilityID = %s,
                                invalid_start = %s,
                                invalid_end = %s
                        WHERE invalid_id = %s;"""
    elif tableType == 'workhist':
        sql_command = """UPDATE worker_workhistory
                            SET    
                                history_companyName = %s,
                                history_dateStart = %s,
                                history_dateEnd = %s,
                                history_urlopVacation = %s,
                                history_urlopBaby = %s,
                                history_urlopRequest = %s,
                                history_urlopUnpaid = %s,
                                history_absenceUnexcused = %s,
                                history_equivalent = %s
                        WHERE history_id = %s;"""
    elif tableType == 'urlop':
        sql_command = """UPDATE worker_urlops
                            SET
                                urlop_typeNumber = %s,
                                urlop_dateStart = %s,
                                urlop_dateEnd = %s,
                                urlop_days = %s,
                                urlop_hours = %s
                        WHERE urlop_id = %s;"""
    return sql_command

def querryText_getLastAgreement():
    sql_command = """SELECT workerAgreements_dateEnd 
                        FROM worker_agreements 
                        WHERE workerAgreements_workerID = %s 
                        ORDER BY workerAgreements_id DESC LIMIT 1;"""
    return sql_command