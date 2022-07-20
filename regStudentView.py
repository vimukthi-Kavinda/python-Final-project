
from tkinter import *
from Admin import *
from Student import *
#creates the student registration form window
class RegStudentGui:
    #when user clicks add button this function is called
    def addStuToDB(self):
        a=Admin()
        #create a student object and set its values from Entry values then send that object to the Admins registerStudent function
        a.registerStudent(Student(self.txtStno.get(),self.txtFnm.get(),self.txtLnm.get(),self.txtEmail.get(),self.txtGndr.get(),self.txtDoB.get(),self.txttpNo.get(),self.txtAddr.get(),self.txtdnStyl.get(),self.txthrrt.get()))
    def __init__(self):

        self.root=Tk()
        self.title=Label(self.root,text="Student registration Form")
        self.lblStno = Label(self.root, text="Student No : ")
        self.lblFnm=Label(self.root,text="first Name : ")
        self.lblLnm=Label(self.root,text="Last Name : ")
        self.lbldnStyl=Label(self.root,text="dance style : ")
        self.lbltpNo=Label(self.root,text="telephone no : ")
        self.lblhrrt=Label(self.root,text="Max Hr rate : ")
        self.lblEmail=Label(self.root,text="Email : ")
        self.lblGndr = Label(self.root, text="Gender : ")
        self.lblDoB = Label(self.root, text="DoB : ")
        self.lblAddr = Label(self.root, text="Address : ")

        self.txtStno=Entry(self.root,width=20)
        self.txtFnm = Entry(self.root, width=20)
        self.txtLnm = Entry(self.root, width=20)
        self.txtdnStyl = Entry(self.root, width=20)
        self.txttpNo = Entry(self.root, width=20)
        self.txthrrt = Entry(self.root, width=20)
        self.txtEmail = Entry(self.root, width=20)
        self.txtGndr = Entry(self.root, width=20)
        self.txtDoB = Entry(self.root, width=20)
        self.txtAddr = Entry(self.root, width=20)

        self.btnAdd=Button(self.root,text="Add",command=self.addStuToDB)
        self.lblStno.grid(column=0,row=1)
        self.lblFnm.grid(column=0, row=2)
        self.lblLnm.grid(column=0, row=3)
        self.lbldnStyl.grid(column=0, row=4)
        self.lbltpNo.grid(column=0, row=5)
        self.lblhrrt.grid(column=0, row=6)
        self.title.grid(column=1,row=0)
        self.lblEmail.grid(column=0, row=7)
        self.lblGndr.grid(column=0, row=8)
        self.lblDoB.grid(column=0, row=9)
        self.lblAddr.grid(column=0, row=10)

        self.txtStno.grid(column=2, row=1)
        self.txtFnm.grid(column=2, row=2)
        self.txtLnm.grid(column=2, row=3)
        self.txtdnStyl.grid(column=2, row=4)
        self.txttpNo.grid(column=2, row=5)
        self.txthrrt.grid(column=2, row=6)
        self.txtEmail.grid(column=2, row=7)
        self.txtGndr.grid(column=2, row=8)
        self.txtDoB.grid(column=2, row=9)
        self.txtAddr.grid(column=2, row=10)
        self.btnAdd.grid(row=12,column=1)
        mainloop()








