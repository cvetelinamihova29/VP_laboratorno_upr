class Person: 
   def __init__(self, name, age): 
      self.name = name
      self.age = age
   def introduce(self):
      print('Здравей, аз съм', self.name, 'и съм на', self.age, 'години')

person1 = Person('Иван', 20)
person2 = Person('Мария', 30)
person1.introduce()
person2.introduce()