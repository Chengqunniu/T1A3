import sys
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from class_for_customer import Customer
from class_for_text import display_message

def check_history():
    '''
    Check customer order history
    '''
    global customer_name

    message3 = display_message('You have selected to display the customer order history')
    message3.color()

    sys.stdout.write('Please enter a customer name '
                    'for checking order history:' + '\n')
    name = sys.stdin.readline().strip()
    customer_name= Customer(name)
    customer_list = customer_name.search_customer()
    Valid_customer_name = True
    # While loop to check whether the customer name entered is in the system.
    # If not, the loop will repeat.
    while Valid_customer_name:   
        try:
            name = float(name)
            name = str(input('Pleaase enter '
                      'the customer name again' + '\n').strip())     
        except ValueError:
            if name not in customer_list:
                name = str(input('Pleaase enter'
                          'the customer name again' + '\n').strip())          
            else:
                Valid_customer_name = False  
    index_of_customer = customer_list.index(name)
    # If loop to display customer order history.
    # If order history is empty, it will display the sentence
    # to let customer know that they have no order history.
    # If not, it will print the order history.
    customer_order_history = customer_name.search_order_history()
    if customer_order_history[index_of_customer] == []:
        print('The customer has no order history')
    else:
        rprint('Customer order history')

        table = Table(title='This is the order history of' + ' '
                     + str(name), title_style = 'bold red', show_lines=True)

        table.add_column('Orders', style='green')
        table.add_column('Stickers', style='yellow', no_wrap=True)
        table.add_column('Total Cost', style='yellow', justify='right')
            
        for x, y in enumerate (customer_order_history[index_of_customer]):
            for key, value in y.items():
                table.add_row(str(x+1), key, value)

        console = Console()
        console.print(table)
