class pizza:
    def __init__(self,name,price):
        self.name=name 
        self.price=price
        
    def display(self):
        print(f"Pizza Name: {self.name}, Price: ${self.price}")
    
    
class burger(pizza):
    
    def display(self):
        return super().display()
    
        
class ColdDrink(pizza):
    def display(self):
        return super().display()