import sys
from class_for_text import text
from collect_info_and_order import collect_info_and_order
from display_customer_info import customer_info
from display_order_history import check_history
from add_update_menu import add_sold_out_stickers, add_update
from display_products import display_products


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
    4: Add update menu items
    5: Add sold out menu items
    6: Display products
    0: Exit the system
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
        elif category == '4':
            add_update()
            press_enter.color_input()
            welcome_page()  
        elif category == '5':
            add_sold_out_stickers()
            press_enter.color_input()
            welcome_page() 
        elif category == '6':
            display_products()
            press_enter.color_input()
            welcome_page()  
        elif category == '0':
            print('Bye')
            sys.exit()  