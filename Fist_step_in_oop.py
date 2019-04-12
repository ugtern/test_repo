from cat_class import Cat

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('bark! bark!')

    def bit(self):
        print(self.name+' biting you!')
    

ozzy = Dog('ozzy', 2)
smoke = Cat('smoke', 2,'meow','tsarap!')
print(ozzy.name, smoke.name)

