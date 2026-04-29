class person:
    def __init__(self, n = "tejas" , o = "Gunda"):
        self.name = n
        self.acc = o
    def info(self):
        print(f"{self.name} is a {self.acc}")

# a = person()
# a.info()
# a.name = "Dhanasree"
# a.acc = "Data Scientist"
# a.info()

a = person("Tejas", "Devloper")
a.info()
b = person()
b.info()