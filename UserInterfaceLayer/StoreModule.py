from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage
from Model.StoreModel import StoreModelClass
from DataAccessLayer.Store_DAL_Module import Store_DAL
from BusinessLogicLayer.Store_BLL_Module import Store_BLL
from UserInterfaceLayer.MainModule import MainForm
from Model.StoreModel import StoreModelBClass


class StoreCRUD:
    def storeCRUD_FormLoad(self):

        # region Functions
        def backToMainForm():
            storeCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            txtstor_idValue.set("")

        def registerStore():
            storeBLLObject = Store_BLL()
            stor_name = txtstor_name.get()
            stor_address = txtstor_address.get()
            city = txtcity.get()
            state = txtstate.get()
            zip = txtzip.get()
            storeObject = StoreModelClass(stor_name=stor_name, stor_address=stor_address,
                                          city=city, state=state, zip=zip)
            storeBLLObject.registerStore(storeObject)
            showList()

        def onTreeSelect(event):
            resetForm()
            index = tvStoreList.selection()
            if index:
                selectedvalues = tvStoreList.item(index)['values']
                txtstor_idValue.set(selectedvalues[1])
                txtstor_name.set(selectedvalues[2])
                txtstor_address.set(selectedvalues[3])
                txtcity.set(selectedvalues[4])
                txtstate.set(selectedvalues[5])
                txtzip.set(selectedvalues[6])

        def deleteStore():
            stor_id = txtstor_idValue.get()
            if stor_id:
                from BusinessLogicLayer.Store_BLL_Module import Store_BLL
                storeBLLObject = Store_BLL()
                storeBLLObject.deleteStore(stor_id)
            showList()

        def showList(*args):
            from BusinessLogicLayer.Store_BLL_Module import Store_BLL
            storeBLLObject = Store_BLL()
            rows = storeBLLObject.getStoreList()
            tvStoreList.delete(*tvStoreList.get_children())

            rowCount = 0
            for row in rows:
                rowCount += 1
                values = [rowCount]
                for value in row:
                    if value == None:
                        values.append("")
                    else:
                        values.append(value)
                tvStoreList.insert("", "end", values=values)

        def updateStore():
            storeID = txtstor_idValue.get()
            storeName = txtstor_name.get()
            storeAddress = txtstor_address.get()
            city = txtcity.get()
            state = txtstate.get()
            zip = txtzip.get()
            storeObject = StoreModelBClass(storeName, storeAddress, city, state, zip
                                           , storeID)

            if storeID:
                from BusinessLogicLayer.Store_BLL_Module import Store_BLL
                storeBLLObject = Store_BLL()
                storeBLLObject.updateStore(storeObject)

            showList()
            resetForm()

        # endregion
        storeCRUDForm = Tk()
        storeCRUDForm.title('Store CRUD Form')
        storeCRUDForm.geometry('1200x600')
        storeCRUDForm.iconbitmap('Images/store.ico')
        storeCRUDForm.resizable(0, 0)
        x = int(storeCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(storeCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        storeCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(storeCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lblstor_id = Label(lblBasicInfo, text='StoreID: ')
        lblstor_id.grid(row=0, column=0, padx=10, pady=10)

        txtstor_idValue = StringVar()
        lblstor_idValue = Label(lblBasicInfo, textvariable=txtstor_idValue)
        lblstor_idValue.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        lblstor_name = Label(lblBasicInfo, text='Store Name: ')
        lblstor_name.grid(row=1, column=0, padx=10, pady=10)

        txtstor_name = StringVar()
        entstor_name = ttk.Entry(lblBasicInfo, width=40, textvariable=txtstor_name)
        entstor_name.grid(row=1, column=1, padx=10, pady=10)

        lblstor_address = Label(lblBasicInfo, text='Store Address: ')
        lblstor_address.grid(row=2, column=0, padx=10, pady=10)

        txtstor_address = StringVar()
        entstor_address = ttk.Entry(lblBasicInfo, width=40, textvariable=txtstor_address)
        entstor_address.grid(row=2, column=1, padx=10, pady=10)

        lblcity = Label(lblBasicInfo, text='City: ')
        lblcity.grid(row=3, column=0, padx=10, pady=10)

        txtcity = StringVar()
        entcity = ttk.Entry(lblBasicInfo, width=40, textvariable=txtcity)
        entcity.grid(row=3, column=1, padx=10, pady=10)

        lblstate = Label(lblBasicInfo, text='State: ')
        lblstate.grid(row=4, column=0, padx=10, pady=10)

        txtstate = StringVar()
        entstate = ttk.Entry(lblBasicInfo, width=40, textvariable=txtstate)
        entstate.grid(row=4, column=1, padx=10, pady=10)

        lblzip = Label(lblBasicInfo, text='Zip Code: ')
        lblzip.grid(row=6, column=0, padx=10, pady=10)

        txtzip = StringVar()
        entzip = ttk.Entry(lblBasicInfo, width=40, textvariable=txtzip)
        entzip.grid(row=6, column=1, padx=10, pady=10)

        btnRegisterStore = ttk.Button(lblBasicInfo, text='Register', command=registerStore)
        btnRegisterStore.grid(row=9, column=1, sticky=NSEW, padx=5)

        btnDeleteStore = ttk.Button(lblBasicInfo, text='Delete', command=deleteStore)
        btnDeleteStore.grid(row=11, column=1, sticky=NSEW, padx=5)

        btnUpdateStore = ttk.Button(lblBasicInfo, text='Update', command=updateStore)
        btnUpdateStore.grid(row=10, column=1, sticky=NSEW, padx=5)

        btnReset = ttk.Button(lblBasicInfo, text='Reset', command=resetForm)
        btnReset.grid(row=9, column=2, sticky=NSEW, padx=5)

        btnBack = ttk.Button(lblBasicInfo, text='Back', command=backToMainForm)
        btnBack.grid(row=9, column=0, sticky=NSEW, padx=5)

        lblFrmStore = LabelFrame(storeCRUDForm, text='Store List')

        lblFrmStore.grid(row=0, column=1, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        columns = ['Index', 'stor_id', 'stor_name', 'stor_address', 'city', 'state', 'zip']
        displayColumns = ['Index', 'stor_name', 'stor_address', 'city', 'state', 'zip']

        tvStoreList = ttk.Treeview(lblFrmStore, columns=columns, selectmode='browse',
                                   show='headings', displaycolumns=displayColumns)

        tvStoreList.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
        tvStoreList.bind('<<TreeviewSelect>>', onTreeSelect)

        tvStoreList.column('#0', width=0)

        tvStoreList.column('Index', width=20)
        tvStoreList.heading('Index', text='#', anchor='n')

        tvStoreList.column('stor_name', width=120)
        tvStoreList.heading('stor_name', text='stor_name', anchor='n')

        tvStoreList.column('stor_address', width=120)
        tvStoreList.heading('stor_address', text='stor_address', anchor='n')

        tvStoreList.column('city', width=70)
        tvStoreList.heading('city', text='city', anchor='n')

        tvStoreList.column('state', width=50)
        tvStoreList.heading('state', text='state', anchor='n')

        tvStoreList.column('zip', width=80)
        tvStoreList.heading('zip', text='zip', anchor='n')

        showList()
        storeCRUDForm.mainloop()
