# Operator overloading in python allows us to define the behavior of operators for user-defined class:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p1+p2)
# print(dir(p1))
e= 34
print(dir(e))