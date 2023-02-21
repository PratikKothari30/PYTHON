#inheritance
class Faculty:
    def _init_(self, f_name, department, f_id):
        self.f_name = f_name
        self.department = department
        self.f_id = f_id

    def print_info(self):
        print('Faculty Information =',self.f_name, self.department, self.f_id)

# obj1 = Faculty("Ashish","Computer_Science",1001)
#obj1.print_info()

#=============================================================================
class Cse(Faculty):
    pass
obj = Cse("Jyoti Mam","Science",1023)
obj.print_info()

#=============================================================================
'''class Me(Faculty):
    pass
obj = Me("xyz Mam","Computer",1006)
obj.print_info()'''

#=============================================================================
#Single Inheritance
'''class college:     #Parent class
    def college_name(self):
        print("\nDr.D.Y.Patil Institute of Technology")

class Student(college):   #child class
    def Student_info(self):
        print("\nName : Pratik Kothari")
        print("Branch : Electronics")

obj = Student()
obj.college_name()
obj.Student_info()
'''
#===============================================================================
#Multilevel Inheritance
'''class college:
    def college_name(self):
        print("\nDr.D.Y.Patil Institute of Technology")'''
#===============================================================================
'''class Student(college):
    def Student_info(self):
        print("\nName : Pratik Kothari")
        print("Branch : Electronics")'''
#===============================================================================
'''class Exam(Student):
    def subject(self):
        print("Subject-1 : Design Engineer")
        print("Subject-2 : Math")
        print("Subject-3 : C-Language")

obj = Exam()
obj.college_name()
obj.Student_info()
obj.subject()
'''
#===============================================================================
#Multiple Inheritance
class SubMarks:
    math = int(input("\nEnter paper marks of Math :"))
    DE = int(input("Enter paper marks of design Engineering :"))
    C = int(input("Enter paper marks of C-Language :"))
    English = int(input("Enter paper marks of English :"))
#===============================================================================
class PractMarks:
    cpract = int(input("Enter practicals marks of C Language :")) 
#===============================================================================
class Result(SubMarks, PractMarks):
#print("If student pass in both = Subject and practical paper then pass")
  def total(self):
    if self.math>=40 and self.DE>=40 and self.C>=40 and self.English>=40 and self.cpract>=20:
        print("Pass")
    else:
        print("Fail")

obj = Result()
obj.total()