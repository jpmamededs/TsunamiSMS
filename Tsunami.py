import os
import time
from termcolor import colored
import requests
import sys

os.system('cls')

print(colored("""


⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠿⠛⠉⠁⠀⢰⡇⠉⠛⠿⣦⡀⠀⠀⠀⠀⠀            by @jpmamededs
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠋⢀⡀⠀⢀⣠⣤⣿⣷⣴⣷⡀⠹⣿⡄⠀⠀⠀            
⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠁⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠞⠛⢿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣤⡾⠋⠀⠀⠀⠀⠹⣿⡟⢻⠏⣾⠃⡿⠋⣹⣿⣤⣶⣦⣤⡿⢿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡶⠶⠟⠋⠁⣀⡀⠀⠀⠀⠀⠀⠈⠻⣾⣠⣇⣼⢁⡞⢉⣿⣿⣿⣿⡏⢰⣿⣿⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⣿⠟⢷⡄⠀⢠⣶⡶⢀⣿⣿⣿⣷⣾⠁⣾⠋⠀⠀⠙⢿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴
⠀⣴⣶⣶⣦⣄⣹⣿⣟⠻⣆⠘⣿⣿⣿⣿⣿⣿⡿⣿⠀⣿⠀⠀⠀⠿⢸⣿⣯⣴⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁
⢸⣿⣿⣿⣿⣿⡟⢻⣿⣿⣿⣶⣤⣽⣿⣿⣿⣿⣧⠸⣧⣿⡄⠀⠀⠀⣈⣉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⣠
⠘⣿⣿⡿⢿⣿⣿⣦⠻⣟⠻⣿⣿⣿⡿⠟⠉⠉⠙⠳⣿⣿⣿⣄⠀⠀⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠁⠀⠀⣴⣯
⠀⠘⢿⣷⣼⣿⣿⣿⣷⣾⣷⣿⠿⠋⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣷⣄⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠋⠁⠀⣠⣴⣿⣷⣤
⠀⠀⠀⠙⠿⢿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠉⠻⢿⣿⣶⣤⣤⣀⣀⣀⣀⣀⣤⣤⣶⠿⠛⣁⣀⣀⡴⠿⢿⣿⡿⢋⣡
▄▄▄█████▓  ██████  █    ██  ███▄    █  ▄▄▄       ███▄ ▄███▓ ██▓   
▓  ██▒ ▓▒▒██    ▒  ██  ▓██▒ ██ ▀█   █ ▒████▄    ▓██▒▀█▀ ██▒▓██▒   
▒ ▓██░ ▒░░ ▓██▄   ▓██  ▒██░▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒██▒   
░ ▓██▓ ░   ▒   ██▒▓▓█  ░██░▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██    ▒██ ░██░   
  ▒██▒ ░ ▒██████▒▒▒▒█████▓ ▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░██░   
  ▒ ░░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░▓     
    ░    ░ ░▒  ░ ░░░▒░ ░ ░ ░ ░░   ░ ▒░  ▒   ▒▒ ░░  ░      ░ ▒ ░   
  ░      ░  ░  ░   ░░░ ░ ░    ░   ░ ░   ░   ▒   ░      ░    ▒ ░   
               ░     ░              ░       ░  ░       ░    ░     
                                                                  
      """, 'blue'))

time.sleep(2)

def opt_menu(): 
    print(colored("""

OPTIONS <------------------>           

1) Send SMS wave
2) Help
3) Follow me on LinkedIn
      
<-------------------------->

""", 'blue')) 
    
opt_menu()
    
options = int(input("\nSelect an option: "))

if options == 1:
    targetnumber = input("Insert the targets number: ")
    message = input("Input the message you want to send: ")
    times_to_send = int(input("How many times do you want to send the message? -> "))


    for i in range(times_to_send) :
        resp = requests.post('https://textbelt.com/text', {
        'phone': f'{targetnumber}',
        'message': f'{message}',
        'key': 'textbelt',
        })
        print(resp.json())

    time.sleep(2)

elif options == 2:
    print('Currently, you will need to see the documentation in the TSUNAMI GitHub repository.')

elif options == 3:
    print(colored("""

        
 _    _  _     _  ___________  _  _     
/ \  / \/ \  // |/ /  __/  _ \/ \/ \  /|
| |  | || |\ ||   /|  \ | | \|| || |\ ||
| |_/\ || | \||   \|  /_| |_/|| || | \||
\____|_/\_/  \\_|\_\____\____/\_/\_/  \|
                                                                                                   
https://www.linkedin.com/in/jpmamededs/                                                      
""", 'blue'))