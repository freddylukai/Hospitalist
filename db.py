import sys
import mysql.connector
from mysql.connector import errorcode
from flask import Flask

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
        " `Queue` int(5) NOT NULL,"
        " `ESI` int NOT NULL DEFAULT 5"
        ")"
    )
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format('triage'))
    except mysql.connector.Error as err:
        print >>sys.stderr, "Create database failure"
        print >>sys.stderr, err


try:
    connect = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='triage')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print >>sys.stderr, "Error: Access Denied. Make sure the administrator password is correct."
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print "Database does not exist, creating now."
        createdb(connect.cursor())
    else:
        print >>sys.stderr, err

else:
    connect.close()
