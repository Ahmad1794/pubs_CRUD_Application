
import pyodbc
from Model.EmployeeModel import EmployeeModelClass
from Model.EmployeeModel import EmployeeModelBClass


class Employee_DAL:
    def registerEmployee(self,employeeObject:EmployeeModelClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[RegisterEmployee] ?,?,?,?,?,?,?"
        params=(employeeObject._fname,employeeObject._minit,employeeObject._lname,employeeObject._job
                ,employeeObject._job_lvl,employeeObject._pub,employeeObject._hire_date)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getEmployeeList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetEmployeeList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows


    def deleteEmployee(self,emp_id):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC [dbo].[DeleteEmployee] ?"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,(emp_id,) )
        connection.commit()

    def updateEmployee(self,employeeObject:EmployeeModelBClass):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="EXEC[dbo].[UpdateEmployee] ?,?,?,?,?,?,?,?"
        params=(employeeObject._fname,employeeObject._minit,employeeObject._lname,employeeObject._job,
                employeeObject._job_lvl,employeeObject._pub,employeeObject._hire_date,employeeObject._emp_id)
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        connection.commit()


    def getJobList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText="Execute [dbo].[GetJobList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText,)
        rows=cursor.fetchall()
        return rows

    def getPubList(self):
        connectionString = "Driver={SQL SERVER};Server=WINTERFELL;Database=pubs;Trusted_Connection=yes"
        commandText = "Execute [dbo].[GetPubList]"
        connection = pyodbc.connect(connectionString)
        cursor = connection.cursor()
        cursor.execute(commandText, )
        rows = cursor.fetchall()
        return rows

