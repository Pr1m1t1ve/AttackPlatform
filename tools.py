#C0ded by Pr1m1t1ve - Evil Dwells Here - https://hackforums.net/member.php?action=profile&uid=4033779
import os
from os import system

banner = """
  dBBBBBBP dBBBBP dBBBBP dBP .dBBBBP
          dBP.BP dBP.BP      BP     
   dBP   dBP.BP dBP.BP dBP   `BBBBb 
  dBP   dBP.BP dBP.BP dBP       dBP 
 dBP   dBBBBP dBBBBP dBBBBPdBBBBP' 
___________________________________
      
      Tools (By god creators)
___________________________________
 """
toolsMenu = ["1. Nmap", "2. Nikto"]

class tools():

    def nmapTool(self):
        print(banner)
        host = input("\033[31m[+]\033[36m Enter Host Address: ")
        port = input("\033[31m[+]\033[36m What port mofo(range x-y)? ")
        system('nmap -A -v -Pn ' + host + ' -p' + port)
        if KeyboardInterrupt:
            exit("Lilbitch")

    def niktoTool(self):
        print(banner)
        host = input("\033[31m[+] \033[36mEnter Nikto's Target: ")
        ssl = bool(input("\033[31m[+]\033[36m Yall want SSL(True | False): "))
        if ssl == True:
            system('clear')
            print(banner)
            system('nikto -host ' + host + ' -ssl')
        else:
            system('clear')
            print(banner)
            system('nikto -host ' + host)

    def toolMenu(self):
        system('clear')
        print(banner)
        for x in range(len(toolsMenu)):
            print(toolsMenu[x])

        getInput = int(input("\033[36m[+]\033[31m Which OG tool you want? "))

        if getInput == 1:
            system('clear')
            tools.nmapTool(self)
        elif getInput == 2:
            system('clear')
            tools.niktoTool(self)
        else:
            system('clear')
            print(banner)
            print("Use the correct syntax please.")
