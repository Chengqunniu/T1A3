import json
from art import text2art
from class_for_text import text, display_message
from display_options import welcome_page

def check_password():
    '''Check password
    '''
    password = input('Enter your password:')
    with open('Password.json', 'rb') as file:
        customer_password = json.load(file)
    correct = True
    while correct:
        if password == customer_password:
            correct = False
        else:
            password = input('Enter your password again:')

    return correct

def main():
    '''Main program
    '''
    welcome_messages = text2art('SmoonyPaws', font='dancingfont')
    message = display_message(welcome_messages)
    press_enter = text('Press enter to continue...')

    #print welcome message and text content
    message.color()
    press_enter.color_input()
    welcome_page()

if __name__ == '__main__':
    check_password()
    main()
