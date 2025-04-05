from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage
from UserInterfaceLayer.MainModule import MainForm
from BusinessLogicLayer.Publisher_BLL_Module import Publisher_BLL
from DataAccessLayer.Publisher_DAL_Module import Publisher_DAL
from Model.PublisherModel import PublisherModelClass
from Model.PublisherModel import PublisherModelBClass

class PublisherCRUD:
    def publisherCRUD_FormLoad(self):

        # region Functions
        def backToMainForm():
            publisherCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            txtpub_idValue.set("")

        def registerPublisher():
            publisherBLLObject = Publisher_BLL()
            pub_name = txtpub_name.get()
            city = txtcity.get()
            state = txtstate.get()
            country = txtcountry.get()
            publisherObject = PublisherModelClass(pub_name=pub_name,
                                          city=city, state=state, country=country)
            publisherBLLObject.registerPublisher(publisherObject)
            showList()

        def onTreeSelect(event):
            resetForm()
            index = tvPublisherList.selection()
            if index:
                selectedvalues = tvPublisherList.item(index)['values']
                txtpub_idValue.set(selectedvalues[1])
                txtpub_name.set(selectedvalues[2])
                txtcity.set(selectedvalues[3])
                txtstate.set(selectedvalues[4])
                txtcountry.set(selectedvalues[5])

        def deletePublisher():
            pub_id = txtpub_idValue.get()
            if pub_id:
                from BusinessLogicLayer.Publisher_BLL_Module import Publisher_BLL
                publisherBLLObject = Publisher_BLL()
                publisherBLLObject.deletePublisher(pub_id)
            showList()

        def showList(*args):
            from BusinessLogicLayer.Publisher_BLL_Module import Publisher_BLL
            publisherBLLObject = Publisher_BLL()
            rows = publisherBLLObject.getPublisherList()
            tvPublisherList.delete(*tvPublisherList.get_children())

            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        values.append(value)
                tvPublisherList.insert("", "end", values=values)

        def updatePublisher():
            pub_id = txtpub_idValue.get()
            pub_name = txtpub_name.get()
            city = txtcity.get()
            state = txtstate.get()
            country = txtcountry.get()
            publisherObject = PublisherModelBClass(pub_name, city, state, country
                                           , pub_id)

            if pub_id:
                from BusinessLogicLayer.Publisher_BLL_Module import Publisher_BLL
                publisherBLLObject = Publisher_BLL()
                publisherBLLObject.updatePublisher(publisherObject)

            showList()
            resetForm()

        # endregion
        publisherCRUDForm = Tk()
        publisherCRUDForm.title('Publisher CRUD Form')
        publisherCRUDForm.geometry('1200x600')
        publisherCRUDForm.iconbitmap('Images/publisher.ico')
        publisherCRUDForm.resizable(0, 0)
        x = int(publisherCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(publisherCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        publisherCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(publisherCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lblpub_id = Label(lblBasicInfo, text='PublisherID: ')
        lblpub_id.grid(row=0, column=0, padx=10, pady=10)

        txtpub_idValue = StringVar()
        lblpub_idValue = Label(lblBasicInfo, textvariable=txtpub_idValue)
        lblpub_idValue.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        lblpub_name = Label(lblBasicInfo, text='Publisher Name: ')
        lblpub_name.grid(row=1, column=0, padx=10, pady=10)

        txtpub_name = StringVar()
        entpub_name = ttk.Entry(lblBasicInfo, width=40, textvariable=txtpub_name)
        entpub_name.grid(row=1, column=1, padx=10, pady=10)

        lblcity = Label(lblBasicInfo, text='City: ')
        lblcity.grid(row=2, column=0, padx=10, pady=10)

        txtcity = StringVar()
        entcity = ttk.Entry(lblBasicInfo, width=40, textvariable=txtcity)
        entcity.grid(row=2, column=1, padx=10, pady=10)

        lblstate = Label(lblBasicInfo, text='State: ')
        lblstate.grid(row=3, column=0, padx=10, pady=10)

        txtstate = StringVar()
        entstate = ttk.Entry(lblBasicInfo, width=40, textvariable=txtstate)
        entstate.grid(row=3, column=1, padx=10, pady=10)

        lblcountry = Label(lblBasicInfo, text='Country: ')
        lblcountry.grid(row=4, column=0, padx=10, pady=10)

        txtcountry = StringVar()
        entcountry = ttk.Entry(lblBasicInfo, width=40, textvariable=txtcountry)
        entcountry.grid(row=4, column=1, padx=10, pady=10)

        btnRegisterPublisher = ttk.Button(lblBasicInfo, text='Register', command=registerPublisher)
        btnRegisterPublisher.grid(row=5, column=1, sticky=NSEW, padx=5)

        btnDeletePublisher = ttk.Button(lblBasicInfo, text='Delete', command=deletePublisher)
        btnDeletePublisher.grid(row=7, column=1, sticky=NSEW, padx=5)

        btnUpdatePublisher = ttk.Button(lblBasicInfo, text='Update', command=updatePublisher)
        btnUpdatePublisher.grid(row=6, column=1, sticky=NSEW, padx=5)

        btnReset = ttk.Button(lblBasicInfo, text='Reset', command=resetForm)
        btnReset.grid(row=5, column=2, sticky=NSEW, padx=5)

        btnBack = ttk.Button(lblBasicInfo, text='Back', command=backToMainForm)
        btnBack.grid(row=5, column=0, sticky=NSEW, padx=5)

        lblFrmPublisher = LabelFrame(publisherCRUDForm, text='Publisher List')

        lblFrmPublisher.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        columns = ['Index', 'pub_id', 'pub_name', 'city', 'state', 'country']
        displayColumns = ['Index','pub_name', 'city', 'state', 'country']

        tvPublisherList = ttk.Treeview(lblFrmPublisher, columns=columns, selectmode='browse',
                                   show='headings', displaycolumns=displayColumns)

        tvPublisherList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
        tvPublisherList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvPublisherList.column('#0', width=0)

        tvPublisherList.column('Index', width=20)
        tvPublisherList.heading('Index', text='#', anchor='n')

        tvPublisherList.column('pub_name', width=120)
        tvPublisherList.heading('pub_name', text='pub_name', anchor='n')

        tvPublisherList.column('city', width=120)
        tvPublisherList.heading('city', text='city', anchor='n')

        tvPublisherList.column('state', width=70)
        tvPublisherList.heading('state', text='state', anchor='n')

        tvPublisherList.column('country', width=50)
        tvPublisherList.heading('country', text='country', anchor='n')


        showList()
        publisherCRUDForm.mainloop()
