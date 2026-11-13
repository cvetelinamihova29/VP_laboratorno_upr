class Person: 
    def __init__(self, name, family, age, nationality): 
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    def print_info(self): 
        print('Име:', self.name)
        print('Фамилия:', self.family)
        print('Възраст:',self.age)
        print('Националност:', self.nationality)
person1 = Person('Иван', 'Петров', 20, 'България')
person1.print_info()