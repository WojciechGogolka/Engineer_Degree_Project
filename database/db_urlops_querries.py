def urlopQuerryText_selectAgreement():
    sql_querry = """SELECT workerAgreements_id 
                        FROM worker_agreements w
                        LEFT JOIN agreement_types a
                        ON w.workerAgreements_agreementType = a.agreement_id
                        WHERE(
                            w.workerAgreements_dateEnd is Null
                            or
                            w.workerAgreements_dateEnd > curdate())
                            and a.agreement_countToUrlop = 1
                            and w.workerAgreements_workerID = %s
                            LIMIT 1;"""
    return sql_querry

def querryText_workerChildsCount():
    sql_querry = """SELECT 
                        count(child_id)
                        FROM worker_children 
                        WHERE 
                        parent_id = %s
                        and DATE_FORMAT(FROM_DAYS(TO_DAYS(NOW())-TO_DAYS(child_birthDate)), '%Y')+0 < 14;"""
    return sql_querry

def querryText_urlopAnnualDays():
    sql_querry = """SELECT 
                        urlop_yearlyLimit
                        FROM urlop_types
                        WHERE urlop_id = %s;"""
    return sql_querry

def urlopQuerryText_usedDaysCount():
    sql_querry = """SELECT
                        SUM(urlop_days)
                            FROM
                                worker_urlops
                            WHERE urlop_workerID = %s
                            and urlop_typeNumber = %s
                            and year(urlop_dateEnd) = year(curdate()) ;"""
    return sql_querry

def urlopQuerryText_usedDaysPaidUrlop():
    sql_querry = """SELECT
                        SUM(urlop_days)
                            FROM
                                worker_urlops
                            WHERE urlop_workerID = %s
                            and urlop_typeNumber = 1;"""
    return sql_querry

def urlopQuerryText_workHistory(urlopType):
    if urlopType == 'paidUrlop':
        sql_querry = """SELECT SUM(history_urlopVacation) """
    elif urlopType == 'childcare':
        sql_querry = """SELECT SUM(history_urlopBaby) """
    elif urlopType == 'requested':
        sql_querry = """SELECT SUM(history_urlopRequest) """
    elif urlopType == 'unpaid':
        sql_querry = """SELECT SUM(history_urlopUnpaid) """
    elif urlopType == 'absenceUnexcused':
        sql_querry = """SELECT SUM(history_absenceUnexcused) """
    sql_querry += """FROM
                        worker_workhistory
                        WHERE history_workerID = %s
                        and year(history_dateEnd) = year(curdate()) ;"""
    return sql_querry

def querryText_getDisabilityIndex():
    sql_querry = """SELECT invalid_id
                            FROM worker_invalid i 
                            JOIN disability_degrees d ON i.invalid_disabilityID = d.disability_id 
                            WHERE invalid_workerID = %s and disability_addUrlop > 0 ; """
    return sql_querry