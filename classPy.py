import platform


class Info:

    def __init__(self , name , age , isMale , phoneNumber):
        self.name = name
        self.age = age
        self.isMale = isMale
        self.phoneNumber = phoneNumber


    def showInfo(self):
        gender = "Male" if self.isMale else "Female"
        print(f"Your name is {self.name} and you are {self.age} old and your gender is {gender} and your phone number {self.phoneNumber}")


class Programmer(Info):
    
    def showProgrammerData(self):
        print(f"{self.name} {self.age}");


person1 = Info("M Hashim" , 22 , True , "03130000000")
# person1.showInfo()

person2 = Programmer("Dayan" , 8 , True , "0000000000")
# person2.showProgrammerData()




# /////// SUPER KEYWORD //////////

class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id


class TestEmployee(Employee):
    def __init__(self , name , id ,lang):
        super().__init__(name , id)
        self.lang = lang



p1 = TestEmployee("M Hashim" , 200 , "Python")

# print(p1.id)
# print(p1.name)
# print(p1.lang)

# ///// Platform ////////

print(platform.system())
print(platform.machine())
print(platform.processor())
print(platform.architecture())
print(platform.uname())
print(platform.version())
print('-----------------------------')
print(' ')
print(' ')
print(' ')
# print('')
# print(dir(platform))
# help(platform)

class School:
    def __init__(self, schoolName , schoolAddress , schoolContact):
        self.schoolName = schoolName
        self.schoolAddress = schoolAddress
        self.schoolContact = schoolContact
        
 
    def showSchooolDetail(self):
        print(f"School name is {self.schoolName} and it's address is {self.schoolAddress} and contact is {self.schoolContact}")




class Student(School):
    
    def __init__(self , id , name , age, stuClass , rollNo , schoolName , schoolAddress , schoolContact):
        super().__init__(schoolName , schoolAddress , schoolContact)
        self.id = id
        self.name = name
        self.age = age
        self.stuClass = stuClass
        self.rollNo = rollNo
    
    
    def shoeInfo(self):
        print(f'Student id is {self.id} and his name is {self.name} and {self.age} years old and in class {self.stuClass} and his rollNo is {self.rollNo}')
        


print(" >>>>>>> Student Info <<<<<<<<")
stu1 = Student(1 , "M Hashim" , 22 , "13 Semester" , 10, "The Educators" , "Charsdaa" , "03130000000")
stu1.shoeInfo()
print('----------------------')
print(stu1.schoolName)
stu1.showSchooolDetail()