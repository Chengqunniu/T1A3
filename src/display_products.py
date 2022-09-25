import json
from rich.console import Console
from rich.table import Table
from class_for_text import display_message


def display_products():
    '''Display all products'''
    
    message6 = display_message('You have selected to display all products')
    message6.color()
    table = Table(title='This is the product list', 
                 title_style = 'bold red', show_lines=True)

    table.add_column('Products', style='green')
    table.add_column('Price', style='yellow', no_wrap=True)
    table.add_column('Sold out', style='yellow', no_wrap=True)
    
    with open('Menu.json', 'rb') as menu_list:
        menu = json.load(menu_list)
    with open('sold_out_list.json', 'rb') as sold_out:
        sold_out_sticker_list = json.load(sold_out)
    for key, value in menu.items():
        if key not in sold_out_sticker_list:
            table.add_row(key, str(value), '❌')
        else:
            table.add_row(key, str(value), '✅')


    console = Console()
    console.print(table)
