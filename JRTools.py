import time
import os
import requests
import sys
from pystyle import Colors, Colorate , Write, Colors
os.system(f'cls & mode 95,30 & title JRTools')


def main():
    menu()


def menu():
    choice = Write.Input("""
         ▄█    ▄████████     ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
    ███   ███    ███ ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
    ███   ███    ███    ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
    ███  ▄███▄▄▄▄██▀     ███   ▀ ███    ███ ███    ███ ███         ███        
    ███ ▀▀███▀▀▀▀▀       ███     ███    ███ ███    ███ ███       ▀███████████ 
    ███ ▀███████████     ███     ███    ███ ███    ███ ███                ███ 
    ███   ███    ███     ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
█▄ ▄███   ███    ███    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
▀▀▀▀▀▀    ███    ███                                   ▀                      
                          Made By Jose#0001                       
                          [1] Check Single Roblox Cookie
                          [2] Proxy Scraper
                          [3] Check Multi Roblox Cookie
                          [4] Exit
                          Enter A Option -> """, Colors.purple_to_red, interval=0.0)
    if choice == "1":
        single()
    elif choice == "2":
        scrape()
    elif choice == "3":
        multi()
    elif choice == "4":
       sys.exit
    else:
        print("Enter Right Choice")
        time.sleep(3)
        os.system('cls')
        menu()





def single():
    cookie = Write.Input('Enter Roblox Cookie ->', Colors.purple_to_red, interval=0.00)
    check = requests.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookie)})
    if check.status_code == 200:
        print(Colorate.Horizontal(Colors.yellow_to_green, "Roblox Cookie Is Valid", 1))
        time.sleep(2)
        print(Colorate.Horizontal(Colors.purple_to_red, "Your Going Back To The Menu", 1))
        time.sleep(2)
        os.system('cls')
        menu()
    elif check.status_code == 404:
        print(Colorate.Horizontal(Colors.purple_to_blue, "Roblox Cookie Is Banned", 1))
        time.sleep(2)
        print(Colorate.Horizontal(Colors.purple_to_red, "Your Going Back To The Menu", 1))
        time.sleep(2)
        os.system('cls')
        menu()

    else:
         print(Colorate.Horizontal(Colors.yellow_to_red, "Roblox Cookie Is Invalid", 1))
         time.sleep(2)
         print(Colorate.Horizontal(Colors.purple_to_red, "Your Going Back To The Menu", 1))
         time.sleep(2)
         os.system('cls')
         menu()

def multi():
    choice = Write.Input('Would You Like To Use Proxies Y/N ->', Colors.purple_to_red, interval=0.00)
    if choice == "Y":
        name = Write.Input('Enter The File Directory Of Txt File Where The Roblox Cookies Are Saved ->', Colors.purple_to_red, interval=0.00)
        file = open(name, "r").read().split('\n')
        proxies = open('proxies.txt', 'r').read().split('\n')
        Valid = open('Valid.txt', 'w')
        Invalid = open('Invalid.txt', 'w')
        for line in file:
         cookies = line.strip("\n")
         check = requests.get(f'https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookies)},proxies={'http' : 'http://' + 'proxy'})
         if check.status_code == 200:
            print(Colorate.Horizontal(Colors.yellow_to_green, "{} Roblox Cookie Is Valid.".format(line.strip("\n"))))
            Valid.write(f'{line}\n')                   
         else:
            print(Colorate.Horizontal(Colors.yellow_to_red, "{} Roblox Cookie Is Invalid.".format(line.strip("\n"))))
            Invalid.write(f'{line}\n')
        
        
    elif choice == "N":
        name = Write.Input('Enter The File Directory Of Txt File Where The Roblox Cookies Are Saved ->', Colors.purple_to_red, interval=0.00)
        file = open(name, "r").read().split('\n')
        Valid = open('Valid.txt', 'w')
        Invalid = open('Invalid.txt', 'w')
        for line in file:
         cookies = line.strip("\n")
         check = requests.get(f'https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(cookies)})
         if check.status_code == 200:
            print(Colorate.Horizontal(Colors.yellow_to_green, "{} Roblox Cookie Is Valid.".format(line.strip("\n"))))
            time.sleep(2)
            Valid.write(f'{line}\n')                   
         else:
            print(Colorate.Horizontal(Colors.yellow_to_red, "{} Roblox Cookie Is Invalid.".format(line.strip("\n"))))
            time.sleep(2)
            Invalid.write(f'{line}\n')
def scrape():

    url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'
    r = requests.get(url)
    results = r.text
    with open('Proxies.txt', 'w') as file:
        file.write(results)
        print(Colorate.Horizontal(Colors.yellow_to_green, "Proxies Scraped SucessFully", 1))
        time.sleep(3)
        print(Colorate.Horizontal(Colors.purple_to_red, "Your Going Back To The Menu", 1))
        time.sleep(3)
        os.system('cls')
        menu()



menu()