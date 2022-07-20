from tkinter import *
from Admin import *
# form window to get details from user
class DeleteInstructorgui:
    ## once delete button is clicked this function is activated
    def deleteIns(self):
        a=Admin()
        #get value from Entry and send it to the function deleteInstructor
        a.deleteInstructor(self.txtNm.get())

    def __init__(self):
        self.root=Tk()
        self.lblTitl=Label(self.root,text="Delete")
        self.lblTitl.grid(row=0,column=0)

        self.lblNm=Label(self.root,text="Input Name : ")
        self.lblNm.grid(column=0,row=1)

        self.txtNm=Entry(self.root,width=20)
        self.txtNm.grid(row=1,column=1)

        self.btnDelete=Button(self.root,text="Delete",command=self.deleteIns)
        self.btnDelete.grid(column=0,row=2)

        mainloop()


