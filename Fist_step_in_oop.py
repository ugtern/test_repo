class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('bark! bark!')

ozzy = Dog('ozzy', 2)
print(ozzy.name)

