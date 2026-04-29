class Employee:
    company= "Google"  # class variable
    def __init__(self, name):
        self.name = name  # instance variable
    def showDetails(self):
        print(f"Employee Name: {self.name}, Company: {self.company}")
    
    @classmethod
    def changeCompany(cls, new_company):
        cls.company = new_company  # This will change the class variable for all instances
    # def changeCompany(self, new_company):
    #     self.company = new_company  # This will create an instance variable for the specific object
    #     # To change the class variable for all instances, we should use Employee.company = new_company

emp1 = Employee("Tejas")
emp2 = Employee("John")


emp1.showDetails()  # Output: Employee Name: Tejas, Company: Google
emp2.changeCompany("Apple")  # This will change not the company for emp2 only but for all the instances of the class Employee 
emp2.showDetails()  # Output: Employee Name: John, Company: Apple
print(Employee.company)  # Output: Apple