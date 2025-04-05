from DataAccessLayer.Publisher_DAL_Module import Publisher_DAL
from Model.PublisherModel import PublisherModelClass
from Model.PublisherModel import PublisherModelBClass

class Publisher_BLL:
    def registerPublisher(self,publisherObject:PublisherModelClass):
        publisherDAL_Object=Publisher_DAL()
        publisherDAL_Object.registerPublisher(publisherObject)

    def getPublisherList(self):
        publisherDAL_Object=Publisher_DAL()
        return publisherDAL_Object.getPublisherList()

    def publisherIDGenerator(self):
        publisherDAL_Object=Publisher_DAL()
        return publisherDAL_Object.publisherIDGenerator()

    def deletePublisher(self,publisherID):
        publisherDAL_Object=Publisher_DAL()
        publisherDAL_Object.deletePublisher(publisherID)

    def updatePublisher(self,publisherObject:PublisherModelBClass):
        publisherDAL_Object=Publisher_DAL()
        publisherDAL_Object.updatePublisher(publisherObject)

