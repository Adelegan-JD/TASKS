class Student:      # This creates a class calleed Student
    def __init__(self, name, course, level):        # This initializes the class, and creates the referencing
        print("Creating a new student...")
        self.name = name  # This assigns name to the object
        self.course = course        # This assigns course to the object
        self.level = level      # This assigns level to the object
        print(f'Student {name} has been created!')

kemi = Student("Kemi Adebayo", "Computer Science", 300)


class NigerianStudent:
    def __init__(self, name, state, course, level):
        print(f"Step 1: Creating student object")
        self.name = name  # This assigns name to the object
        self.state_of_origin = state        # # This assigns state to the object
        self.course = course   # This assigns course to the object
        self.level = level      #This assigns level to the object
        self.student_id = self.generate_id()      #This generates a unique id for the object
        print(f'Step 6: {self.name} from {self.state_of_origin} is ready! Your matric number is {self.student_id}')

    def generate_id(self):
        import random
        return f'UNIOGUN{random.randint(10000, 99999)}'

# When an object is created, this happens
ayo = NigerianStudent('Ayo Daniel', 'Ogun', 'Machine Learning', 400)

# To print each attribute, call the function name
print(ayo.name)

# Another Example
class PhoneUser:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.airtime = 0
        print(f'{self.name} joined {self.network} network')


    def buy_airtime(self, amount):
        self.airtime += amount  # self ensures it gets the RIGHT person
        return f"{self.name} now has NGN{self.airtime} airtime"


# Creating multiple users
abeeb = PhoneUser("Abeeb Bakare", "MTN")
onisemo = PhoneUser("Onisemo Williams", "Airtel")

# Each person's actions affect only affect their own account
print(abeeb.buy_airtime(500))
print(onisemo.buy_airtime(500))

print(abeeb.airtime)
print(onisemo.airtime)

# Defining the attributes of a student
class Student:
    def __init__(self, name, course, level, state_of_origin):
        self.name = name
        self.course = course
        self.level = level
        self.state_of_origin = state_of_origin
        self.cgpa = 0.0

# Creating a studentt object
Fathia = Student("Fathia Abdul", "Biochemistry", 400, "Ogun State")

# Accessing Attributes
print(Fathia.name)
print(Fathia.course)
print(Fathia.level)
print(Fathia.state_of_origin)

# TYPES OF ATTRRIBUTES
# 1. Instance Attributes - unique to each object
student1 = Student("Anthony Joshua", "Engineering", 200, "Ogun")
student2 = Student("Fadilat Hassan", "Medicinee", 400, "Lagos")
print(student1.name)
print(student2.name)

# 2. Class attributes: Shared by all objects of the class
class Student:
    university = "Federal University of Technology, Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course

student1 = Student("Anthony Joshua", "Engineering")
student2 = Student("Fadilat Hassan", "Medicinee")
print(Student.university)     
print(student1.university)   
print(student2.university)   


# METHODS - They describe what the person can do

class Student:
    def __init__(self, name, course, level):
        #Attributes
        self.name = name
        self.course = course
        self.level = level
        self.cgpa = 0.0
        self.fees_paid = False

    #Method: The action the student can do
    def pay_school_fees(self):
        self.fees_paid = True
        return f"{self.name} has paid school fees for {self.level} level"
    
    #Method: Another action
    def register_courses(self):
        if self.fees_paid:
            return f"{self.name} has registered courses for {self.course}"
        else:
            return f"{self.name} is yet to pay tuition!"
        
    #Method: another action to calculate gpa
    def calculate_gpa(self, grades):
        if grades:
            self.cgpa = sum(grades) /len(grades)
            return f"{self.name}'s  CGPA is now {self.cgpa:.2f}"
        return "No grades provided"





























