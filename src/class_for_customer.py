import sys
import json


with open('Menu.json', 'rb') as menu_list:
    menu = json.load(menu_list)

class Customer:

    def __init__(self, name):
        self.name = name

    def order(self):
        global sticker
        global order

        order = []
        sys.stdout.write('Enter the sticker name [Enter a valid sticker only, e.g. Yum Yum Hana]:\n')
        sticker = str(sys.stdin.readline().strip())
        # While loop to check whether the input dish name is in the Menu. If not in the Menu, then the while loop will keep looping.
        while sticker not in menu:   
            sys.stdout.write('Please enter a valid sticker name:'+ '\n')
            sticker = str(sys.stdin.readline().strip())
        self.record_quantity()
        
    def record_quantity(self):
        '''check whether the quantity input is integer and greater than zero
        '''
        global number_of_stickers
        number_of_stickers = []
        quantity_is_float = True
        while quantity_is_float:
            sys.stdout.write('Enter the sticker quantity [Enter a positive integer only, e.g. 1, 2, 3]:\n')
            quantity = (sys.stdin.readline().strip())
            # Use try-except to exclude float, 0, negative and input that not a number.
            try:
                quantity_1 = int(quantity)
                if quantity_1 > 0:
                    quantity_is_float = False
            except ValueError:
                quantity_is_float = True
        order.append(sticker)
        number_of_stickers.append(quantity)