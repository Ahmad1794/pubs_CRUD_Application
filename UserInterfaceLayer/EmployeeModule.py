from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import PhotoImage
from tkcalendar import DateEntry
from UserInterfaceLayer.MainModule import MainForm
from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
from Model.EmployeeModel import EmployeeModelClass
from Model.EmployeeModel import EmployeeModelBClass

class EmployeeCRUD:
    def employeeCRUD_FormLoad(self):


        def backToMainForm():
            employeeCRUDForm.destroy()
            mainFormObject = MainForm()
            mainFormObject.mainFormLoad()

        def resetForm():
            for widget in lblBasicInfo.winfo_children():
                if isinstance(widget, ttk.Entry):
                    widget.delete(0, END)
            txtemp_idValue.set("")
            txthire_date.set("")
            txtjob.set("")
            txtpub.set("")

        def registerEmployee():
            employeeBLLObject=Employee_BLL()
            fname=txtfname.get()
            minit=txtminit.get()
            lname=txtlname.get()
            job_id=jobDict[txtjob.get()]
            job_lvl=txtjob_lvl.get()
            pub_id=publisherDict[txtpub.get()]
            hire_date=txthire_date.get()
            employeeObject=EmployeeModelClass(fname=fname,minit=minit,lname=lname,
                                              job=job_id,job_lvl=job_lvl,pub=pub_id,hire_date=hire_date)
            employeeBLLObject.registerEmployee(employeeObject)
            showList()


        def onTreeSelect(event):
            resetForm()
            index=tvEmployeeList.selection()
            if index:
                selectedvalues=tvEmployeeList.item(index)['values']
                txtemp_idValue.set(selectedvalues[1])
                txtfname.set(selectedvalues[2])
                txtminit.set(selectedvalues[3])
                txtlname.set(selectedvalues[4])
                txtjob.set(selectedvalues[5])
                txtjob_lvl.set(selectedvalues[6])
                txtpub.set(selectedvalues[7])
                txthire_date.set(selectedvalues[8])

        def deleteEmployee():
            emp_id=txtemp_idValue.get()
            if emp_id:
                from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
                employeeBLLObject=Employee_BLL()
                employeeBLLObject.deleteEmployee(emp_id)
            showList()


        def showList(*args):
            from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
            employeeBLLObject=Employee_BLL()
            rows = employeeBLLObject.getEmployeeList()
            tvEmployeeList.delete(*tvEmployeeList.get_children())

            rowCount=0
            for row in rows:
                rowCount+=1
                values=[rowCount]
                for value in row:
                    if value==None:
                        values.append("")
                    else:
                        values.append(value)
                tvEmployeeList.insert("","end",values=values)

        def updateEmployee():
            emp_id=txtemp_idValue.get()
            fname = txtfname.get()
            minit = txtminit.get()
            lname = txtlname.get()
            job_id = jobDict[txtjob.get()]
            job_lvl = txtjob_lvl.get()
            pub_id = publisherDict[txtpub.get()]
            hire_date = txthire_date.get()
            employeeObject = EmployeeModelClass(emp_id=emp_id, fname=fname, minit=minit, lname=lname,
                                                job=job_id, job_lvl=job_lvl, pub=pub_id, hire_date=hire_date)
            if emp_id:
                from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
                employeeBLLObject = Employee_BLL()
                employeeBLLObject.updateEmployee(emp_id)

            showList()
            resetForm()


        jobDict=dict()
        def getJobList():
            from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
            employeeBLLObject = Employee_BLL()
            jobList =employeeBLLObject.getJobList()

            if len(jobList)>0:
                for job in jobList:
                    if job[1] not in jobDict:
                        jobDict[job[1]]=job[0]
            return list(jobDict.keys())

        publisherDict=dict()
        def getPubList():
            from BusinessLogicLayer.Employee_BLL_Module import Employee_BLL
            employeeBLLObject = Employee_BLL()
            publisherList =employeeBLLObject.getPubList()

            if len(publisherList)>0:
                for publisher in publisherList:
                    if publisher[1] not in publisherDict:
                        publisherDict[publisher[1]]=publisher[0]
            return list(publisherDict.keys())






        employeeCRUDForm = Tk()
        employeeCRUDForm.title('Employee CRUD Form')
        employeeCRUDForm.geometry('1200x600')
        employeeCRUDForm.iconbitmap('Images/employee.ico')
        employeeCRUDForm.resizable(0, 0)
        x = int(employeeCRUDForm.winfo_screenwidth() // 2 - 1200 // 2)
        y = int(employeeCRUDForm.winfo_screenheight() // 2 - 600 // 2)
        employeeCRUDForm.geometry('+{}+{}'.format(x, y))

        lblBasicInfo = LabelFrame(employeeCRUDForm, text='Basic Information')
        lblBasicInfo.grid(row=0, column=0, padx=10, pady=10, ipadx=20, ipady=20, sticky=NSEW)

        lblemp_id = Label(lblBasicInfo, text='Employee ID: ')
        lblemp_id.grid(row=0, column=0, padx=10, pady=10)

        txtemp_idValue = StringVar()
        lblemp_idValue = Label(lblBasicInfo, textvariable=txtemp_idValue)
        lblemp_idValue.grid(row=0, column=1, padx=10, pady=10,sticky=W)

        lblfname = Label(lblBasicInfo, text='First Name: ')
        lblfname.grid(row=1, column=0, padx=10, pady=10)

        txtfname = StringVar()
        entfname = ttk.Entry(lblBasicInfo, width=40, textvariable=txtfname)
        entfname.grid(row=1, column=1, padx=10, pady=10)

        lblminit = Label(lblBasicInfo, text='Middle Name Initial: ')
        lblminit.grid(row=2, column=0, padx=10, pady=10)

        txtminit = StringVar()
        entminit = ttk.Entry(lblBasicInfo, width=40, textvariable=txtminit)
        entminit.grid(row=2, column=1, padx=10, pady=10)

        lbllname = Label(lblBasicInfo, text='Last Name: ')
        lbllname.grid(row=3, column=0, padx=10, pady=10)

        txtlname = StringVar()
        entlname = ttk.Entry(lblBasicInfo, width=40, textvariable=txtlname)
        entlname.grid(row=3, column=1, padx=10, pady=10)

        lbljob = Label(lblBasicInfo, text='Job: ')
        lbljob.grid(row=4, column=0, padx=10, pady=10)

        txtjob = StringVar()
        cmbjob = ttk.Combobox(lblBasicInfo, width=40,state='readonly',values=getJobList(), textvariable=txtjob)
        cmbjob.grid(row=4, column=1, padx=10, pady=10)

        lbljob_lvl = Label(lblBasicInfo, text='Job Level: ')
        lbljob_lvl.grid(row=5, column=0, padx=10, pady=10)

        txtjob_lvl = StringVar()
        entjob_lvl = ttk.Entry(lblBasicInfo, width=40, textvariable=txtjob_lvl)
        entjob_lvl.grid(row=5, column=1, padx=10, pady=10)


        lblpub = Label(lblBasicInfo, text='Publisher: ')
        lblpub.grid(row=6, column=0, padx=10, pady=10)

        txtpub = StringVar()
        cmbpub = ttk.Combobox(lblBasicInfo, width=40, state='readonly', values=getPubList(), textvariable=txtpub)
        cmbpub.grid(row=6, column=1, padx=10, pady=10)


        lblhire_date = Label(lblBasicInfo, text='Hire Date: ')
        lblhire_date.grid(row=7, column=0, padx=10, pady=10)

        txthire_date = StringVar()
        enthire_date = DateEntry(lblBasicInfo, width=40, textvariable=txthire_date)
        enthire_date.grid(row=7, column=1, padx=10, pady=10)

        btnRegisterEmployee=ttk.Button(lblBasicInfo,text='Register',command=registerEmployee)
        btnRegisterEmployee.grid(row=9,column=1,sticky=NSEW,padx=5)

        btnDeleteEmployee=ttk.Button(lblBasicInfo,text='Delete',command=deleteEmployee)
        btnDeleteEmployee.grid(row=11,column=1,sticky=NSEW,padx=5)

        btnUpdateEmployee = ttk.Button(lblBasicInfo, text='Update', command=updateEmployee)
        btnUpdateEmployee.grid(row=10, column=1, sticky=NSEW, padx=5)


        btnReset = ttk.Button(lblBasicInfo, text='Reset',command=resetForm)
        btnReset.grid(row=9, column=2,sticky=NSEW,padx=5)

        btnBack=ttk.Button(lblBasicInfo,text='Back',command=backToMainForm)
        btnBack.grid(row=9,column=0,sticky=NSEW,padx=5)



        lblFrmEmployee=LabelFrame(employeeCRUDForm,text='Employee List')

        lblFrmEmployee.grid(row=0,column=1,padx=10,pady=10,ipadx=20, ipady=20,sticky=NSEW)

        columns = ['Index', 'emp_id', 'fname', 'minit', 'lname', 'job', 'job_lvl', 'pub', 'hire_date']
        displayColumns = ['Index', 'fname', 'minit', 'lname', 'job', 'job_lvl', 'pub', 'hire_date']

        tvEmployeeList=ttk.Treeview(lblFrmEmployee,columns=columns,selectmode='browse',
                                  show='headings',displaycolumns=displayColumns)


        tvEmployeeList.grid(row=0,column=0,padx=10,pady=10,sticky=NSEW)
        tvEmployeeList.bind('<<TreeviewSelect>>',onTreeSelect)

        tvEmployeeList.column('#0',width=0)

        tvEmployeeList.column('Index',width=20)
        tvEmployeeList.heading('Index',text='#',anchor='n')

        tvEmployeeList.column('fname',width=70)
        tvEmployeeList.heading('fname',text='fname',anchor='n')

        tvEmployeeList.column('minit',width=70)
        tvEmployeeList.heading('minit',text='minit',anchor='n')

        tvEmployeeList.column('lname',width=100)
        tvEmployeeList.heading('lname',text='lname',anchor='n')

        tvEmployeeList.column('job',width=120)
        tvEmployeeList.heading('job',text='job',anchor='n')

        tvEmployeeList.column('job_lvl',width=80)
        tvEmployeeList.heading('job_lvl',text='job_lvl',anchor='n')

        tvEmployeeList.column('pub',width=40)
        tvEmployeeList.heading('pub',text='pub',anchor='n')

        tvEmployeeList.column('hire_date',width=70)
        tvEmployeeList.heading('hire_date',text='hire_date',anchor='n')
        showList()
        employeeCRUDForm.mainloop()