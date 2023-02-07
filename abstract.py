from abc import ABC, abstractmethod
class FruitAbstract(ABC):

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def weight(self):
        pass


class Apple(FruitAbstract):

    def color(self):
        print('Red')


    def price(self):
        print('15 petot')
    
    def weight(self):
        print('100 grams')

class Banana(FruitAbstract):

    def color(self):
        print('yellow')


    def price(self):
        print('35 petot')
    
    def weight(self):
        print('150 grams')

class Orange(FruitAbstract):

    def color(self):
        print('orange')


    def price(self):
        print('50 petot')
    
    def weight(self):
        print('300 grams')


apple = Apple()
apple.color()
apple.weight()
apple.price()

orange = Orange()
orange.color()
orange.weight()
orange.price()


banana = Banana()
banana.color()
banana.weight()
banana.price()