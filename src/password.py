import json
import click
from class_for_text import text


@click.command()
@click.option(
    "--password", prompt=True, hide_input=True,
    confirmation_prompt=True
)


def encode(password):
    '''Create a new password'''
    system_password = password
    with open('Password.json', 'w', encoding = 'utf8') as file:
        json.dump(system_password, file)

MESSAGE= 'Please enter your password'
password_message = text(MESSAGE)
password_message.color()

encode()