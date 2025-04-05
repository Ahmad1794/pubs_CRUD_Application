from sqlite3.dbapi2 import paramstyle

import pyodbc
from Model.AuthorModel import AuthorModelClass
from Model.AuthorModel import AuthorModelBClass


class Author_DAL:
    def registerAuthor(self,authorObject:AuthorModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[RegisterAuthor] ?,?,?,?,?,?,?,?"
        params=(authorObject._au_lname,authorObject._au_fname,authorObject._phone,authorObject._address,authorObject._city,authorObject._state,authorObject._zip,authorObject._contract)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getAuthorList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetAuthorList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows

    def authorIDGenerator(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[GenerateNextAuthorId]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        new_au_id = cursor.fetchone()[0]
        return new_au_id


    def deleteAuthor(self,au_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeleteAuthor] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(au_id,) )
        connection.commit()

    def updateAuthor(self,authorObject:AuthorModelBClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdateAuthor] ?,?,?,?,?,?,?,?,?"
        params=(authorObject._au_lname,authorObject._au_fname,authorObject._phone,authorObject._address,authorObject._city,
                authorObject._state,authorObject._zip,authorObject._contract,authorObject._au_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()



