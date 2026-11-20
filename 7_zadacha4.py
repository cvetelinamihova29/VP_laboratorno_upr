class Person: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

class Student(Person): 
    def __init__(self, name, age, faculty_number): 
        super().__init__(name, age)
        self.faculty_number = faculty_number

student1 = Student('Иван', 20, 121226118)
