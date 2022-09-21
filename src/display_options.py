import sys
from class_for_text import text
from collect_info_and_order import collect_info_and_order
from display_customer_info import customer_info
from display_order_history import check_history


press_enter = text('Press enter to continue...')
message2 = text('Welcome to the Smoonypaws ordering system!' )

def welcome_page():
    '''Welcome page for the system
    '''
    # sys.stdout.write('Welcome to the Smoonypaws ordering system!' + '\n')
    message2.color()
    print()
    sys.stdout.write('#'* 40)
    sys.stdout.write('''
    You can choose from the following options:
    1: Collect information & Order stickers
    2: Display existing customer information
    3: Check customer order history
    ''' + '\n')
    sys.stdout.write('#' * 40 + '\n')
    # If customer does not enter a correct number, it will keep asking them to enter a right number.
    number_not_zero = True
    while number_not_zero:
        category= str(input('Choose one option:').strip())
        if category == '1':
            collect_info_and_order()
            press_enter.color_input()
            welcome_page()
        elif category == '2':
            customer_info()
            press_enter.color_input()
            welcome_page()
        elif category == '3':
            check_history()
            press_enter.color_input()
            welcome_page()   