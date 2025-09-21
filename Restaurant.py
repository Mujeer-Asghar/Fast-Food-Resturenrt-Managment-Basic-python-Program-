class Restaurant:
    def __init__(self,name,price):
        self.name=name 
        self.price=price
    def display(self):
        print(f"Pizza Name: {self.name}, Price: ${self.price}")


class pizza(Restaurant):
    def display(self):
        return super().display()
    
class burger(Restaurant):
    
    def display(Restaurant):
        return super().display()
    
        
class ColdDrink(Restaurant):
    def display(self):

        return super().display()
