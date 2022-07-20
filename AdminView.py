from tkinter import *
from AddInstructorView import *
from DeleteInstructorView import *
from EditInstructorView import *
from ScheduleInstructorView import *
from regStudentView import *
from InstructorAllView import *
#creates admin view window
class AdminViewGui:
    # calls if click Add a Instructor button
    def addIns(self):
        a = AddInstructorgui()

    # calls if click Delete a Instructor button
    def delIns(self):
        a = DeleteInstructorgui()

    # calls if click Edit a Instructor button
    def editIns(self):
        a = EditInstructorgui()

    # calls if click View all Instructors button
    def vwIns(self):
        a = ViewInstructorgui()

    # calls if click Schedule Instructor button
    def sheduleIns(self):
        a = ScheduleInstructorgui()

    # calls if click Student registration button
    def regStu(self):
        a = RegStudentGui()


    def __init__(self):
        self.root=Tk()
        self.btnAddIns=Button(self.root,text="Add a Instructor",command=self.addIns)
        self.btnDelIns = Button(self.root, text="Delete a Instructor", command=self.delIns)
        self.btnEdtIns = Button(self.root, text="Edit a Instructor", command=self.editIns)
        self.btnAllViw = Button(self.root, text="View all Instructors", command=self.vwIns)
        self.btnRegStu = Button(self.root, text="Student registration", command=self.regStu)
        self.btnScheduleIns = Button(self.root, text="Schedule Instructor", command=self.sheduleIns)

        self.btnAddIns.grid(column=0,row=0)
        self.btnDelIns.grid(column=0, row=1)
        self.btnEdtIns.grid(column=0, row=2)
        self.btnAllViw.grid(column=0, row=3)
        self.btnScheduleIns.grid(column=0, row=4)
        self.btnRegStu.grid(column=0, row=5)

        self.root.mainloop()