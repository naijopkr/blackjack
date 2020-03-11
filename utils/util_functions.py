from sys import platform
from os import system

def clear():
    """ Clears console """

    if platform == 'win32':
        system('cls')
    else:
        system('clear')
