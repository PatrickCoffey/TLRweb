

import time
import copy

from django.db.transaction import rollback, commit, get_autocommit, set_autocommit
from django.db import connections

import constants
import queries

"""
tempbd
------
This is some logic from a previous projects, im placing in this file to 
copy past into other files later.
"""

def execQuery(sSQL, dic=None, db='etl'):
    cursor = connections[db].cursor()
    ret = {}
    if _checkSQL(sSQL, dic):
        if dic == None:
            cursor.execute(sSQL)
            ret = dictfetchall(cursor)
        else:
            cursor.execute(sSQL, dic)
            ret = dictfetchall(cursor)
    return ret

def _checkSQL(sSQL, dic):
    """Need to implement this properly!"""
    if str(sSQL).find(';') <= 1:
        return True

def getUsers():
    """Returns all users in the DB"""
    with connection.cursor() as cursor:
        sSQL = 'SELECT * FROM auth_user'
        cursor.execute(sSQL)
        ret = dictfetchall(cursor)
        return ret

def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()]

def updateTempDB(data):
    """Pushes data to the temp database. AKA Staging DB"""
    try:
        set_autocommit(False, constants.DB)
        data = dict(data)
        total = len(data)
        counter = 1
        for csvname, tabledata in data.iteritems():
            tabledata = list(tabledata)
            print('Current table: ' + csvname + '(' + str(counter) + '/' + str(total)) + ')'
            counter += 1
            print('Rows in current table: ' + str(len(tabledata)) + '\n')
            tablename = getTNfromCSV(csvname)
            execQuery('DELETE FROM ' + tablename, None, constants.DB)
            for row in tabledata:
                row = dict(row)
                sSQL = "INSERT INTO " + tablename + " "
                columns = ''
                placeholders = ''
                dataList = []
                for key in row.iterkeys():
                    keyName = key.replace('(', '').replace(')', '').replace(' ', '_')
                    columns += ', ' + (keyName)
                    placeholders += ', ?'
                    dataList.append(row[key])
                sSQL += '(%s) VALUES (%s)' % (columns, placeholders)
                sSQL = sSQL.replace(' (, ', ' (').replace(' (, ?, ', ' (')
                execQuery(sSQL, dataList, constants.DB)
    except Exception as e:
        rollback()
        raise e
    else:
        commit()
    finally:
        set_autocommit(True, constants.DB)

def extractTemp():
    """Pulls Data from the Temp database. AKA Staging DB"""
    data = {}
    print('running query...')
    data = execQuery(queries.SELECT_ALL, db=constants.DB)
    print('query ran')
    for item in data:
        print(item)

def parseCSV(csvfile):
    data = {}
    temp = {}
    headers = []
    i = 0
    k = 0
    j = 0
    with open(csvfile, 'rb') as f:
        for row in f:
            if 'Usual Clinic Name' in row:
                headers = row.replace('"','').strip('\n').split(',')
                if i != 0:
                    data[constants.QUERY_ORDER[i - 1]] = copy.copy(temp)
                temp = []
                i += 1
            else:
                dic = {}
                for j in range(len(headers)):
                    dic[headers[j]] = row.replace('"','').strip('\n').split(',')[j]
                temp.append(dic.copy())
            j += 1
        data[constants.QUERY_ORDER[i - 1]] = copy.copy(temp)
    ret = _cleanData(data)
    return ret

def _cleanData(data):
    """Currently only fixes dates... and removes non 1 ranked items... and blank items!"""
    tempdata = data
    ret = {}
    print("Cleaning Data...")
    for csvname, tabledata in tempdata.iteritems():
        print("Cleaning " + csvname + "!")
        for row in tabledata[:]:
            if 'Result Desc' in row.iterkeys() and 'Result Measure' in row.iterkeys():
                if _canBeNumeric(row['Result Desc']):
                    if row['Result Desc'] != row['Result Measure']:
                        data[csvname].remove(row)
                        continue
                    elif row['Result Desc'] == '' and row['Result Measure'] == '':
                        data[csvname].remove(row)
                        continue
            for colname, val in row.iteritems():
                if "date" in colname.lower() and "rank" in colname.lower():
                    if not str(val) == '1':
                        data[csvname].remove(row)
                if "date" in colname.lower() and not "rank" in colname.lower():
                    row[colname] = str(val).replace('/', '-')
    return data

def getTNfromCSV(csvName):
    for csv, table in CSVMap.iteritems():
        if csv == csvName:
            return constants.db_prefix + table

def _canBeNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def _pushToProd():
    for key in CSVMap.iterkeys():
        tablename = getTNfromCSV(key)

if __name__ == '__main__':
    sTime = time.time()
    csvfile = 'C:/Users/Pat12/Documents/Reports/TLR+V8.3+test.csv'
    testData = parseCSV(csvfile)

    fTime = time.time()
    print(str(fTime-sTime) + ' secs for parse')

    updateDB(testData)

    fTime = time.time()
    print(str(fTime-sTime) + ' secs for all!')
    print(execQuery('''SELECT 
    result_component, 
    HRN, 
    Result_Measure, 
    Usual_Clinic_Name, 
    Result_Desc, 
    RANK_Result_Date_DESC, 
    Result_Date 
    FROM DjangoTLR_csvSysBP''', None, constants.DB))