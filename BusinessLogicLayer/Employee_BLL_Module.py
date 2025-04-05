from DataAccessLayer.Employee_DAL_Module import Employee_DAL
from Model.EmployeeModel import EmployeeModelClass
from Model.EmployeeModel import EmployeeModelBClass
class Employee_BLL:
    def registerEmployee(self,employeeObject:EmployeeModelClass):
        employeeDAL_Object=Employee_DAL()
        employeeDAL_Object.registerEmployee(employeeObject)

    def getEmployeeList(self):
        employeeDAL_Object=Employee_DAL()
        return employeeDAL_Object.getEmployeeList()

    def employeeIDGenerator(self):
        employeeDAL_Object=Employee_DAL()
        return employeeDAL_Object.employeeIDGenerator()

    def deleteEmployee(self,emp_id):
        employeeDAL_Object=Employee_DAL()
        employeeDAL_Object.deleteEmployee(emp_id)

    def updateEmployee(self,employeeObject:EmployeeModelBClass):
        employeeDAL_Object=Employee_DAL()
        employeeDAL_Object.updateEmployee(employeeObject)

    def getJobList(self):
        employeeDAL_Object = Employee_DAL()
        return employeeDAL_Object.getJobList()

    def getPubList(self):
        employeeDAL_Object = Employee_DAL()
        return employeeDAL_Object.getPubList()

