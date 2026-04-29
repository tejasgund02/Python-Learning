class person:
    name = "unknown"
    age = 0
    occupation = "unknown"
    def info(self):
        print(f" {self.name} is {self.age} years old and works as a {self.occupation}")

p1 = person()
p1.name = "John"   
p1.age = 30
p1.occupation = "Software Engineer"
p1.info()