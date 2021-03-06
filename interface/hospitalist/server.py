from flask import Flask
from flask import request
import sys
import mysql.connector
from mysql.connector import errorcode

def createdb(cursor):
    TABLES = {}
    TABLES['resourcetypes'] = (
        "CREATE TABLE `resourcetypes` ("
        " `ID` int(6) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        " `Name` varchar(40) NOT NULL,"
        " `Total` int(5) NOT NULL DEFAULT 0,"
        " `Available` int(5) NOT NULL DEFAULT 0"
        ")"
    )
    TABLES['resources'] = (
        "CREATE TABLE `resources` ("
        " `ID` int(9) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        " `Type` int(6) NOT NULL FOREIGN KEY REFERENCES `resourcetypes` (`ID`)"
        " `Name` varchar(40) NOT NULL,"
        " `Patient` int(9) NOT NULL DEFAULT 0 FOREIGN KEY REFERENCES `patients` (`ID`)"
        ")"
    )
    TABLES['patients'] = (
        "CREATE TABLE  `patients` ("
        " `ID`  int(9) NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        " `LastName` varchar(16) NOT NULL."
        " `FirstName` varchar(16) NOT NULL,"
        " `Age` int NOT NULL DEFAULT 0"
        " `Queue` int(5) NOT NULL,"
        " `ESI` int NOT NULL DEFAULT 5"
        ")"
    )
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('triage'))
    except mysql.connector.Error as err:
        print >>sys.stderr, "Create database failure"
        print >>sys.stderr, err

app = Flask(__name__)

@app.route('/')
#default
def create_db():
    connect = mysql.connector.connect(user='root', password='password', host='127.0.0.1')
    cursor = connect.cursor()
    try:
        connect.database = 'triage'
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print >> sys.stderr, "Error: Access Denied. Make sure the administrator password is correct."
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist, creating now."
            createdb(cursor)
        else:
            print >> sys.stderr, err

    else:
        connect.close()

@app.route('/newresource/', methods=['POST'])
def newresource():
    data = request.form
    connect = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='triage')
    cursor = connect.cursor()
    query = ("INSERT INTO resourcetypes (Name, Total) VALUES (%s, %i)")
    name = data['name']
    total = data['total']
    cursor.execute(query, (name, total))


@app.route('/newpatient/', methods=['POST'])
def newpatient():
    data = request.form
    connect = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='triage')
    cursor = connect.cursor()
    query = ("INSERT INTO patients (LastName, FirstName, Age, Queue, ESI) VALUES (%s, %s, %i, %i, %i)")
    #TODO: Write a legit queuing algorithm
    firstname = data['first_name']
    lastname = data['last_name']
    age = data['age']
    esi = data['esi']
    mostrecent = ("SELECT TOP 1 Queue FROM patients SORT BY Queue DESC") + 1
    cursor.execute(query, (firstname, lastname, age, esi, mostrecent))




@app.route('/queue/')
def getqueue():
    print '<?xml version="1.0" encoding="UTF-8"?>'
    query = ("SELECT FirstName, LastName, Age, ESI FROM patients SORT BY Queue ASC")
    connect = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='triage')
    cursor = connect.cursor()
    cursor.execute(query)
    for (FirstName, LastName, ESI) in cursor:
        print '<patient>'
        print '\t<first_name>%s</first_name>'.format(FirstName)
        print '\t<last_name>%s</last_name>'.format(LastName)
        print '\t<esi>%i</esi>'.format(ESI)
        print '</patient>'

if __name__ == '__main__':
    app.run()