#C0ded by Pr1m1t1ve - Evil Dwells Here - https://hackforums.net/member.php?action=profile&uid=4033779
#TODO: DNS, NoSQLi, Header Injection, PHP recon.

import attack as pew
import recons
import tools as tl
import socket
from os import system
import paramiko

banner = '''\033[92m
██████╗ ██████╗  ██╗███╗   ███╗ ██╗████████╗ ██╗██╗   ██╗███████╗
██╔══██╗██╔══██╗███║████╗ ████║███║╚══██╔══╝███║██║   ██║██╔════╝
██████╔╝██████╔╝╚██║██╔████╔██║╚██║   ██║   ╚██║██║   ██║█████╗  
██╔═══╝ ██╔══██╗ ██║██║╚██╔╝██║ ██║   ██║    ██║╚██╗ ██╔╝██╔══╝  
██║     ██║  ██║ ██║██║ ╚═╝ ██║ ██║   ██║    ██║ ╚████╔╝ ███████╗
╚═╝     ╚═╝  ╚═╝ ╚═╝╚═╝     ╚═╝ ╚═╝   ╚═╝    ╚═╝  ╚═══╝  ╚══════╝
_________________________________________________________________\033[31m

-_-_-_-_-_-_-_-_-_-Pr1m1t1ves Attack Platform-_-_-_-_-_-_-_-_-_-
_________________________________________________________________                                                             
\n\n\n'''

mainMenu = ["1. Reconnaissance", "2. Attack Platform", "3. Useful Tools", "4. SearchSploit", "5. Print Disclaimer"]
disclaimer = "This tool was not made for use in illegal ways.\nTherefore I am not responsible for how you use this tool.\nI also do not own all the tools included in this kit."

def moduleload(arg):
    from recons import recon

attack = pew.attack()
tools = tl.tools()
recon = recons.recon()
def searchsploit():
    print("Coming Soon")
    return

def main():
    system('clear')
    print(banner)
    for x in range(len(mainMenu)):
        print (mainMenu[x])

    getInput = int(input("\n\033[31m[+]\033[36m What would you like to do? "))

    if getInput == 1:
        recon.reconMenu()
    elif getInput == 2:
        pew.attackplat()
    elif getInput == 3:
        tools.toolMenu()
    elif getInput == 4:
        searchsploit()
    elif getInput == 5:
        print(disclaimer)
        main()
    else:
        system('clear')
        print(banner)
        print("Use the correct syntax please.")


main()
