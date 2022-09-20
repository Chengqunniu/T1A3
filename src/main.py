from art import text2art
from class_for_text import text, display_message
from display_options import welcome_page


def main():
    welcome_messages = text2art('SmoonyPaws', font='dancingfont')
    message = display_message(welcome_messages)
    press_enter = text('Press enter to continue...')

    #print welcome message and text content
    message.color()
    press_enter.color_input()
    welcome_page()

if __name__ == '__main__':
    main()
