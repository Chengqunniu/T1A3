import sys
from class_for_text import display_message
from class_for_customer import Customer, Order


def collect_info():
    '''Collect customers' name'''
    global name

    message1 = display_message('You have selected to place order for customers')
    message1.color()
    sys.stdout.write('Enter the name of the customer:' + '\n')
    
    valid_name = True
    while valid_name:
        # Check whether the inpput is valid
        # Give user another chance if input is invalid     
        name = sys.stdin.readline().strip()
        try:
            name = float(name)
        except ValueError:
            valid_name = False
            return name
        else:
            sys.stdout.write('please enter a valid name, not number\n')
    
    return name


def collect_info_and_order():
    customer_name = Customer(collect_info())
    customer_name.add_membership()
    customer_name.add_rewards_membership()
    customer_order = Order(name)
    customer_order.order()
    customer_order.record_quantity()
    customer_order.repeat_order()
    customer_order.calculate_price()
    customer_order.print_receipt()
    customer_name.store_order_history()

if __name__ == '__main__':
    collect_info_and_order()  
    print()
