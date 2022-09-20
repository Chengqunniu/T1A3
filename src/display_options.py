import sys
from class_for_text import text


press_enter = text('Press enter to continue...')
message2 = text('Welcome to the Smoonypaws ordering system!' )

def welcome_page():
    '''Welcome page for the system
    '''
    # sys.stdout.write('Welcome to the Smoonypaws ordering system!' + '\n')
    message2.color()
    print()
    sys.stdout.write('#'* 40)