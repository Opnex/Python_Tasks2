# class Students:
#     def __init__(self, name, course, level):
#         print("Creating a new student.....")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f"Student {name} has been created")

# details = Students("kemi Adebayo", "Computer Science", 300)
# print(details.course, details.level)




# # **How __init__ and self Work Together**
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating Stdent object.....")
#         self.name = name
#         self.state_of_origin = state
#         self.course = course
#         self.student_id = self.generate_id()
#         print(f"step 6: {self.name} from {self.state_of_origin} is ready")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"

# file = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")
# print(file.name)
# print(file.state_of_origin)
# print(file.course)
# print(file.student_id)




# # _more exaple_
# class phoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")
    
#     def buy_airtime(self, amount):
#         self.airtime += amount
#         return f"{self.name} now has #{self.airtime} airtime"
    
# # Creating multiple user
# data1 = phoneUser("Abeeb Bakare", "MTN")
# data2 = phoneUser("Onisemo Williams", "Airtel")

# # Each person's actions affect only their own account
# print(data1.buy_airtime(500))
# print(data2.buy_airtime(1000))
# print(data1.airtime)
# print(data2.airtime)



# # Defining Attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0

#     # Creating a student object
# fathia = Student("Fathia Abdul", "Biochemistry", 300, "Ogun State")

# # Accessing attributes
# print(fathia.name)
# print(fathia.course)
# print(fathia.state_of_origin)

#### Types of Attributes
# 1. Instance Attributes - Unique to each object

# student1 = Student("Anthony Johnson", "Engineer", 200, "Ogun")
# student2 = Student("Fadilat Hassan", "Medicine", 200, "Lagos")

# print(student1.name)
# print(student2.name)


# # 2. Class Attributes - Shared by all objects of the class
# class Student:
#     university = "Fedaral University of Technology Akure"

#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
# student1 = Student("Opeyemi", ("Accounting"))
# student2 = Student("Lekan", ("Biology"))

# print(Student.university)
# print(Student.university)
# print(Student.university)




# class Student:
#     def __init__(self, name, course, level):
#         # Attribute
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpg = 0.0
#         self.fees_paid = False

#     # Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_course(self):
#         if self.fees_paid:
#             return f"{self.name} has registered course for {self.course}"
#         else:
#             return f"{self.name} must pay school fees first!"
        
#           # Method: calculates CGPA
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided"
    
#     # Using methods
# Abiodun = Student("Abiodun Akinola", "Gistology", 600)
# print(Abiodun.pay_school_fees())
# print(Abiodun.register_course())
# print(Abiodun.calculate_cgpa([4.2, 3.8, 4.0, 3.5]))




# #### Types of Methods
# # 1. Instance Methods - Work with specific object data


# # 'self' refers to the specific student
# def pay_school_fees(self):
#     return f"{self.name} has paid school fees"


# # 2. Class Methods - Work with class-level data
# @classmethod
# def get_university(cls):
#     return cls.unigversity


# # 3. Static Methods - Don't need object or class data
# @staticmethod
# def academic_calender():
#     return "Academic session run from September to July"



# **How Attributes and Methods Work Together**
# - The Relationship
# - Attributes store the data
# - Methods use and modify that data

class BankAccount:
    def __init__(self, owner, bank_name, balance=0):
        # ATTRIBUTES - What the account HAS
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    # METHODS - What the account can DO
    def deposit(self, amount):
     """Add money to the account"""
     if amount > 0:
        self.balance += amount # Method changes attribute
        return f"#{amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: #{self.balance:,}"
     return "Invalid deposit amount"
    

    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > 0 and amount <= self.balance:
           self.balance -= amount # Method changes attribute
           return f"#{amount:,} withdraw from {self.owner}'s account. New balance: #{self.balance}"
        return "Insufficient funds or invalid amount"
    

    def transfer(self, amount, recipient):
       """Remove money from the account"""
       if amount > 0 and amount <= self.balance:
          self.balance -= amount
          return f"#{amount:,} transfered from {self.owner} to {recipient}. Remaining balance: #{self.balance:,}"
       return "Transfer failed: Insufficient funds"
    

    def check_balance(self):
       """Check current balance"""
       return f"{self.owner}'s {self.bank_name} account balance: #{self.balance}"
    

    def generate_account_number(self):
       """Generate a unique account number"""
       import random
       return f"01{random.randint(10000000, 99999999)}"
    

    # Creating and using the account
Opnex_account = BankAccount("Thomas Opeyemi", "AXT Bank", 50000)


# Attributes (characteristics)
print(Opnex_account.deposit(25000))
print(Opnex_account.withdraw(10000))
print(Opnex_account.transfer(15000, "Oladunjoye Ayomidimeji"))
print(Opnex_account.check_balance())
        
    
