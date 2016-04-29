from flask import Flask
from flask import request
import sys
import mysql.connector
from mysql.connector import errorcode

TABLES = {}
TABLES['patients'] = (
    "CREATE TABLE IF NOT EXISTS `patients` ("
    " `ID`  int(9) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    " `LastName` varchar(16) NOT NULL,"
    " `FirstName` varchar(16) NOT NULL,"
    " `Age` int NOT NULL DEFAULT 0,"
    " `Queue` int(5) NOT NULL,"
    " `ESI` int NOT NULL DEFAULT 5"
    ")"
)
TABLES['resourcetypes'] = (
    "CREATE TABLE IF NOT EXISTS `resourcetypes` ("
    " `ID` int(6) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    " `Name` varchar(40) NOT NULL,"
    " `Total` int(5) NOT NULL DEFAULT 0,"
    " `Available` int(5) NOT NULL DEFAULT 0"
    ")"
)
TABLES['resources'] = (
    "CREATE TABLE IF NOT EXISTS`resources` ("
    " `ID` int(9) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
    " `Type` int(6) NOT NULL,"
    " `Name` varchar(40) NOT NULL,"
    " `Patient` int(9) NOT NULL DEFAULT 0,"
    " CONSTRAINT `res_type` FOREIGN KEY (`Type`) REFERENCES `resourcetypes` (`ID`) ON DELETE CASCADE"
    ")"
)

def initialize_db(cursor, connection):
    msgs = ""
    try:
        cursor.execute("DROP TABLE IF EXISTS resources")
        cursor.close()
        connection.commit()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS resourcetypes")
        cursor.close()
        connection.commit()
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS patients")
        cursor.close()
        connection.commit()
        cursor = connection.cursor()
        for name, iter in TABLES.iteritems():
            cursor.execute(iter)
            cursor.close()
            connection.commit()
            cursor = connection.cursor()
    except mysql.connector.Error as err:
        msgs += str(err) + "\n"
    return msgs

app = Flask(__name__)

app.debug = True

@app.route('/')
#default
def default():
    tables = ""
    connect = mysql.connector.connect(user='root', password='password',
                                     host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306', database='triage')
    cursor = connect.cursor()
    cursor.execute("SHOW tables")
    for i in cursor.fetchall():
        tables += str(i) + " "
    return "You are at the default webpage. Tables in DB are: " + tables

@app.route('/initialize/')
def create_db():
    connect = mysql.connector.connect(user='root', password='password', host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306')
    cursor = connect.cursor()
    try:
        connect.database = 'triage'
        errors = initialize_db(cursor, connect)
        if errors == "":
            return "Nothing more to do."
        else:
            return errors
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            return "Error: Access denied. Contact the server administrator for details."
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            return "Error: Database does not exist."
        else:
            return "Unknown error." +str(err)

    else:
        cursor.close()
        connect.close()

@app.route('/newresource/', methods=['POST'])
def newresource():
    data = request.form
    connect = mysql.connector.connect(user='root', password='password', host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306', database='triage')
    cursor = connect.cursor()
    query = ("INSERT INTO resourcetypes (Name, Total, Available) VALUES (%s, %s, %s)")
    name = data['name']
    total = data['total']
    cursor.execute(query, (name, total, total))
    cursor.close()
    connect.commit()
    connect.close()
    return "Added."

@app.route('/fixresources/')
def fixres():
    connect = mysql.connector.connect(user='root', password='password',
                                      host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306',
                                      database='triage')
    cursor = connect.cursor()
    query = ("SELECT ID, Name, Total FROM resourcetypes")
    cursor.execute(query)
    connect2 = mysql.connector.connect(user='root', password='password',
                                      host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306',
                                      database='triage')
    cursor2 = connect2.cursor()
    for (id, name, total) in cursor:
        for x in range(0, int(total)):
            query2 = ("INSERT INTO resources (Type, Name) VALUES (%s, %s)")
            cursor2.execute(query2, (id, name))
            cursor2.close()
            connect2.commit()
            cursor2 = connect2.cursor()
    connect.close()
    return "Fixed."

@app.route('/newpatient/', methods=['POST'])
def newpatient():
    data = request.form
    connect = mysql.connector.connect(user='root', password='password', host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306', database='triage')
    cursor = connect.cursor()
    query = ("INSERT INTO patients (LastName, FirstName, Age, Queue, ESI) VALUES (%s, %s, %s, %s, %s)")
    #TODO: Write a legit queuing algorithm
    firstname = data['first_name']
    lastname = data['last_name']
    age = data['age']
    esi = data['esi']
    resources = data['res']
    allrequired = str.split(str(resources), ",")
    mostrecent = 1
    cursor.execute(query, (lastname, firstname, age, esi, mostrecent))
    cursor.close()
    connect.commit()
    cursor = connect.cursor()
    for resource in allrequired:
        query = ("SELECT Available FROM resourcetypes WHERE ID=%s")
        cursor.execute(query, (resource,))
        for (avail,) in cursor:
            connect2 = mysql.connector.connect(user='root', password='password',
                                              host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com',
                                              port='3306', database='triage')
            cursor2 = connect.cursor()
            query = ("UPDATE resourcetypes SET Available=%s WHERE ID=%s")
            cursor2.execute(query, (str(int(avail)-1), str(resource)))
            cursor2.close()
            connect2.commit()
        query = ("SELECT ID FROM resources WHERE Type=%s LIMIT 1")
        cursor.execute(query, (resource,))
        for (id1,) in cursor:
            connect2 = mysql.connector.connect(user='root', password='password',
                                               host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com',
                                               port='3306', database='triage')
            cursor2 = connect.cursor()
            query1 = ("UPDATE resources SET Patient=%s WHERE ID=%s")
            query2 = ("SELECT ID FROM patients ORDER BY ID DESC LIMIT 1")
            cursor2.execute(query2)
            for (id2,) in cursor2:
                connect3 = mysql.connector.connect(user='root', password='password',
                                                   host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com',
                                                   port='3306', database='triage')
                cursor3 = connect.cursor()
                cursor3.execute(query1, (id2, id1))
                cursor3.close()
                connect3.commit()
    connect.close()
    connect2.close()
    connect3.close()
    return "Completed"


@app.route('/queue/')
def getqueue():
    str1 = ""
    str1 +=  '{"patients":['
    query = ("SELECT FirstName, LastName, ID, Age, ESI FROM patients ORDER BY Queue ASC")
    connect = mysql.connector.connect(user='root', password='password', host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306', database='triage')
    cursor = connect.cursor()
    cursor.execute(query)
    for (FirstName, LastName, ID, Age, ESI) in cursor:
        str1 += '{{"firstname":"{}",'.format(FirstName)
        str1 += '"lastname":"{}",'.format(LastName)
        str1 += '"ID":"{}",'.format(ID)
        str1 += '"age":"{}",'.format(Age)
        str1 += '"esi":"{}"}},'.format(ESI)
    str1 = str1[:-1]
    str1 += ']}'
    return str1

@app.route('/deletepatient/', methods=['POST'])
def delpatient():
    patid = request.form['id']
    query = ("DELETE FROM patients WHERE ID=%s")
    connect = mysql.connector.connect(user='root', password='password', host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306', database='triage')
    cursor = connect.cursor()
    cursor.execute(query, (patid,))
    cursor.close()
    connect.commit()
    connect.close()
    return "OK."

@app.route('/resourceview/')
def getresources():
    str1 = ""
    str1 += '{"resources":['
    query = ("SELECT Name, Total, Available FROM resourcetypes")
    connect = mysql.connector.connect(user='root', password='password',
                                      host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306',
                                      database='triage')
    cursor = connect.cursor()
    cursor.execute(query)
    for (Name, Total, Avail) in cursor:
        str1 += '{{"name":"{}",'.format(Name)
        str1 += '"total":"{}",'.format(Total)
        str1 += '"available":"{}"}},'.format(Avail)
    str1 = str1[:-1]
    str1 += ']}'
    return str1

@app.route('/updatewebview/')
def webview():
    str1 = ""
    with open("tophalf.txt", "r") as top:
        str1 += top.read()
    query = ("SELECT FirstName, LastName, ESI FROM patients ORDER BY Queue ASC")
    connect = mysql.connector.connect(user='root', password='password',
                                      host='triageinstance.ccqpts7hcb67.us-east-1.rds.amazonaws.com', port='3306',
                                      database='triage')
    cursor = connect.cursor()
    cursor.execute(query)
    str1 +='<div class="gridright">'
    for (FirstName, LastName, ESI) in cursor:
        str1 += '<div class="grid-item">' + "<p>" + LastName + ", " + FirstName + ": " + str(ESI) + "</p></div>\n"
    str1 +='</div>\n'
    str1 +='<div class="gridleft">'
    query2 = ("SELECT Name, Total, Available FROM resourcetypes")
    cursor.execute(query2)
    for (Name, Total, Available) in cursor:
        str1 += '<div class="grid-item">' + "<p>" + Name + ": " + str(Available) + "/" + str(Total) + "</p></div>\n"
    str1 +="</div>\n"
    with open("bottomhalf.txt", "r") as bottom:
        str1 += bottom.read()
    return str1

if __name__ == '__main__':
    app.run()
