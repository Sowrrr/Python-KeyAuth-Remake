from keyauth import api

import sys
import time
import os
import hashlib
from time import sleep
from datetime import datetime
from colorama import Fore
from pystyle import *
import getpass


# FORE COLORS
w = Fore.LIGHTWHITE_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
b = Fore.LIGHTBLUE_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
black = Fore.LIGHTBLACK_EX




#DEFS

def slow_print(msg):
    for char in msg:
        print(char, end='', flush=True)
        time.sleep(0.5/20)

    
    print()



def getchecksum():
    md5_hash = hashlib.md5()
    file = open(''.join(sys.argv), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest

user = os.getlogin()


# NIGGER.NIGGER.BAT

os.system(f"title  Python Keyauth Remake by sowrrr#3097")
os.system('cls')
slow_print(f"{m}[{y}+{m}] {black}Press any key to continue: ")
os.system("pause >nul")
os.system('cls')
os.system(f"title Python Keyauth Remake by sowrrr#3097 ")
          

os.system('cls')


# KEYAUTHAPP
keyauthapp = api(
    name = "",
    ownerid = "",
    secret = "",
    version = "",
    hash_to_check = getchecksum()
)

slow_print(f"{m}[{y}+{m}] {black}Initializing...")
time.sleep(1)

os.system(f"title Python Keyauth Remake by sowrrr#3097 ^|  Users: {keyauthapp.app_data.onlineUsers}  ^|  Version {keyauthapp.app_data.app_ver}")



print()
slow_print(f"{m}[{y}+{m}] {black}Current Session Validation Status: {keyauthapp.check()}")
slow_print(f"{m}[{y}+{m}] {black}Blacklisted? : {keyauthapp.checkblacklist()}")
os.system('cls')





def answer():
    try:
        slow_print(f"""
 {m}[{y}1{m}] {black}Login
 {m}[{y}2{m}] {black}Register
 {m}[{y}3{m}] {black}License Key Only
        """)
        ans = input(f" {m}[{m}{y}>>>{y}{m}]{m} {black}Select Option:{y} ")
        if ans == "1":
            os.system('cls')
            
            user = input(f'\n{m}[{m}{y}?{y}{m}]{m} {black} Provide username:{y} ')
            print()
            password = getpass.getpass(f'{m}[{m}{y}?{y}{m}]{m} {black} Provide password:{y} ')
            os.system('cls')
            keyauthapp.login(user, password)
        elif ans == "2":
            os.system('cls')
            user = input(f'{m}[{m}{y}?{y}{m}]{m} {black} Provide username:{y} ')
            password = input(f'{m}[{m}{y}?{y}{m}]{m} {black} Provide password:{y} ')
            os.system('cls')
            license = input(f' {m}[{m}{y}?{y}{m}]{m} {black} Provide License:{y} ')
            keyauthapp.register(user, password, license)
        elif ans == "3":
            os.system('cls')
            key = input(f'{m}[{m}{y}?{y}{m}]{m} {black}Enter your license:{y} ')
            keyauthapp.license(key)
            os.system('cls')
        else:
            slow_print(f"\n{m}[{m}{y}x{y}{m}]{m} {black}Not Valid Option")
            time.sleep(1)
            os.system('cls')
            answer()
    except KeyboardInterrupt:
        os._exit(1)


answer()

def choices():
    while True:
        slow_print(f"{m}[{m}{y}1{y}{m}]{m}{black} Cleaner")
        slow_print(f"{m}[{m}{y}2{y}{m}]{m}{black} Spoof")
        slow_print(f"{m}[{m}{y}3{y}{m}]{m}{black} Check Serials\n")

        choice = input(f"{m}[{y}>>>{m}] {black}Select option: ")

        os.system('cls')
        if choice == "1": 

            slow_print(f"{m}[{m}{y}+{y}{m}]{m} {black}Press enter for clean\n")   # CLEANER
            os.system('pause')
            slow_print(f"{m}[{m}{y}!{y}{m}]{m} {black}Cleaning...\n")   # CLEANER
            #bytes = keyauthapp.file("")
            #f = open("example.exe", "wb")
            #f.write(bytes)
            #f.close()
            slow_print(f"{m}[{m}{y}+{y}{m}]{m} {g}Cleaned! ") # SPOOFED
            time.sleep(4)
            os.system('cls')

        elif choice == "2":
            slow_print(f"{m}[{m}{y}+{y}{m}]{m} {black}Press enter for spoof \n") # SPOOF
            os.system('pause')
            slow_print(f"{m}[{m}{y}!{y}{m}]{m} {black}Spoofing...\n")   # CLEANER
            #bytes = keyauthapp.file("")
            #f = open("example.exe", "wb")
            #f.write(bytes)
            #f.close()
            slow_print(f"{m}[{m}{y}+{y}{m}]{m} {g}Spoofed! ") # SPOOFED
            time.sleep(4)
            os.system('cls')


        elif choice == "3":
            slow_print(f"{m}[{m}{y}+{y}{m}]{m} {black}Press enter for check your serials\n") # CHECKER
            os.system("pause >nul")
            os.system("cls")

        while(True):
            os.system("cls")
            slow_print(f"{m}[{m}{y}</>{y}{m}] {black}Baseboard\n{y}")
            os.system(f"wmic baseboard get serialnumber")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}Mac\n{y}")
            os.system(f"""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}CPU\n{y}")
            os.system(f"wmic cpu get processorid")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}GPU\n{y}")
            os.system(f"wmic PATH Win32_VideoController GET Description,PNPDeviceID")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}DISK DRIVE\n{y}")
            os.system(f"wmic diskdrive get serialnumber")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}MotherBoard\n{y}")
            os.system(f"wmic baseboard get serialnumber")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}RAM\n{y}")
            os.system(f"wmic memorychip get serialnumber")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}Bios\n{y}")
            os.system(f"wmic bios get serialnumber")
            slow_print(f"{m}[{m}{y}</>{y}{m}]{m} {black}smBios\n{y}")
            os.system(f"wmic csproduct get uuid")



            os.system("pause >nul")

choices()

os.system("cls")
