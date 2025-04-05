import pyodbc
from Model.StoreModel import StoreModelClass
from Model.StoreModel import StoreModelBClass


class Store_DAL:
    def registerStore(self,storeObject:StoreModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[RegisterStore] ?,?,?,?,?"
        params=(storeObject._stor_name,storeObject._stor_address,storeObject._city,
                storeObject._state,storeObject._zip)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getStoreList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetStoreList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows



    def deleteStore(self,stor_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeleteStore] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(stor_id,) )
        connection.commit()

    def updateStore(self,storeObject:StoreModelBClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdateStore] ?,?,?,?,?,?"
        params=(storeObject._stor_name,storeObject._stor_address,storeObject._city,
                storeObject._state,storeObject._zip,storeObject._stor_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()



