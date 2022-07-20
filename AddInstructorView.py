
from tkinter import *
from Admin import *
from Instructor import *

# form window to get details from user
class AddInstructorgui:
    # once add button is clicked this function is activated
    def addInsToDB(self):
        a=Admin()
        #gets values from entries and create a instructor object and sent that object to addInstructor function
        a.addInstructor(Instructor(self.txtnm.get(),self.txtgndr.get(),self.txtdnStyl.get(),self.txttpNo.get(),self.txthrrt.get(),self.txtAvailability.get()))

    def __init__(self):

        self.root=Tk()
        self.title=Label(self.root,text="Add Form")
        self.lblnm=Label(self.root,text="name : ")
        self.lblgndr=Label(self.root,text="gender : ")
        self.lbldnStyl=Label(self.root,text="dance style : ")
        self.lbltpNo=Label(self.root,text="telephone no : ")
        self.lblhrrt=Label(self.root,text="Hr rate : ")
        self.lblAvilability=Label(self.root,text="availability : ")

        self.txtnm=Entry(self.root,width=20)
        self.txtgndr = Entry(self.root, width=20)
        self.txtdnStyl = Entry(self.root, width=20)
        self.txttpNo = Entry(self.root, width=20)
        self.txthrrt = Entry(self.root, width=20)
        self.txtAvailability = Entry(self.root, width=20)

        self.btnAdd=Button(self.root,text="Add",command=self.addInsToDB)
        self.lblnm.grid(column=0,row=1)
        self.lblgndr.grid(column=0, row=2)
        self.lbldnStyl.grid(column=0, row=3)
        self.lbltpNo.grid(column=0, row=4)
        self.lblhrrt.grid(column=0, row=5)
        self.lblAvilability.grid(column=0, row=6)
        self.title.grid(column=1,row=0)

        self.txtnm.grid(column=2, row=1)
        self.txtgndr.grid(column=2, row=2)
        self.txtdnStyl.grid(column=2, row=3)
        self.txttpNo.grid(column=2, row=4)
        self.txthrrt.grid(column=2, row=5)
        self.txtAvailability.grid(column=2, row=6)
        self.btnAdd.grid(row=7,column=1)
        mainloop()








