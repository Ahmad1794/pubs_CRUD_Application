import pyodbc
from Model.PublisherModel import PublisherModelClass
from Model.PublisherModel import PublisherModelBClass


class Publisher_DAL:
    def registerPublisher(self,publisherObject:PublisherModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[RegisterPublisher] ?,?,?,?"
        params=(publisherObject._pub_name,publisherObject._city,publisherObject._state,
                publisherObject._country)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getPublisherList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetPublisherList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows



    def deletePublisher(self,pub_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeletePublisher] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(pub_id,) )
        connection.commit()

    def updatePublisher(self,publisherObject:PublisherModelBClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdatePublisher] ?,?,?,?,?"
        params=(publisherObject._pub_name,publisherObject._city,
                publisherObject._state,publisherObject._country,publisherObject._pub_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()



