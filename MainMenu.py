#!/usr/bin/env python


#imports

import os, pygame, sys, random
import easygui
import random
from pygame.locals import *

#globals
GAMES_LIST = []

    

def gamemenu():
    os.system("ls games > gamesList.txt")
    os.system("ls /usr/local/bin/indiecity/installedapps/pisnes/full/roms > romsList.txt")

    global GAMES_LIST
    global ROMS_LIST
    GAMES_LIST = [line.lower().strip() for line in open('gamesList.txt')]
    ROMS_LIST = [line.lower().strip() for line in open('romsList.txt')]
    resolution = [640, 480]
    msg = "Welcome to the python portable game console."
    buttons = GAMES_LIST
    picture = None
    while True:
          title = "Enjoy your game!"
          selection = easygui.buttonbox(msg, title, buttons, picture)
          for game in GAMES_LIST:
              selection == game
              execfile("/home/pi/pythongameproject/games/" +selection +"/" +selection)
          for game in ROMS_LIST:
              selection == game
              os.system("./usr/local/bin/indiecity/installedapps/pisnes/full" +selection)
   

if __name__ == '__main__':
   gamemenu()
