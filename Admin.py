from Controller import *
from Instructor import *
from Student import *

class Admin:
    #sends an instructor to add to DB if he is already not in DB
    def addInstructor(self,ins):
        if(isinDB(ins.name)==False):
            addInstructorDB(ins)
        else:
            print("Name is already in database")

    def editInstructor(self,ins):
        # sends an instructor to edit DB record if he is already in DB
        if(isinDB(ins.name)==False):
            print("The instructor you entered, is not in the database")
        else:
            changeInstructorDB(ins)


    def deleteInstructor(self,insNme):
        # sends an instructor to delete DB record if he is already in DB
        if(isinDB(insNme)==False):
            print("Entered instructor is not registered")
        else:
            deleteInstructorDB(insNme)

    def viewInstructor(self):
        #call viewInstructors in controller file to get all instructor records from db
        viewInstructors()

    #send instructor name to set for suitable students
    def scheduleInstructor(self,insNme):
        setInstructor2Students(insNme)
    #send an student to add to db
    def registerStudent(self,stu):
        addStudentDB(stu)
