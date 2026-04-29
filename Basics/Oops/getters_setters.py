# write a doc string for difference between below two classes and which one is better to use in which scenario.
"""
The first class, `Person`, uses traditional getter and setter methods to access and modify the attributes. This approach is straightforward and works well, but it can lead to more verbose code when accessing or modifying attributes.
The second class, `PersonWithProperty`, uses property decorators to create a more Pythonic way of accessing and modifying attributes. This approach provides a cleaner syntax and allows for additional logic to be included in the getter and setter methods, such as validation.

In general, using property decorators is considered a better practice in Python as it provides a more elegant and readable way to manage attribute access. It also allows for better encapsulation and can help prevent unintended side effects when modifying attributes. However, the traditional getter and setter methods may still be useful in certain scenarios where you want to explicitly control the access to attributes or when working with legacy code.

"""              
# Below are some examples of getters and setters in Python with description for beginners. Getters and setters are methods that allow you to access and modify the attributes of a class while encapsulating the internal representation.

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, name):
        self._name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

# Example usage
person = Person("Alice", 30)
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.set_name("Bob")
person.set_age(25)
print(person.get_name())  # Output: Bob
print(person.get_age())   # Output: 25

# Using property decorators for getters and setters
class PersonWithProperty:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

# Example usage
person_prop = PersonWithProperty("Charlie", 40) 
print(person_prop.name)  # Output: Charlie
print(person_prop.age)   # Output: 40   
person_prop.name = "Dave"
person_prop.age = 35    
print(person_prop.name)  # Output: Dave
print(person_prop.age)   # Output: 35   
