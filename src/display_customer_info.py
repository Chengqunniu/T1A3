import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from class_for_text import display_message


def customer_info():
    '''Display customer information as a table'''
    message2 = display_message('You have selected to display the customer information')
    message2.color()
    
    table = Table(title='Customer Information', title_style='yellow', show_lines=True)

    table.add_column('Name', style='cyan', no_wrap=True, )
    table.add_column('Rewards Customer', justify='center')

    with open('Customer_list.json', 'rb') as customer:
        customer_list = json.load(customer)
    with open('Rewards_customer_list.json', 'rb') as rewards_customer:
        rewards_customer_list = json.load(rewards_customer)

    number = input('Please select customer group: '
                   '1 for non-rewards customer, 2 for rewards customer'+'\n').strip()
    valid = True
    while valid:
        try:
            number = int(number)
            if number == 1:
                if customer_list == rewards_customer_list:
                    print('All customers are rewards customers')
                    break
                else:
                    for name in customer_list:
                        if name not in rewards_customer_list:
                            table.add_row(name, '❌')
                            valid = False
            elif number == 2:
                if rewards_customer_list == []:
                    print('All customers are non-rewards customers')
                    break
                else:
                    for name in rewards_customer_list:
                        table.add_row(name, '✅')
                        valid = False
            else:
                number = input('Please enter a valid number: ').strip()
        except ValueError:
            number = Prompt.ask('Please enter a valid number').strip()


    console = Console()
    console.print(table)

