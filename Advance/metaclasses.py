# write a simple realtime example of metaclass in python


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        return f"{self.name} is eating yem yum..."
        
class customMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        # print("Base classes:", bases)
        # print("Attributes:", attrs)
        attrs["school"]= "Deathcode school" # Add a new attribute to the class
        bases = (person,)  # Add person as a base class
        return super().__new__(cls, name, bases, attrs)
    
   


class student(metaclass=customMetaclass):
    def __init__(self, rno, classroom):
        self.name = rno
        self.age = classroom

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.name}, Classroom: {self.age}, School: {self.school}  ")

# Create an instance of the student class
s1 = student(43, "10th grade")
s1.name = "John"
s1.age = 15
print(s1.eat())
s1.display()