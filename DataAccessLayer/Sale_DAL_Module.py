from sqlite3.dbapi2 import paramstyle

import pyodbc
from Model.SaleModel import SaleModelClass


class Sale_DAL:
    def registerSale(self,saleObject:SaleModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[RegisterSale] ?,?,?,?,?,?"
        params=(saleObject._stor_id,saleObject._ord_num,saleObject._ord_date,saleObject._qty,
                saleObject._payterms,saleObject._title_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getSaleList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetSaleList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows

    # def saleIDGenerator(self):
    #     connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
    #     commandText="EXEC[dbo].[GenerateNextSaleId]"
    #     connection = pyodbc.connect(connectionString)
    #     cursor = connection.cursor()
    #     cursor.execute(commandText,)
    #     new_au_id = cursor.fetchone()[0]
    #     return new_au_id


    def deleteSale(self,stor_id,ord_num,ord_date,qty,payterms,title_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeleteSale] ?,?,?,?,?,?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(stor_id,ord_num,ord_date,qty,payterms,title_id,) )
        connection.commit()

    def updateSale(self,new_stor_id,old_stor_id,new_ord_num,old_ord_num,new_ord_date,old_ord_date,
                   new_qty,old_qty,new_payterms,old_payterms,new_title_id,old_title_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdateSale] ?,?,?,?,?,?,?,?,?,?,?,?"
        params=(new_stor_id,old_stor_id,new_ord_num,old_ord_num,new_ord_date,old_ord_date,
                   new_qty,old_qty,new_payterms,old_payterms,new_title_id,old_title_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getStoreList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText = "Execute [dbo].[GetStoreListForSale]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows



    def getTitleList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText = "Execute [dbo].[GetTitleListForSale]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows
