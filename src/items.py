

class Item:
    def __init__ (self, name:str, description:str, quantity:int, price:float):

        # data validation
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(description, str):
            raise TypeError("Description must be a string")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if not isinstance(price, (float,int)):
            raise TypeError("Price must be a float")
        
        assert quantity >= 0, "Quantity must be greater than or equal to 0"
        assert price >= 0, "Price must be greater than or equal to 0"


        # self assignment
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
    
    # def __str__ (self):
        # return f"{self.name}:\n\t{self.description}\n\tQuantity: {self.quantity}\n\tPrice: {self.price}"
    
    def get_stock_quantity (self):
        return self.quantity
    
    def get_total_price (self):
        return self.quantity * self.price
    

iphone15 = Item("iPhone 15", "The latest iPhone", 10, 1000)
print(iphone15.quantity)

iphone15Plus = Item("iPhone 15 Plus", "The latest iPhone", 100, 1000)
print(iphone15Plus.quantity)