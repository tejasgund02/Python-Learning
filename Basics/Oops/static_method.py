class claculation:
    def __init__(self, n):
        self.n = n
    
    def addonline(self, n):
        self.n = n + self.n
    
    @staticmethod
    def add(a, b):
        return a+b

# Example usage
result = claculation.add(5, 10)
print(result)  # Output: 15

a = claculation(10)
a.addonline(6)  
print(a.n)  # Output: 15
print(a.add(3, 7))  # Output: 10