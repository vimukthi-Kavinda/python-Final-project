#creates student objects
class Student:
    def __init__(self,stid,fn,sn,email,gender,doB,tpNo,address,danceStyle,maxHrRate):
        self.stId=stid;
        self.firstName=fn
        self.surName=sn
        self.email=email
        self.gender=gender
        self.DoB=doB
        self.tpNo=tpNo
        self.address=address
        self.danceStyle=danceStyle
        self.maxHrRate=maxHrRate
