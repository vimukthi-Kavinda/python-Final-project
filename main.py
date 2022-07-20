from tkinter.font import Font
#main point
from InstructorView import *
from AdminView import *
from tkinter import *

#if user clicks instructor button then this function activtes
def loadInstructor():
    a=InsViewGui()#creates an object from InsViewGui class


#if user clicks Admin button then this function activtes
def loadAdmin():
    a=AdminViewGui()#creates an object from AdminViewGui class


#creates main window
root=Tk()


fontStyle = Font(family="Lucida Grande", size=20)
lblTitle=Label(root,text="Dance Feet",font=fontStyle)
lblLog=Label(root,text="Login as a : ")

btnIns=Button(root,text="Instructor",command=loadInstructor)
btnAdmn=Button(root,text="Admin",command=loadAdmin)
lblTitle.grid(column=1,row=0)
lblLog.grid(row=1,column=1)
btnIns.grid(row=2,column=0)
btnAdmn.grid(row=2,column=2)
mainloop()