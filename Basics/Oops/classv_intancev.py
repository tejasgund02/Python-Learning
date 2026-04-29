class Employees:
    company = "Apple"   #--> class Veriable
    def __init__(self, name):
        self.name = name
   
    def showDetails(self):
        print(f"Employee Name: {self.name}, Company: {self.company}")


emp1 = Employees("John")
emp2 = Employees("Tejas")
emp2.company = "Google" #--> instance variable scpecific for emp2

emp1.showDetails()  # Output: Employee Name: John, Company: Apple
emp2.showDetails()  # Output: Employee Name: Tejas, Company: Google

    