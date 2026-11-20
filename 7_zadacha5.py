class Flyer: 
    def fly(self):
        print('Летя в небето')

class Swimmer: 
    def swim(self): 
        print('Плувам във водата')

class Duck(Flyer, Swimmer): 
    pass

duck1 = Duck()
duck1.fly()
duck1.swim()
print(Duck.mro())