from DataAccessLayer.Title_DAL_Module import Title_DAL
from Model.TitleModel import TitleModelClass
from Model.TitleModel import TitleModelBClass
class Title_BLL:
    def registerTitle(self,titleObject:TitleModelClass):
        titleDAL_Object=Title_DAL()
        titleDAL_Object.registerTitle(titleObject)

    def getTitleList(self):
        titleDAL_Object=Title_DAL()
        return titleDAL_Object.getTitleList()



    def deleteTitle(self,au_id):
        titleDAL_Object=Title_DAL()
        titleDAL_Object.deleteTitle(au_id)

    def updateTitle(self,titleObject:TitleModelBClass):
        titleDAL_Object=Title_DAL()
        titleDAL_Object.updateTitle(titleObject)

    def getPubList(self):
        titleDAL_Object = Title_DAL()
        return titleDAL_Object.getPubList()
