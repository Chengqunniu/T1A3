import sys
import json
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from class_for_customer import Customer

def check_history():
    '''
    Check customer order history
    '''
    global customer_name
    sys.stdout.write('Please enter a customer name for checking order history:' + '\n')
    name = sys.stdin.readline().strip()
    customer_name= Customer(name)
    customer_list = customer_name.search_customer()
    Valid_customer_name = True
    # While loop to check whether the customer name entered is in the system. If not, the loop will repeat. 
    while Valid_customer_name:
        if name not in customer_list:
            sys.stdout.write('Pleaase enter the customer name again' + '\n')
            name = str(sys.stdin.readline().strip())
        else:
            Valid_customer_name = False  
    index_of_customer = customer_list.index(name)
    # If loop to display customer order history. If order history is empty, it will display the sentence to let customer know that they have no order history. If not, it will print the order history.
    customer_order_history = customer_name.search_order_history()
    if customer_order_history[index_of_customer] == []:
        sys.stdout.write('The customer has no order history' + '\n')
    else:
        rprint('Customer order history')

        table = Table(title='This is the order history of' + ' ' + str(name), title_style = 'bold red', show_lines=True)

        table.add_column('Orders', style='green')
        table.add_column('Stickers', style='yellow', no_wrap=True)
        table.add_column('Total Cost', style='yellow', justify='right')
            
        for x, y in enumerate (customer_order_history[index_of_customer]):
            for key, value in y.items():
                table.add_row(str(x+1), key, value)

        console = Console()
        console.print(table)
