import json
import sys


def search_menu():
    global menu
    with open('Menu.json', 'rb') as menu_list:
        menu = json.load(menu_list)