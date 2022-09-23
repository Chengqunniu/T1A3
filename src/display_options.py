import sys
import clearing
from class_for_text import text
from collect_info_and_order import collect_info_and_order
from display_customer_info import customer_info
from display_order_history import check_history
from add_update_menu import add_sold_out_stickers, add_update
from display_products import display_products
from simple_term_menu import TerminalMenu


press_enter = text('Press enter to continue...')
message2 = text('Welcome to the Smoonypaws ordering system!' )


def welcome_page():
    options = ['1: Collect information & Order stickers',
     '2: Display existing customer information',
     '3: Check customer order history',
     '4: Add update menu items',
     '5: Add sold out menu items',
     '6: Display products',
     '0: Exit the system']
    terminal_menu = TerminalMenu(options, title='Options')
    menu_entry_index = terminal_menu.show()
    match menu_entry_index:
        case 0:
            collect_info_and_order()
            press_enter.color_input()
            welcome_page()
        case 1:
            customer_info()
            press_enter.color_input()
            welcome_page()
        case 2:
            check_history()
            press_enter.color_input()
            welcome_page()   
        case 3:
            add_update()
            press_enter.color_input()
            welcome_page()  
        case 4:
            add_sold_out_stickers()
            press_enter.color_input()
            welcome_page() 
        case 5:
            display_products()
            press_enter.color_input()
            welcome_page()  
        case 6:
            clearing.clear()
            print('Bye')
            sys.exit()