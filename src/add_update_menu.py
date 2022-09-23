import json
import sys
from class_for_text import display_message


def add_update():
    '''Add and update menu items.

    Input should be the correct format.
    '''  
    message4 = display_message('You have selected to add and update menu items')
    message4.color()

    search_menu()
    string = str(input('Please enter the new stickers and prices with the following format: '
                      + 'sticker_1 : price_1, sticker_2: price_2\n').strip())
    string_list = string.split(',')
    new_menu_list = []
    # For loop to update the stickers and prices
    for x in string_list:  #obtain each sticker and their cost as a single string
        change_list = x.split(':')    
        # Remove space for each string, then form a list. 
        # Later use for loop to go though the list and update the menu and price.
        for i in change_list:
            new_sticker = (i.strip())      
            new_menu_list.append(new_sticker)
        # Use try-except to exclude input that is 0, negative or not a number.
        try:
            new_price = float(new_menu_list[1]) 
            if new_price > 0:
                menu[new_menu_list[0]] = new_price
            else:
                print('The price entered for' + ' ' + str(new_menu_list[0] +' ' + 'is not valid'))
        except ValueError:
            print('The price entered for' + ' ' + str(new_menu_list[0] +' ' + 'is not valid'))
        new_menu_list = []
    with open('Menu.json', 'w', encoding='utf8') as menu_list:
        json.dump(menu, menu_list)

    return menu


def add_sold_out_stickers():
    '''Add sold out stickers
    '''
    message5 = display_message('You have selected to add sold out stickers')
    message5.color()

    sold_out_list()
    search_menu()
    sys.stdout.write('Please add sold out stickers' + '\n')
    # Use strip and split methods to remove space and comma. 
    stickername = str(sys.stdin.readline().strip())
    stickername_list = stickername.split(',')
    # For loop to check whether the sticker is in menu or not. 
    # If yes, update the sold out list. If not, let customer know.
    sold_out_sticker_list = []
    for x in stickername_list:
        sold_out_stickers = x.strip()
        if sold_out_stickers in menu:
            sold_out_sticker_list.append(sold_out_stickers)
        else:
            sys.stdout.write(str(sold_out_stickers) + ' ' + 'will not be added' + '\n')
    final_sold_out_stickers_list = sold_out_sticker_list
    with open('sold_out_list.json', 'w', encoding='utf8') as sold_out:
            json.dump(final_sold_out_stickers_list, sold_out)
            
    return final_sold_out_stickers_list
 

def search_menu():
    '''Retrieve menu items
    '''
    global menu
    with open('Menu.json', 'rb') as menu_list:
        menu = json.load(menu_list)


def sold_out_list():
    '''Retrieve sold out items
    '''
    global sold_out_sticker_list
    with open('Sold_out_list.json', 'rb') as sold_out:
        sold_out_sticker_list = json.load(sold_out)
        