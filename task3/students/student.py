class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)