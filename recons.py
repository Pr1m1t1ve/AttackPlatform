#C0ded by Pr1m1t1ve - Evil Dwells Here - https://hackforums.net/member.php?action=profile&uid=4033779
import os
import socket
from queue import Queue
import time
import http.client
import sys
from os import system


reconList = ["1. Host to IP", "2. Banner Grabber", "3. HTTP Header Grabber"]

banner = """
 ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █ 
▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ 
▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒
▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒
░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░
░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░ ░ ░  ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░
  ░░   ░    ░   ░        ░ ░ ░ ▒     ░   ░ ░ 
   ░        ░  ░░ ░          ░ ░           ░ 
                ░                            
    """

class recon():
    def hostName(self):
        host = input("\n\033[31m[+]\033[36m URL: ")
        IP = socket.getaddrinfo(host, 80, 0, 0, socket.IPPROTO_TCP)
        for x in range(len(IP)):
            print(IP[x])
        input("\033[31m[+]\033[36m Press enter to continue ")

        return

    def bannerPull(self):
        host = input("\033[31m[+]\033[36m IP Address: ")
        port = input("\033[31m[+]\033[36m Port: ")
        s = socket.socket()
        s.settimeout(10)
        s.connect((host,port))
        banners = s.recv(1024)
        print(banners)
        input("\033[31m[+]\033[36m Press enter to continue ")
        return

    def headerGrab(self):
        host = input("\033[31m[+]\033[36m Target: ")
        conn = http.client.HTTPConnection(host)
        conn.request("GET", "/")
        r1 = conn.getresponse()
        print(r1.getheaders())
        input("\033[31m[+]\033[36m Press enter to continue ")
        return


    def reconMenu(self):
        system('clear')
        print(banner)
        for x in range(len(reconList)):
         print(reconList[x])

        habib = int(input("\033[31m[+]\033[36m Choose your tool: "))

        if habib == 1:
            system('clear')
            print(banner)
            recon.hostName(self)
        elif habib == 2:
            system('clear')
            print(banner)
            recon.bannerPull(self)
        elif habib == 3:
            system('clear')
            print(banner)
            recon.headerGrab(self)
        else:
            system('clear')
            print(banner)
            print("Use the correct syntax please.")
        return
