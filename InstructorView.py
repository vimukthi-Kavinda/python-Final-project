from tkinter import *
from Instructor import *
#defines the window for instructor
class InsViewGui:
    #when clicks the booking button then gets the name of intructor from txt field and create a instructor object
    def isInstInDB(self):
        ins=Instructor(self.txtName.get(),"","","","","")
        #call the addLessonBooking function by sending booking no from txt box
        ins.addLessonBooking(self.txtbking.get())







    def __init__(self):
        self.root=Tk()
        self.lblTitle=Label(self.root,text="Instructor")
        self.txtName=Entry(self.root,width=20)
        self.txtbking = Entry(self.root, width=20)
        self.lblNm=Label(self.root,text="Instructor Name : ")
        self.lblBking = Label(self.root, text="Input Booking code : ")
        self.btnVerify=Button(self.root,text="Booking for your students",command=self.isInstInDB)
        self.lblTitle.grid(column=1,row=0)
        self.lblNm.grid(column=0, row=1)
        self.lblBking.grid(column=0,row=2)
        self.txtbking.grid(column=2,row=2)
        self.txtName.grid(column=2,row=1)
        self.btnVerify.grid(column=1,row=3)
        self.root.mainloop()


