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
        self.repeat_order()
        self.calculate_price()


        
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

    def repeat_order(self):
        '''Used for repeat order.
        '''
        valid = False
        # While loop to check whether customers need to order anthor dish or not.
        while not valid:
            sys.stdout.write('Want to order another sticker? ' + 'Y or N' + '\n')
            another_sticker = str(sys.stdin.readline().strip())
            # If the answer is not N, then the loop will repeat.
            if another_sticker == 'N':
                valid = True
                return valid
            elif another_sticker == 'Y':
                sys.stdout.write('Enter a valid sticker name' + '\n')
                new_sticker_name = str(sys.stdin.readline().strip())
                while new_sticker_name not in menu:
                    # Read the new input
                    new_sticker_name = str(input('Please enter a valid sticker name:').strip())
                sticker = new_sticker_name
                self.record_quantity()

    def calculate_price(self):
        '''calculate the price
        '''
        global total_cost
        global discount

        base_price = 0

        for sticker_index, sticker_name in enumerate(order):    
            price = float(menu[sticker_name]) * int(number_of_stickers[sticker_index])
            base_price += price
        total_cost = base_price

    