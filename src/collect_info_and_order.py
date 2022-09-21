import sys
from class_for_text import display_message
from class_for_customer import Customer



def collect_info_and_order():
    '''Collect customers' name'''
    message1 = display_message('Pleas press enter to order')
    message1.color()
    sys.stdout.write('Enter the name of the customer:' + '\n')

    while True:
        # Check whether the inpput is valid
        # Give user another chance if input is invalid     
        name = sys.stdin.readline().strip()
        try:
            name = float(name)
        except ValueError:
            break
        else:
            sys.stdout.write('please enter a valid name, not number\n')


    customer_name = Customer(name)
    customer_name.order()
    customer_name.record_quantity()
    customer_name.repeat_order()
    customer_name.add_membership()
    customer_name.calculate_price()
    customer_name.print_receipt()
    customer_name.store_order_history()

    print()
