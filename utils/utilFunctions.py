from sys import exit, platform
from os import system

def clear():
    if platform == 'win32':
        system('cls')
    else:
        system('clear')

def exit_game():
    exit(0)
