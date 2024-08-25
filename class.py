class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_one = Person("Nafis", 26)
print(f"Hello {person_one.name} speaking. Age is {person_one.age}.")