from DataAccessLayer.Store_DAL_Module import Store_DAL
from Model.StoreModel import StoreModelClass
from Model.StoreModel import StoreModelBClass

class Store_BLL:
    def registerStore(self,storeObject:StoreModelClass):
        storeDAL_Object=Store_DAL()
        storeDAL_Object.registerStore(storeObject)

    def getStoreList(self):
        storeDAL_Object=Store_DAL()
        return storeDAL_Object.getStoreList()

    def storeIDGenerator(self):
        storeDAL_Object=Store_DAL()
        return storeDAL_Object.storeIDGenerator()

    def deleteStore(self,StoreID):
        storeDAL_Object=Store_DAL()
        storeDAL_Object.deleteStore(StoreID)

    def updateStore(self,storeObject:StoreModelBClass):
        storeDAL_Object=Store_DAL()
        storeDAL_Object.updateStore(storeObject)

