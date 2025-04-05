from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage

from UserInterfaceLayer.MainModule import MainForm
from BusinessLogicLayer.Author_BLL_Module import Author_BLL
from Model.AuthorModel import AuthorModelClass
from Model.AuthorModel import AuthorModelBClass

class AuthorCRUD:
    def authorCRUD_FormLoad(self):


        def backToMainForm():
            authorCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            intContract.set(None)
            txtau_idValue.set("")

        def registerAuthor():
            authorBLLObject=Author_BLL()
            au_lname=txtAuthorLastName.get()
            au_fname=txtAuthorFirstName.get()
            phone=txtPhone.get()
            address=txtAddress.get()
            city=txtCity.get()
            state=txtState.get()
            zip=txtZipCode.get()
            contract=intContract.get()
            authorObject=AuthorModelClass(au_lname=au_lname,au_fname=au_fname,phone=phone,address=address,city=city,state=state,zip=zip,contract=contract)
            authorBLLObject.registerAuthor(authorObject)
            showList()


        def onTreeSelect(event):
            resetForm()
            index=tvAuthorList.selection()
            if index:
                selectedvalues=tvAuthorList.item(index)['values']
                txtau_idValue.set(selectedvalues[1])
                txtAuthorLastName.set(selectedvalues[2])
                txtAuthorFirstName.set(selectedvalues[3])
                txtPhone.set(selectedvalues[4])
                txtAddress.set(selectedvalues[5])
                txtCity.set(selectedvalues[6])
                txtState.set(selectedvalues[7])
                txtZipCode.set(selectedvalues[8])
                contract= selectedvalues[9]
                if contract=='True':
                    intContract.set(1)
                elif contract=='False':
                    intContract.set(0)

        def deleteAuthor():
            authorID=txtau_idValue.get()
            if authorID:
                from BusinessLogicLayer.Author_BLL_Module import Author_BLL
                authorBLLObject=Author_BLL()
                authorBLLObject.deleteAuthor(authorID)
            showList()


        def showList(*args):
            from BusinessLogicLayer.Author_BLL_Module import Author_BLL
            authorBLLObject=Author_BLL()
            rows = authorBLLObject.getAuthorList()
            tvAuthorList.delete(*tvAuthorList.get_children())

            rowCount=0
            for row in rows:
                rowCount+=1
                values=[rowCount]
                for value in row:
                    if value==None:
                        values.append("")
                    else:
                        values.append(value)
                tvAuthorList.insert("","end",values=values)

        def updateAuthor():
            authorID=txtau_idValue.get()
            authorLastName=txtAuthorLastName.get()
            authorFirstName=txtAuthorFirstName.get()
            phone=txtPhone.get()
            address=txtAddress.get()
            city=txtCity.get()
            state=txtState.get()
            zip=txtZipCode.get()
            contract=intContract.get()
            authorObject=AuthorModelBClass(authorLastName,authorFirstName,phone,address,city,state,zip,contract,authorID)

            if authorID:
                from BusinessLogicLayer.Author_BLL_Module import Author_BLL
                authorBLLObject = Author_BLL()
                authorBLLObject.updateAuthor(authorObject)

            showList()
            resetForm()






        authorCRUDForm = Tk()
        authorCRUDForm.title('Author CRUD Form')
        authorCRUDForm.geometry('1200x600')
        authorCRUDForm.iconbitmap('Images/author.ico')
        authorCRUDForm.resizable(0, 0)
        x = int(authorCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(authorCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        authorCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(authorCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lblau_id = Label(lblBasicInfo, text='AuthorID: ')
        lblau_id.grid(row=0, column=0, padx=10, pady=10)

        txtau_idValue = StringVar()
        lblau_idValue = Label(lblBasicInfo, text='AuthorIDValue: ', textvariable=txtau_idValue)
        lblau_idValue.grid(row=0, column=1, padx=10, pady=10,sticky=W)

        lblau_lname = Label(lblBasicInfo, text='Author Last Name: ')
        lblau_lname.grid(row=1, column=0, padx=10, pady=10)

        txtAuthorLastName = StringVar()
        entAuthorLastName = ttk.Entry(lblBasicInfo, width=40, textvariable=txtAuthorLastName)
        entAuthorLastName.grid(row=1, column=1, padx=10, pady=10)

        lblau_fname = Label(lblBasicInfo, text='Author First Name: ')
        lblau_fname.grid(row=2, column=0, padx=10, pady=10)

        txtAuthorFirstName = StringVar()
        entAuthorFirstName = ttk.Entry(lblBasicInfo, width=40, textvariable=txtAuthorFirstName)
        entAuthorFirstName.grid(row=2, column=1, padx=10, pady=10)

        lblPhone = Label(lblBasicInfo, text='Phone: ')
        lblPhone.grid(row=3, column=0, padx=10, pady=10)

        txtPhone = StringVar()
        entPhone = ttk.Entry(lblBasicInfo, width=40, textvariable=txtPhone)
        entPhone.grid(row=3, column=1, padx=10, pady=10)

        lblAddress = Label(lblBasicInfo, text='Address: ')
        lblAddress.grid(row=4, column=0, padx=10, pady=10)

        txtAddress = StringVar()
        entAddress = ttk.Entry(lblBasicInfo, width=40, textvariable=txtAddress)
        entAddress.grid(row=4, column=1, padx=10, pady=10)

        lblCity = Label(lblBasicInfo, text='City: ')
        lblCity.grid(row=5, column=0, padx=10, pady=10)

        txtCity = StringVar()
        entCity = ttk.Entry(lblBasicInfo, width=40, textvariable=txtCity)
        entCity.grid(row=5, column=1, padx=10, pady=10)


        lblState = Label(lblBasicInfo, text='State: ')
        lblState.grid(row=6, column=0, padx=10, pady=10)

        txtState = StringVar()
        entState = ttk.Entry(lblBasicInfo, width=40, textvariable=txtState)
        entState.grid(row=6, column=1, padx=10, pady=10)


        lblZipCode = Label(lblBasicInfo, text='Zip Code: ')
        lblZipCode.grid(row=7, column=0, padx=10, pady=10)

        txtZipCode = StringVar()
        entZipCode = ttk.Entry(lblBasicInfo, width=40, textvariable=txtZipCode)
        entZipCode.grid(row=7, column=1, padx=10, pady=10)

        lblContract = Label(lblBasicInfo, text='Contract: ')
        lblContract.grid(row=8, column=0, padx=10, pady=10)

        intContract = IntVar()
        intContract.set(None)
        entYes = ttk.Radiobutton(lblBasicInfo,variable=intContract, text='Yes',value=1)
        entYes.grid(row=8, column=1, padx=10, pady=10,sticky=W)

        entNo = ttk.Radiobutton(lblBasicInfo,variable=intContract, text='No',value=0)
        entNo.grid(row=8, column=1, padx=10, pady=10)

        btnRegisterAuthor=ttk.Button(lblBasicInfo,text='Register',command=registerAuthor)
        btnRegisterAuthor.grid(row=9,column=1,sticky=NSEW,padx=5)

        btnDeleteAuthor=ttk.Button(lblBasicInfo,text='Delete',command=deleteAuthor)
        btnDeleteAuthor.grid(row=11,column=1,sticky=NSEW,padx=5)

        btnUpdateAuthor = ttk.Button(lblBasicInfo, text='Update', command=updateAuthor)
        btnUpdateAuthor.grid(row=10, column=1, sticky=NSEW, padx=5)


        btnReset = ttk.Button(lblBasicInfo, text='Reset',command=resetForm)
        btnReset.grid(row=9, column=2,sticky=NSEW,padx=5)

        btnBack=ttk.Button(lblBasicInfo,text='Back',command=backToMainForm)
        btnBack.grid(row=9,column=0,sticky=NSEW,padx=5)



        lblFrmAuthor=LabelFrame(authorCRUDForm,text='Author List')

        lblFrmAuthor.grid(row=0,column=1,padx=10,pady=10,ipadx=20, ipady=20,sticky=NSEW)

        columns = ['Index', 'au_id', 'au_lname', 'au_fname', 'phone', 'address', 'city', 'state', 'zip', 'contract']
        displayColumns = ['Index', 'au_lname', 'au_fname', 'phone', 'address', 'city', 'state', 'zip', 'contract']

        tvAuthorList=ttk.Treeview(lblFrmAuthor,columns=columns,selectmode='browse',
                                  show='headings',displaycolumns=displayColumns)


        tvAuthorList.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        tvAuthorList.bind('<<TreeviewSelect>>',onTreeSelect)

        tvAuthorList.column('#0',width=0)

        tvAuthorList.column('Index',width=20)
        tvAuthorList.heading('Index',text='#',anchor='n')

        tvAuthorList.column('au_lname',width=70)
        tvAuthorList.heading('au_lname',text='au_lname',anchor='n')

        tvAuthorList.column('au_fname',width=70)
        tvAuthorList.heading('au_fname',text='au_fname',anchor='n')

        tvAuthorList.column('phone',width=100)
        tvAuthorList.heading('phone',text='phone',anchor='n')

        tvAuthorList.column('address',width=120)
        tvAuthorList.heading('address',text='address',anchor='n')

        tvAuthorList.column('city',width=80)
        tvAuthorList.heading('city',text='city',anchor='n')

        tvAuthorList.column('state',width=40)
        tvAuthorList.heading('state',text='state',anchor='n')

        tvAuthorList.column('zip',width=50)
        tvAuthorList.heading('zip',text='zip',anchor='n')

        tvAuthorList.column('contract',width=70)
        tvAuthorList.heading('contract',text='contract',anchor='n')
        showList()
        authorCRUDForm.mainloop()