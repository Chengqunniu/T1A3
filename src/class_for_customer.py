import sys
import json


with open('Menu.json', 'rb') as menu_list:
    menu = json.load(menu_list)

class Customer:

    def __init__(self, name):
        self.name = name

    def order(self):
        '''order stickers
        '''
        global sticker
        global order
        global number_of_stickers

        number_of_stickers = []
        order = []
        sys.stdout.write('Enter the sticker name [Enter a valid sticker only, e.g. Yum Yum Hana]:\n')
        sticker = str(sys.stdin.readline().strip())
        # While loop to check whether the input dish name is in the Menu. If not in the Menu, then the while loop will keep looping.
        while sticker not in menu:   
            sys.stdout.write('Please enter a valid sticker name:'+ '\n')
            sticker = str(sys.stdin.readline().strip())
        self.record_quantity()
        self.repeat_order()
        self.add_membership()
        self.calculate_price()
        self.print_receipt()

        
    def record_quantity(self):
        '''check whether the quantity input is integer and greater than zero
        '''
        quantity_is_float = True
        
        # While loop to check the input and give user another change if the input is invalid.
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
        print(number_of_stickers)
        for sticker_index, sticker_name in enumerate(order):    
            price = float(menu[sticker_name]) * int(number_of_stickers[sticker_index])
            base_price += price
        self.search_rewards_customer()
        if self.name in rewards_customer_list:
            total_cost= float(base_price * 9/10)
            discount = str('-10%')
        else:
            total_cost = base_price
            discount = str('0%')
    
    def add_membership(self):
        '''Add customer to the rewards customer list
        '''
        self.search_rewards_customer()
        if self.name not in rewards_customer_list:
            valid = False
            while not valid:
                sys.stdout.write('The customer is not in the rewards program. Does the customer want to join the rewards program' + '\n' + '[Enter Y/N]?' +'\n')
                answer = str(sys.stdin.readline().strip())
            # Check whether the answer is valid.
                if answer == 'Y' or answer == 'N':
                    valid = True
            if answer == 'Y':
                sys.stdout.write('Successfully add the customer to the rewards program' + '\n')
                self.add_rewards_customer()

    def store_order_history(self):
        '''Store customer order histories
        '''
        self.search_customer()
        index_of_customer = customer_list.index(self.name) 
        # For loop to record customer order hisotry.
        self.search_order_history()
        personal_order_history = ''
        for sticker_index, sticker_name in enumerate(order):
            order_history = (str(number_of_stickers[sticker_index]) + 'x' + str(sticker_name) + '|')
            personal_order_history += str(order_history)
        final_personal_order_history = {str(personal_order_history):  str(total_cost)}
        customer_order_history[index_of_customer].append(final_personal_order_history)
        with open('Customer_order_history.json', 'w') as add_history:
            json.dump(customer_order_history, add_history)

    def print_receipt(self):
        '''Print receipt
        '''
        print('*' * 50)
        print('Receipt of Customer' + ' ' + str(self.name))
        print('*' * 50)
        # This function is to align the line of the receipt
        receipt_line = lambda left, right: (f'{left:25}  {str(right):>25}') +'\n'
       
        # Use for loop to display each dish on a single line on the receipt.
        for dish_index, dish_name in enumerate(order):      
            unit_price = menu[dish_name]
            Line_1 = str(unit_price) + '(AUD)' + ' x ' + str(number_of_stickers[dish_index])
            sys.stdout.write(receipt_line(str(dish_name + ':'), Line_1))
        Line_2 = str(discount) + '(AUD)'
        Line_3 = str(total_cost) + '(AUD)'
        sys.stdout.write(receipt_line('Discount:', Line_2))
        sys.stdout.write(receipt_line('Total Cost:', Line_3))  

    def search_rewards_customer(self):
        global rewards_customer_list
        rewards_customer_list = []
        with open('Rewards_customer_list.json', 'rb') as rewards_customer:
            rewards_customer_list = json.load(rewards_customer)

    def add_rewards_customer(self):
        self.search_rewards_customer()
        rewards_customer_list.append(self.name)
        with open('Rewards_customer_list.json', 'w') as rewards_customer:
            json.dump(rewards_customer_list, rewards_customer)
          
    def search_customer(self):
        global customer_list
        with open('Customer_list.json', 'rb') as customer:
            customer_list = json.load(customer)

        return customer_list

    def add_customer(self):
        self.search_customer()
        customer_list.append(self.name)
        with open('Customer_list.json', 'w') as customer:
            json.dump(customer_list, customer)

    def search_order_history(self):
        global customer_order_history
        with open('Customer_order_history.json', 'rb') as search_history:
            customer_order_history = json.load(search_history)

        return customer_order_history