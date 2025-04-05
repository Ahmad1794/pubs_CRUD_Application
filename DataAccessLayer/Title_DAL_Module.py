from sqlite3.dbapi2 import paramstyle

import pyodbc
from Model.TitleModel import TitleModelClass
from Model.TitleModel import TitleModelBClass


class Title_DAL:
    def registerTitle(self,titleObject:TitleModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[RegisterTitle] ?,?,?,?,?,?,?,?,?"
        params=(titleObject._title,titleObject._type,titleObject._pub,titleObject._price,
                titleObject._advance,titleObject._royalty,titleObject._ytd_sales,titleObject._notes,titleObject._pubdate)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getTitleList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetTitleList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows




    def deleteTitle(self,au_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeleteTitle] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(au_id,) )
        connection.commit()

    def updateTitle(self,titleObject:TitleModelBClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdateTitle] ?,?,?,?,?,?,?,?,?"
        params=(titleObject._au_lname,titleObject._au_fname,titleObject._phone,titleObject._address,titleObject._city,
                titleObject._state,titleObject._zip,titleObject._contract,titleObject._au_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()

    def getPubList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText = "Execute [dbo].[GetPubList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

