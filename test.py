
class Tomato():
    def type(self):
        print('Vegetables')
    def color(self):
        print('Red')

class Apple():
    def type(self):
        print('Fruit')
    def color(self):
        print('red')
    

obj_apple = Apple()
obj_tomato = Tomato()
for attribute in (obj_apple, obj_tomato):
    attribute.type()
    attribute.color()
