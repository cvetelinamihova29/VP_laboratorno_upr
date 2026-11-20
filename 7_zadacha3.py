class Animal: 
    def make_sound(self): 
        print('Животното издава звук')

class Dog(Animal): 
    def make_sound(self): 
        print('Кучето лае: Бав-бав!')

dog1 = Dog()
dog1.make_sound()