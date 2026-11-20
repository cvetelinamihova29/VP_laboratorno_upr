class Counter: 
    value = 0
    def increment(self): 
        self.value +=1
    def show(self):
        print(self.value)

count1 = Counter()
count1.increment()
count1.increment()
count1.show()
count2 = Counter()
count2.increment()
count2.show()