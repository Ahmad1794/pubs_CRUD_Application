from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage
from tkcalendar import DateEntry
from UserInterfaceLayer.MainModule import MainForm
from DataAccessLayer.Sale_DAL_Module import Sale_DAL
from BusinessLogicLayer.Sale_BLL_Module import Sale_BLL
from Model.SaleModel import SaleModelClass

class SaleCRUD:
    def saleCRUD_FormLoad(self):


        def backToMainForm():
            saleCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            txtstor_id.set("")
            txttitle_id.set("")
            txtord_date.set("")

        def registerSale():
            saleBLLObject=Sale_BLL()
            stor_id=storeDict[txtstor_id.get()]
            ord_num=txtord_num.get()
            ord_date=txtord_date.get()
            qty=txtqty.get()
            payterms=txtpayterms.get()
            title_id=titleDict[txttitle_id.get()]
            saleObject=SaleModelClass(stor_id=stor_id,ord_num=ord_num,ord_date=ord_date,qty=qty,payterms=payterms,title_id=title_id)
            saleBLLObject.registerSale(saleObject)
            showList()


        def onTreeSelect(event):
            resetForm()
            index=tvSaleList.selection()
            if index:
                selectedvalues=tvSaleList.item(index)['values']
                txtstor_id.set(selectedvalues[1])
                txtord_num.set(selectedvalues[2])
                txtord_date.set(selectedvalues[3])
                txtqty.set(selectedvalues[4])
                txtpayterms.set(selectedvalues[5])
                txttitle_id.set(selectedvalues[6])

        def deleteSale():
            stor_id=txtstor_id.get()
            ord_num=txtord_num.get()
            ord_date=txtord_date.get()
            qty=txtqty.get()
            payterms=txtpayterms.get()
            title_id=txttitle_id.get()
            if stor_id and ord_num and ord_date and qty and payterms and title_id:
                from BusinessLogicLayer.Sale_BLL_Module import Sale_BLL
                saleBLLObject=Sale_BLL()
                saleBLLObject.deleteSale(stor_id,ord_num,ord_date,qty,payterms,title_id)
            showList()


        def showList(*args):
            from BusinessLogicLayer.Sale_BLL_Module import Sale_BLL
            saleBLLObject=Sale_BLL()
            rows = saleBLLObject.getSaleList()
            tvSaleList.delete(*tvSaleList.get_children())

            rowCount=0
            for row in rows:
                rowCount+=1
                values=[rowCount]
                for value in row:
                    if value==None:
                        values.append("")
                    else:
                        values.append(value)
                tvSaleList.insert("","end",values=values)

        def updateSale():

            old_stor_id=storeDict[txtstor_id]
            old_ord_num=txtord_num
            old_ord_date=txtord_date
            old_qty=txtqty
            old_payterms=txtpayterms
            old_title_id=titleDict[txttitle_id]
            new_stor_id=storeDict[txtstor_id.get()]
            new_ord_num=txtord_num.get()
            new_ord_date=txtord_date.get()
            new_qty=txtqty.get()
            new_payterms=txtpayterms.get()
            new_title_id=titleDict[txttitle_id.get()]

            sale_BLLObject=(new_stor_id,old_stor_id,new_ord_num,old_ord_num,new_ord_date,old_ord_date,
                   new_qty,old_qty,new_payterms,old_payterms,new_title_id,old_title_id)
            sale_BLLObject.updateSale()

            showList()
            resetForm()
        
        
        storeDict=dict()
        def getStoreList():
            from BusinessLogicLayer.Sale_BLL_Module import Sale_BLL
            saleBLLObject = Sale_BLL()
            storeList =saleBLLObject.getStoreList()

            if len(storeList)>0:
                for store in storeList:
                    if store[1] not in storeDict:
                        storeDict[store[1]]=store[0]
            return list(storeDict.keys())
        
        
        
        titleDict=dict()
        def getTitleList():
            from BusinessLogicLayer.Sale_BLL_Module import Sale_BLL
            saleBLLObject = Sale_BLL()
            titleList =saleBLLObject.getTitleList()

            if len(titleList)>0:
                for title in titleList:
                    if title[1] not in titleDict:
                        titleDict[title[1]]=title[0]
            return list(titleDict.keys())





        saleCRUDForm = Tk()
        saleCRUDForm.title('Sale CRUD Form')
        saleCRUDForm.geometry('1200x600')
        saleCRUDForm.iconbitmap('Images/sale.ico')
        saleCRUDForm.resizable(0, 0)
        x = int(saleCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(saleCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        saleCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(saleCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lblstor_id = Label(lblBasicInfo, text='Store ID: ')
        lblstor_id.grid(row=0, column=0, padx=10, pady=10)

        txtstor_id = StringVar()
        cmbstor_id = ttk.Combobox(lblBasicInfo, width=40, state='readonly', values=getStoreList(), textvariable=txtstor_id)
        cmbstor_id.grid(row=0, column=1, padx=10, pady=10)

        lblord_num = Label(lblBasicInfo, text='Order Number: ')
        lblord_num.grid(row=1, column=0, padx=10, pady=10)

        txtord_num = StringVar()
        entord_num = ttk.Entry(lblBasicInfo, width=40, textvariable=txtord_num)
        entord_num.grid(row=1, column=1, padx=10, pady=10)

        lblord_date = Label(lblBasicInfo, text='Order Date: ')
        lblord_date.grid(row=2, column=0, padx=10, pady=10)

        txtord_date = StringVar()
        entord_date = DateEntry(lblBasicInfo, width=40, textvariable=txtord_date)
        entord_date.grid(row=2, column=1, padx=10, pady=10)

        lblqty = Label(lblBasicInfo, text='Quantity: ')
        lblqty.grid(row=3, column=0, padx=10, pady=10)

        txtqty = StringVar()
        entqty = ttk.Entry(lblBasicInfo, width=40, textvariable=txtqty)
        entqty.grid(row=3, column=1, padx=10, pady=10)

        lblpayterms = Label(lblBasicInfo, text='Pay Terms: ')
        lblpayterms.grid(row=4, column=0, padx=10, pady=10)

        txtpayterms = StringVar()
        entpayterms = ttk.Entry(lblBasicInfo, width=40, textvariable=txtpayterms)
        entpayterms.grid(row=4, column=1, padx=10, pady=10)

        lbltitle_id = Label(lblBasicInfo, text='Title: ')
        lbltitle_id.grid(row=5, column=0, padx=10, pady=10)

        txttitle_id = StringVar()
        cmbtitle_id = ttk.Combobox(lblBasicInfo, width=40, state='readonly', values=getTitleList(), textvariable=txttitle_id)
        cmbtitle_id.grid(row=5, column=1, padx=10, pady=10)

        btnRegisterSale=ttk.Button(lblBasicInfo,text='Register',command=registerSale)
        btnRegisterSale.grid(row=6,column=1,sticky=NSEW,padx=5)

        btnDeleteSale=ttk.Button(lblBasicInfo,text='Delete',command=deleteSale)
        btnDeleteSale.grid(row=7,column=1,sticky=NSEW,padx=5)

        # btnUpdateSale = ttk.Button(lblUpdate, text='Update', command=updateSale)
        # btnUpdateSale.grid(row=3, column=1, sticky=NSEW, padx=5)

        btnReset = ttk.Button(lblBasicInfo, text='Reset',command=resetForm)
        btnReset.grid(row=6, column=2,sticky=NSEW,padx=5)

        btnBack=ttk.Button(lblBasicInfo,text='Back',command=backToMainForm)
        btnBack.grid(row=6,column=0,sticky=NSEW,padx=5)




        lblFrmSale=LabelFrame(saleCRUDForm,text='Sale List')
        lblFrmSale.grid(row=0,column=1,padx=10,pady=10,ipadx=20, ipady=20,sticky=NSEW)

        columns = ['Index', 'stor_id','ord_num','ord_date','qty','payterms','title_id']
        displayColumns = ['Index', 'stor_id','ord_num','ord_date','qty','payterms','title_id']

        tvSaleList=ttk.Treeview(lblFrmSale,columns=columns,selectmode='browse',
                                  show='headings',displaycolumns=displayColumns)


        tvSaleList.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        tvSaleList.bind('<<TreeviewSelect>>',onTreeSelect)

        tvSaleList.column('#0',width=0)

        tvSaleList.column('Index',width=20)
        tvSaleList.heading('Index',text='#',anchor='n')

        tvSaleList.column('stor_id',width=70)
        tvSaleList.heading('stor_id',text='stor_id',anchor='n')

        tvSaleList.column('ord_num',width=70)
        tvSaleList.heading('ord_num',text='ord_num',anchor='n')

        tvSaleList.column('ord_date',width=100)
        tvSaleList.heading('ord_date',text='ord_date',anchor='n')

        tvSaleList.column('qty',width=120)
        tvSaleList.heading('qty',text='qty',anchor='n')

        tvSaleList.column('payterms',width=80)
        tvSaleList.heading('payterms',text='payterms',anchor='n')

        tvSaleList.column('title_id',width=40)
        tvSaleList.heading('title_id',text='title_id',anchor='n')


        showList()
        saleCRUDForm.mainloop()