from DataAccessLayer.Sale_DAL_Module import Sale_DAL
from Model.SaleModel import SaleModelClass
class Sale_BLL:
    def registerSale(self,saleObject:SaleModelClass):
        saleDAL_Object=Sale_DAL()
        saleDAL_Object.registerSale(saleObject)

    def getSaleList(self):
        saleDAL_Object=Sale_DAL()
        return saleDAL_Object.getSaleList()

    def saleIDGenerator(self):
        saleDAL_Object=Sale_DAL()
        return saleDAL_Object.saleIDGenerator()

    def deleteSale(self,stor_id,ord_num,ord_date,qty,payterms,title_id):
        saleDAL_Object=Sale_DAL()
        saleDAL_Object.deleteSale(stor_id,ord_num,ord_date,qty,payterms,title_id)

    def updateSale(self,new_stor_id,old_stor_id,new_ord_num,old_ord_num,new_ord_date,old_ord_date,
                   new_qty,old_qty,new_payterms,old_payterms,new_title_id,old_title_id):
        saleDAL_Object=Sale_DAL()
        saleDAL_Object.updateSale(new_stor_id,old_stor_id,new_ord_num,old_ord_num,new_ord_date,old_ord_date,
                   new_qty,old_qty,new_payterms,old_payterms,new_title_id,old_title_id)


    def getStoreList(self):
        saleDAL_Object = Sale_DAL()
        return saleDAL_Object.getStoreList()

    def getTitleList(self):
        saleDAL_Object = Sale_DAL()
        return saleDAL_Object.getTitleList()