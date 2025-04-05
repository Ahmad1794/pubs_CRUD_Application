from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage

from tkcalendar import DateEntry

from UserInterfaceLayer.MainModule import MainForm
from BusinessLogicLayer.Title_BLL_Module import Title_BLL
from Model.TitleModel import TitleModelClass
from Model.TitleModel import TitleModelBClass

class TitleCRUD:
    def titleCRUD_FormLoad(self):


        def backToMainForm():
            titleCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            txttitle_idValue.set("")
            txtpub.set("")
            txtpubdate.set("")

        def registerTitle():
            titleBLLObject=Title_BLL()
            title=txttitle.get()
            type=txttype.get()
            pub=publisherDict[txtpub.get()]
            price=txtprice.get()
            advance=txtadvance.get()
            royalty=txtroyalty.get()
            ytd_sales=txtytd_sales.get()
            notes=txtnotes.get()
            pubdate=txtpubdate.get()
            titleObject=TitleModelClass(title=title,type=type,pub=pub,price=price,advance=advance,
                                        royalty=royalty,ytd_sales=ytd_sales,notes=notes,pubdate=pubdate)
            titleBLLObject.registerTitle(titleObject)
            showList()


        def onTreeSelect(event):
            resetForm()
            index=tvTitleList.selection()
            if index:
                selectedvalues=tvTitleList.item(index)['values']
                txttitle_idValue.set(selectedvalues[1])
                txttitle.set(selectedvalues[2])
                txttype.set(selectedvalues[3])
                txtpub.set(selectedvalues[4])
                txtprice.set(selectedvalues[5])
                txtadvance.set(selectedvalues[6])
                txtroyalty.set(selectedvalues[7])
                txtytd_sales.set(selectedvalues[8])
                txtnotes.set(selectedvalues[9])
                txtpubdate.set(selectedvalues[10])

        def deleteTitle():
            title_id=txttitle_idValue.get()
            if title_id:
                from BusinessLogicLayer.Title_BLL_Module import Title_BLL
                titleBLLObject=Title_BLL()
                titleBLLObject.deleteTitle(title_id)
            showList()


        def showList(*args):
            from BusinessLogicLayer.Title_BLL_Module import Title_BLL
            titleBLLObject=Title_BLL()
            rows = titleBLLObject.getTitleList()
            tvTitleList.delete(*tvTitleList.get_children())

            rowCount=0
            for row in rows:
                rowCount+=1
                values=[rowCount]
                for value in row:
                    if value==None:
                        values.append("")
                    else:
                        values.append(value)
                tvTitleList.insert("","end",values=values)

        def updateTitle():
            title_id=txttitle_idValue
            title=txttitle.get()
            type=txttype.get()
            pub=publisherDict[txtpub.get()]
            price=txtprice.get()
            advance=txtadvance.get()
            royalty=txtroyalty.get()
            ytd_sales=txtytd_sales.get()
            notes=txtnotes.get()
            pubdate=txtpubdate
            titleObject=TitleModelBClass(title_id=title_id,title=title,type=type,pub=pub,price=price,advance=advance,
                                        royalty=royalty,ytd_sales=ytd_sales,notes=notes,pubdate=pubdate)
            if title_id:
                from BusinessLogicLayer.Title_BLL_Module import Title_BLL
                titleBLLObject = Title_BLL()
                titleBLLObject.updateTitle(titleObject)

            showList()
            resetForm()

        publisherDict=dict()
        def getPubList():
            from BusinessLogicLayer.Title_BLL_Module import Title_BLL
            titleBLLObject = Title_BLL()
            publisherList =titleBLLObject.getPubList()

            if len(publisherList)>0:
                for publisher in publisherList:
                    if publisher[1] not in publisherDict:
                        publisherDict[publisher[1]]=publisher[0]
            return list(publisherDict.keys())





        titleCRUDForm = Tk()
        titleCRUDForm.title('Title CRUD Form')
        titleCRUDForm.geometry('1200x600')
        titleCRUDForm.iconbitmap('Images/title.ico')
        titleCRUDForm.resizable(0, 0)
        x = int(titleCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(titleCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        titleCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(titleCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lbltitle_id = Label(lblBasicInfo, text='Title ID: ')
        lbltitle_id.grid(row=0, column=0, padx=10, pady=10)

        txttitle_idValue = StringVar()
        lbltitle_idValue = Label(lblBasicInfo,  textvariable=txttitle_idValue)
        lbltitle_idValue.grid(row=0, column=1, padx=10, pady=10,sticky=W)

        lbltitle = Label(lblBasicInfo, text='Title Name: ')
        lbltitle.grid(row=1, column=0, padx=10, pady=10)

        txttitle = StringVar()
        enttitle = ttk.Entry(lblBasicInfo, width=40, textvariable=txttitle)
        enttitle.grid(row=1, column=1, padx=10, pady=10)

        lbltype = Label(lblBasicInfo, text='Type: ')
        lbltype.grid(row=2, column=0, padx=10, pady=10)

        txttype = StringVar()
        enttype = ttk.Entry(lblBasicInfo, width=40, textvariable=txttype)
        enttype.grid(row=2, column=1, padx=10, pady=10)

        lblpub = Label(lblBasicInfo, text='Publisher: ')
        lblpub.grid(row=3, column=0, padx=10, pady=10)

        txtpub = StringVar()
        cmbpub = ttk.Combobox(lblBasicInfo, width=40, state='readonly', values=getPubList(), textvariable=txtpub)
        cmbpub.grid(row=3, column=1, padx=10, pady=10)


        lblprice = Label(lblBasicInfo, text='Price: ')
        lblprice.grid(row=4, column=0, padx=10, pady=10)

        txtprice = StringVar()
        entprice = ttk.Entry(lblBasicInfo, width=40, textvariable=txtprice)
        entprice.grid(row=4, column=1, padx=10, pady=10)

        lbladvance = Label(lblBasicInfo, text='Advance: ')
        lbladvance.grid(row=5, column=0, padx=10, pady=10)

        txtadvance = StringVar()
        entadvance = ttk.Entry(lblBasicInfo, width=40, textvariable=txtadvance)
        entadvance.grid(row=5, column=1, padx=10, pady=10)


        lblroyalty = Label(lblBasicInfo, text='Royalty: ')
        lblroyalty.grid(row=6, column=0, padx=10, pady=10)

        txtroyalty = StringVar()
        entroyalty = ttk.Entry(lblBasicInfo, width=40, textvariable=txtroyalty)
        entroyalty.grid(row=6, column=1, padx=10, pady=10)


        lblytd_sales = Label(lblBasicInfo, text='Year to Date Sales: ')
        lblytd_sales.grid(row=7, column=0, padx=10, pady=10)

        txtytd_sales = StringVar()
        entytd_sales = ttk.Entry(lblBasicInfo, width=40, textvariable=txtytd_sales)
        entytd_sales.grid(row=7, column=1, padx=10, pady=10)

        lblnotes = Label(lblBasicInfo, text='Notes: ')
        lblnotes.grid(row=8, column=0, padx=10, pady=10)

        txtnotes = StringVar()
        entnotes = ttk.Entry(lblBasicInfo, width=40, textvariable=txtnotes)
        entnotes.grid(row=8, column=1, padx=10, pady=10)


        lblpubdate = Label(lblBasicInfo, text='Publish Date: ')
        lblpubdate.grid(row=9, column=0, padx=10, pady=10)

        txtpubdate = StringVar()
        entpubdate = DateEntry(lblBasicInfo, width=40, textvariable=txtpubdate)
        entpubdate.grid(row=9, column=1, padx=10, pady=10)


        btnRegisterTitle=ttk.Button(lblBasicInfo,text='Register',command=registerTitle)
        btnRegisterTitle.grid(row=10,column=1,sticky=NSEW,padx=5)

        btnDeleteTitle=ttk.Button(lblBasicInfo,text='Delete',command=deleteTitle)
        btnDeleteTitle.grid(row=12,column=1,sticky=NSEW,padx=5)

        btnUpdateTitle = ttk.Button(lblBasicInfo, text='Update', command=updateTitle)
        btnUpdateTitle.grid(row=11, column=1, sticky=NSEW, padx=5)


        btnReset = ttk.Button(lblBasicInfo, text='Reset',command=resetForm)
        btnReset.grid(row=10, column=2,sticky=NSEW,padx=5)

        btnBack=ttk.Button(lblBasicInfo,text='Back',command=backToMainForm)
        btnBack.grid(row=10,column=0,sticky=NSEW,padx=5)



        lblFrmTitle=LabelFrame(titleCRUDForm,text='Title List')

        lblFrmTitle.grid(row=0,column=1,padx=10,pady=10,ipadx=20, ipady=20,sticky=NSEW)

        columns = ['Index', 'title_id', 'title', 'type', 'pub', 'price', 'advance', 'royalty', 'ytd_sales', 'notes']
        displayColumns = ['Index', 'title', 'type', 'pub', 'price', 'advance', 'royalty', 'ytd_sales', 'notes']

        tvTitleList=ttk.Treeview(lblFrmTitle,columns=columns,selectmode='browse',
                                  show='headings',displaycolumns=displayColumns)


        tvTitleList.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        tvTitleList.bind('<<TreeviewSelect>>',onTreeSelect)

        tvTitleList.column('#0',width=0)

        tvTitleList.column('Index',width=20)
        tvTitleList.heading('Index',text='#',anchor='n')

        tvTitleList.column('title',width=70)
        tvTitleList.heading('title',text='title',anchor='n')

        tvTitleList.column('type',width=70)
        tvTitleList.heading('type',text='type',anchor='n')

        tvTitleList.column('pub',width=100)
        tvTitleList.heading('pub',text='pub',anchor='n')

        tvTitleList.column('price',width=120)
        tvTitleList.heading('price',text='price',anchor='n')

        tvTitleList.column('advance',width=80)
        tvTitleList.heading('advance',text='advance',anchor='n')

        tvTitleList.column('royalty',width=40)
        tvTitleList.heading('royalty',text='royalty',anchor='n')

        tvTitleList.column('ytd_sales',width=50)
        tvTitleList.heading('ytd_sales',text='ytd_sales',anchor='n')

        tvTitleList.column('notes',width=70)
        tvTitleList.heading('notes',text='notes',anchor='n')
        showList()
        titleCRUDForm.mainloop()