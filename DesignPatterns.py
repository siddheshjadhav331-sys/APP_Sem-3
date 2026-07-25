from abc import ABC, abstractmethod

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating Singleton Instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

print("Singleton Pattern Example")
obj1 = Singleton()
obj2 = Singleton()
print("Both objects are same:", obj1 is obj2)

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        return "Woof!"

class Cat(Animal):

    def speak(self):
        return "Meow!"

class AnimalFactory:

    @staticmethod
    def get_animal(name):
        if name.lower() == "dog":
            return Dog()
        elif name.lower() == "cat":
            return Cat()
        else:
            return None

print("Factory Pattern Example")
animal = AnimalFactory.get_animal("dog")
print("Dog:", animal.speak())

animal = AnimalFactory.get_animal("cat")
print("Cat:", animal.speak())

class Observer:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")

class Subject:

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

print("Observer Pattern Example")
subject = Subject()

o1 = Observer("Rahul")
o2 = Observer("Nikhil")

subject.attach(o1)
subject.attach(o2)

subject.notify("New Notification Available")

class Strategy(ABC):

    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):

    def execute(self, a, b):
        return a + b

class MultiplyStrategy(Strategy):

    def execute(self, a, b):
        return a * b

class Context:

    def __init__(self, strategy):
        self.strategy = strategy

    def perform(self, a, b):
        return self.strategy.execute(a, b)

print("Strategy Pattern Example")

context = Context(AddStrategy())
print("Addition:", context.perform(10, 5))

context = Context(MultiplyStrategy())
print("Multiplication:", context.perform(10, 5))

#Output
"""
Singleton Pattern Example
Creating Singleton Instance...
Both objects are same: True
Factory Pattern Example
Dog: Woof!
Cat: Meow!
Observer Pattern Example
Rahul received: New Notification Available
Nikhil received: New Notification Available
Strategy Pattern Example
Addition: 15
Multiplication: 50
"""