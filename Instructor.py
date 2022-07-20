from Student import *
from Controller import *
#creates Instrucor object
class Instructor:
    def __init__(self,name,gender,styles,tp,rte,availability):
        self.name=name
        self.gender=gender
        self.styles=styles
        self.tpNo=tp
        self.hrRate=rte
        self.availability=availability





    def addLessonBooking(self,bookingNo):
        #checks whether relevant instructor is in the DB
        if(isinDB(self.name)):
            #if he is in, then calles makeAbooking in controller file
            makeAbooking(self.name,bookingNo)
        else:
            print("you are not registered..")




