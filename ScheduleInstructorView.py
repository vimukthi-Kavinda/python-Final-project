from tkinter import *



from tkinter import *
from Admin import *
#creates form to schedule an instructor for suitable students
class ScheduleInstructorgui:
    #calles when clicked on Schedule him button
    def ScheduleIns(self):
        a=Admin()
        #get value from Entry and send that value to the scheduleInstructor function
        a.scheduleInstructor(self.txtNm.get())


    def __init__(self):
        self.root=Tk()
        self.lblTitl=Label(self.root,text="Schedule for relevant Student")
        self.lblTitl.grid(row=0,column=0)

        self.lblNm=Label(self.root,text="Input Instructor Name : ")
        self.lblNm.grid(column=0,row=1)

        self.txtNm=Entry(self.root,width=20)
        self.txtNm.grid(row=1,column=1)

        self.btnSchedule=Button(self.root,text="Schedule him",command=self.ScheduleIns)
        self.btnSchedule.grid(column=0,row=2)

        mainloop()


