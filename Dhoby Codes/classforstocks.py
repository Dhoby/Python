class Stock:
    '''A simple attempt to represent a stock'''
 
    def __init__(self, name, buy_price, quantity):
        '''Initialize attributes to describe a stock'''
        self.name = name
        self.buy_price = buy_price
        self.quantity = quantity
 
    def get_descriptive_name(self):
       '''Return a neatly formatted descriptive name'''
       long_name = f"{self.name} {self.buy_price} {self.quantity}"
       return long_name.title()


stock_01 = Stock('同仁堂', 46.4225, 800)
print(stock_01.get_descriptive_name())  