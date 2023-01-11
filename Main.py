import os

from pystyle import *

import json

from rich import print_json

import getpass

from elevate import elevate

from time import sleep

from colorama import *

import errors ## official Assembly errors file for Windows

from subprocess import Popen, PIPE



## elevate()





username = getpass.getuser()



user_directory_path = f'C:/Users/{username}'




os.system('cls')



done = False




banner = '''

     ___                             __    __    
    /   |  _____________  ____ ___  / /_  / /_  __
   / /| | / ___/ ___/ _ \/ __ `__ \/ __ \/ / / / /
  / ___ |(__  |__  )  __/ / / / / / /_/ / / /_/ /
 /_/  |_/____/____/\___/_/ /_/ /_/_.___/_/\__, /  
                                         /____/  



'''



print(Colorate.Color(Colors.purple, banner, True))




print(Colorate.Color(Colors.green, ' reading "config.json"...\n'))




setup_type = open('config.json')



config = json.load(setup_type)




if config["setup_type"] == 'full':

    print_json(data=config)

    print('')