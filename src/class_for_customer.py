import sys


class Customer:

    def __init__(self, name):
        self.name = name

    def order(self):
        global sticker
        global order

        order = []
        sys.stdout.write('Enter the sticker name [Enter a valid sticker only, e.g. Yum Yum Hana]:\n')
        sticker = str(sys.stdin.readline().strip())
        # While loop to check whether the input dish name is in the Menu. If not in the Menu, then the while loop will keep looping.
        while sticker not in menu:   
            sys.stdout.write('Please enter a valid sticker name:'+ '\n')
            sticker = str(sys.stdin.readline().strip())