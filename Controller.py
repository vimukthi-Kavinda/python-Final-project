import sqlite3
from tkinter import *
#creates conection with projectDB.db file
con=sqlite3.connect("projectDB.db")


#get an instructor object as parameter and executes the sql with its attributes and add to the DB
def addInstructorDB(instructor):
    query="insert into instructor values(?,?,?,?,?,?)"
    cursor=con.cursor()
    ls=(instructor.name,instructor.gender,instructor.styles,instructor.tpNo,instructor.hrRate,instructor.availability)
    cursor.execute(query,ls)
    con.commit()
    print("done")

#get an student object as parameter and executes the sql with its attributes and add to the DB
def addStudentDB(student):
    query = "insert into student values(?,?,?,?,?,?,?,?,?,?,?)"
    cursor = con.cursor()
    ls = (student.stId,student.firstName, student.surName, student.email, student.gender, student.DoB,student.tpNo,student.address,student.danceStyle,student.maxHrRate,"")
    cursor.execute(query, ls)
    con.commit()
    print("done")

#get an instructor object as parameter and executes the sql with its attributes and UPDATE record the DB
def changeInstructorDB(instructor):
    query = "update instructor set gender=?,style=?,tpno=?,hrrate=?,availability=? where name=?"
    cursor = con.cursor()
    ls = (instructor.gender, instructor.styles, instructor.tpNo, instructor.hrRate,instructor.availability,instructor.name)
    cursor.execute(query, ls)
    con.commit()
    print("done")
#get an instructor name as parameter and executes the sql with its attributes and remove the record from the DB
def deleteInstructorDB(instructor):
    query = "delete from instructor where name=?"
    cursor = con.cursor()
    ls = (instructor,)
    cursor.execute(query, ls)
    con.commit()
    print("done")
#get all records in instructor table and creates the all instructor view
def viewInstructors():
    query = "select * from instructor"
    cursor = con.cursor()

    cursor.execute(query)
    rows=cursor.fetchall()
    root=Tk()
    rowCount=len(rows)
    colCount=len(rows[0])
    for i in range(rowCount):
        for j in range(colCount):
            enty=Label(root,width=20)
            enty.grid(row=i, column=j)
            enty['text'] = rows[i][j]


    print("done")

def setInstructor2Students(nme):#get student ids of students and set instructor to them

    query1="select stuid,dancestyle,maxhrrate from student"
    cursor = con.cursor()

    cursor.execute(query1)
    stuRows = cursor.fetchall()
    query2 = "select style,hrrate from instructor where name='"+nme+"'"
    cursor = con.cursor()

    cursor.execute(query2)
    instructor = cursor.fetchall() #assume that we cannot have multiple instructor with same name
    #get students for an instructor
    setStudents=list()
    if(len(instructor)==0):
        print("No such instructor in db")
    else:
        for student in stuRows:
            #check instructors dancing style equals to student dancing style and students hr rate >= instructor hr rate
            if student[1]==instructor[0][0] and student[2]>=instructor[0][1]:
                setStudents.append(student[0])

        for stID in setStudents:

            query3="update student set insname=? where stuid=?"
            cursor = con.cursor()
            ls = (nme,stID)
            cursor.execute(query3, ls)
            con.commit()
            print("done")




def isinDB(insNm):
    query = "select * from instructor where name='"+insNm+"'"
    cursor = con.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()
    if(len(rows)==0):
        return False
    return rows


def makeAbooking(insNme,bookingNo):
    query="select stuid from student where insname='"+insNme+"'"
    cursor = con.cursor()

    cursor.execute(query)
    stuRows = cursor.fetchall()
    for stNo in stuRows:
        query1 = "insert into booking values(?,?,?)"
        cursor = con.cursor()
        stNo=stNo[0]
        ls = (stNo,insNme,bookingNo)
        cursor.execute(query1, ls)
        con.commit()
    print("done")



