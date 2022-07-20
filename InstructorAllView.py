from tkinter import *
from Admin import *
#creates instructor view window
class ViewInstructorgui:
    #once View All is clicked this function activated
    def viewIns(self):
        a=Admin()
        a.viewInstructor()


    def __init__(self):
        self.root=Tk()
        self.btnView=Button(self.root,text="View All",command=self.viewIns)
        self.lblTitle=Label(self.root,text="View All")
        
        self.lblTitle.grid(column=0,row=0)
        self.btnView.grid(column=1,row=1)

        mainloop()

