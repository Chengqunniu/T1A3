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

    sys.stdout.write('Please select customer group: 1 for non-rewards customer, 2 for rewards customer'+'\n')
    valid = True
    while valid:
        number = sys.stdin.readline().strip()
        if number == 1:
            for name in customer_list:
                if name not in rewards_customer_list:
                    table.add_row(name, '❌')
        elif number ==2:
            for name in rewards_customer_list:
                table.add_row(name, '✅')
        else:
            sys.stdout.write('Please enter a valid number')


    console = Console()
    console.print(table)

customer_info()
