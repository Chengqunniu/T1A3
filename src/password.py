import click
from class_for_text import text

@click.command()
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True
)
def encode(password):
    '''create a new password
    '''
    system_password = password
    with open('password.txt', 'w', encoding='utf8') as file:
        file.write(system_password)

MESSAGE= 'Please enter your password'
password_message = text(MESSAGE)
password_message.color()

encode()