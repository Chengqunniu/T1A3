import json
import sys


def add_update():
    '''Convert the input into a dictionary and update current dictionary for menu. Input should be the correct format.
    '''  
    search_menu()
    string = str(input('Please enter the new stickers and prices with the following format: sticker_1 : price_1, sticker_2: price_2\n').strip())
    string_list = string.split(',')  
    new_menu_list = []
    # For loop to update the stickers and prices
    for x in string_list:  #obtain each sticker and their cost as a single string
        change_list = x.split(':')     
         # Remove space for each string, then form a list. Later use for loop to go though the list and update the menu and price.
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
    with open('Menu.json', 'w') as menu_list:
        json.dump(menu, menu_list)
        
def search_menu():
    global menu
    with open('Menu.json', 'rb') as menu_list:
        menu = json.load(menu_list)