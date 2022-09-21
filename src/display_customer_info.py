import sys
import json
from rich import print as rprint
from rich.console import Console
from rich.table import Table


def customer_info():
    '''Display customer information as a table
    '''
    rprint('SmoonyPaws')

    table = Table(title='Customer Information', show_lines=True)

    table.add_column('Name', style='cyan', no_wrap=True, )
    table.add_column('Rewards Customer', justify='center')

    with open('Customer_list.json', 'rb') as customer:
        customer_list = json.load(customer)
    with open('Rewards_customer_list.json', 'rb') as rewards_customer:
        rewards_customer_list = json.load(rewards_customer)

    number = input('Please select customer group: 1 for non-rewards customer, 2 for rewards customer'+'\n').strip()
    valid = True
    while valid:
        try:
            number = int(number)
            if number == 1:
                for name in customer_list:
                    if name not in rewards_customer_list:
                        table.add_row(name, '❌')
                        valid = False
            elif number == 2:
                for name in rewards_customer_list:
                    table.add_row(name, '✅')
                    valid = False
            else:
                number = input('Please enter a valid number' + '\n').strip()
        except ValueError:
            number = input('Please enter a valid number' + '\n').strip()


    console = Console()
    console.print(table)

