from DataAccessLayer.Author_DAL_Module import Author_DAL
from Model.AuthorModel import AuthorModelClass
from Model.AuthorModel import AuthorModelBClass
class Author_BLL:
    def registerAuthor(self,authorObject:AuthorModelClass):
        authorDAL_Object=Author_DAL()
        authorDAL_Object.registerAuthor(authorObject)

    def getAuthorList(self):
        authorDAL_Object=Author_DAL()
        return authorDAL_Object.getAuthorList()

    def authorIDGenerator(self):
        authorDAL_Object=Author_DAL()
        return authorDAL_Object.authorIDGenerator()

    def deleteAuthor(self,au_id):
        authorDAL_Object=Author_DAL()
        authorDAL_Object.deleteAuthor(au_id)

    def updateAuthor(self,authorObject:AuthorModelBClass):
        authorDAL_Object=Author_DAL()
        authorDAL_Object.updateAuthor(authorObject)

