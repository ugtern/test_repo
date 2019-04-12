class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('bark! bark!')

    def bit(self):
        print(self.name+' biting you!')
    

ozzy = Dog('ozzy', 2)
print(ozzy.name)

