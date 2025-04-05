import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage
from PIL import Image,ImageTk




class MainForm :
    def mainFormLoad(self):
        mainForm = Tk()
        mainForm.title('Main Form')
        mainForm.geometry('800x600')
        mainForm.iconbitmap('Images/shop.ico')
        mainForm.resizable(0, 0)
        x = int(mainForm.winfo_screenwidth() // 2 - 800 // 2)
        y = int(mainForm.winfo_screenheight() // 2 - 600 // 2)
        mainForm.geometry('+{}+{}'.format(x, y))
        image = Image.open('Images/mainbackg.png')
        bg_image = ImageTk.PhotoImage(image)
        label = Label(mainForm, image=bg_image)
        label.place(x=0, y=0, relwidth=1, relheight=1)





        def authorCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.AuthorModule import AuthorCRUD
            authorCRUDObject=AuthorCRUD()
            authorCRUDObject.authorCRUD_FormLoad()

        authorImage=PhotoImage(file='Images/button_authors.png')
        authorbtn = Button(mainForm,command=authorCRUD,image=authorImage)
        authorbtn.grid(row=1, column=1,padx=35,pady=35)

        def employeeCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.EmployeeModule import EmployeeCRUD
            employeeCRUDObject=EmployeeCRUD()
            employeeCRUDObject.employeeCRUD_FormLoad()

        employeeImage=PhotoImage(file='Images/button_employees.png')
        employeebtn = Button(mainForm,command=employeeCRUD,image=employeeImage)
        employeebtn.grid(row=1, column=2,padx=25,pady=10)

        def publisherCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.PublisherModule import PublisherCRUD
            publisherCRUDObject=PublisherCRUD()
            publisherCRUDObject.publisherCRUD_FormLoad()

        publisherImage=PhotoImage(file='Images/button_publishers.png')
        publisherbtn = Button(mainForm,command=publisherCRUD, image=publisherImage)
        publisherbtn.grid(row=1, column=3,padx=25,pady=10)

        def saleCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.SaleModule import SaleCRUD
            saleCRUDObject=SaleCRUD()
            saleCRUDObject.saleCRUD_FormLoad()

        saleImage=PhotoImage(file='Images/button_sales.png')
        salebtn = Button(mainForm,command=saleCRUD, image=saleImage)
        salebtn.grid(row=2, column=1,padx=25,pady=10)

        def storeCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.StoreModule import StoreCRUD
            storeCRUDObject=StoreCRUD()
            storeCRUDObject.storeCRUD_FormLoad()

        storeImage=PhotoImage(file='Images/button_stores.png')
        storebtn = Button(mainForm,command=storeCRUD, image=storeImage)
        storebtn.grid(row=2, column=2,padx=25,pady=10)

        def titleCRUD():
            mainForm.destroy()
            from UserInterfaceLayer.TitleModule import TitleCRUD
            titleCRUDObject=TitleCRUD()
            titleCRUDObject.titleCRUD_FormLoad()

        titleImage=PhotoImage(file='Images/button_titles.png')
        titlebtn = Button(mainForm,command=titleCRUD, image=titleImage)
        titlebtn.grid(row=2, column=3,padx=25,pady=10)


        exitImage=PhotoImage(file='Images/button_exit.png')
        exitbtn=Button(mainForm,command=mainForm.destroy,image=exitImage)
        exitbtn.grid(row=3,column=2,padx=25,pady=35)




        mainForm.mainloop()



