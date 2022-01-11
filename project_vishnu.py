class Student :
    MIN_PASSING_MARKS = 40

    def __init__(self, name, srn, semester, marks):
        self.name = name
        self.srn = srn
        self.semester = semester
        self.marks = marks

    def __str__(self):
        tmp = {'name' : self.name, 'srn' : self.srn, 'semester' : self.semester, 'marks' : self.marks }
        return str(tmp)

    def getAverage(self):
        temp = 0
        counter = 0
        for sub in self.marks.keys():
            counter += 1
            temp += self.marks[sub]
        return (temp/counter)

    def allPassed(self):
        for sub in self.marks.keys():
            if self.marks[sub] < self.MIN_PASSING_MARKS:
                return False
        return True

studentList = []

def addStudent(name, srn, semester, marks):
    student = Student(name, srn, semester, marks)
    studentList.append(student)

def deleteStudent(srn):
    for temp in studentList:
        if temp.srn == srn:
            studentList.remove(temp)

def listStudentsAboveAverage(average):
    tempList = []
    for temp in studentList:
        if temp.getAverage() > average:
            tempList.append(temp)
    return tempList

def listStudentsAllPassed():
    tempList = []
    for temp in studentList:
        if temp.allPassed() == True:
            tempList.append(temp)
    return tempList

def listStudentsFailed():
    tempList = []
    for temp in studentList:
        if temp.allPassed() == False:
            tempList.append(temp)
    return tempList

def searchStudent(srn):
    for temp in studentList:
        if temp.srn == srn:
            return temp
    return None

def printStudentList(studList):
    for temp in studList:
        print(str(temp))
    print('\n---------------------------\n')

data = [
    { 'name' : 'vishnu', 'semester' : 1, 'srn' : '12022', 'marks' : {'physics' : 95, 'math' : 98, 'mechanical' : 94, 'electrical' : 99, 'computers' : 99}},
    { 'name' : 'vivek ', 'semester' : 1, 'srn' : '12021', 'marks' : {'physics' : 85, 'math' : 78, 'mechanical' : 84, 'electrical' : 79, 'computers' : 85}},
    { 'name' : 'mohith', 'semester' : 1, 'srn' : '12023', 'marks' : {'physics' : 15, 'math' : 68, 'mechanical' : 94, 'electrical' : 59, 'computers' : 49}}]

addStudent(data[0]['name'],data[0]['srn'],data[0]['semester'],data[0]['marks'])
addStudent(data[1]['name'],data[1]['srn'],data[1]['semester'],data[1]['marks'])
addStudent(data[2]['name'],data[2]['srn'],data[2]['semester'],data[2]['marks'])
printStudentList(studentList)

deleteStudent('12021')
printStudentList(studentList)

addStudent('manohar', '12025', 1, {'physics' : 15, 'math' : 28, 'mechanical' : 34, 'electrical' : 9, 'computers' : 19})
printStudentList(studentList)

temp = listStudentsAllPassed()
printStudentList(temp)

temp = listStudentsFailed()
printStudentList(temp)

temp = searchStudent('12022')
print(str(temp))
print('\n---------------------\n')

temp = listStudentsAboveAverage(80)
printStudentList(temp)