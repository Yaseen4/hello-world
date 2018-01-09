class Student():
    def __init__(self,lastName,surName,studentNumber,couRse):

        self.lastname = lastName
        self.surname = surName
        self.studentnumber = studentNumber
        self.course = couRse

    def getLastname(self):
        return self.lastname

    def getSurname(self):
        return self.surname

    def getStudentID(self):
        return self.studentnumber

    def getCourse(self):
        return self.course


    def setLastname(self,newLastname):
        self.lastname = newLastname

    def setSurname(self,newSurname):
        self.surname = newSurname


    def setStudentID(self,newStudentID):
        self.studentnumber = newStudentID

    def setCourse(self,newCourse):
        self.course = newCourse

    def printAll(self):
        print("The lastname is: " + self.lastname)
        print("The surname is: " + self.surname)
        print("The studentID is: " + self.studentnumber)
        print("The course is: " + self.course)
