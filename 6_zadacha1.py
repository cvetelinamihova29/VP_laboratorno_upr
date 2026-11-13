class Person: 
    def __init__(self, name, family, age, nationality): 
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print_1(self): 
        print('Име:', self.name)
        print('Фамилия:', self.family)
        print('Възраст:',self.age)
        print('Националност:', self.nationality)

person1 = Person('Иван', 'Петров', 20, 'България')
person1.print_1()

class Student(Person): 
    def __init__(self, name, family, age, nationality, university, yearofstudy): 
        Person.__init__(self, name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    def print_info(self): 
        print('Име:', self.name)
        print('Фамилия:', self.family)
        print('Възраст:', self.age)
        print('Националност:', self.nationality)
        print('Университет:', self.university)
        print('Година на учене:', self.yearofstudy)

person2 = Student('Иван', 'Петров', 20, 'България', 'ТУ София', 2026)
person2.print_info()

class Lecturer(Person): 
    def __init__(self, name, family, age, nationality, university, experience):
        Person.__init__(self, name, family, age, nationality)
        self.university = university
        self.experience = experience
    def print2(self): 
        print('Име:', self.name)
        print('Фамилия:', self.family)
        print('Възарст: ', self.age)
        print('Националност: ', self.nationality)
        print('Университет: ', self.university)
        print('Години стаж: ', self.experience)

person3 = Lecturer('Мария', 'Иванова', 50, 'България', 'ТУ София', 30)
person3.print2()