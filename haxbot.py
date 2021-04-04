import os
import platform
from lib import reverseIP
from lib import scanner
from lib import smtp
from lib import dorker
from lib import RemoveDuplicate
from lib import RemoveSubdomain
from lib import toIp
from time import sleep
def banner():
    banner = '''
         _    _             __   __           ____     ____    _______ 
        | |  | |     /\     \ \ / /          |  _ \   / __ \  |__   __|
        | |__| |    /  \     \ V /   ______  | |_) | | |  | |    | |   
        |  __  |   / /\ \     > <   |______| |  _ <  | |  | |    | |   
        | |  | |  / ____ \   / . \           | |_) | | |__| |    | |   
        |_|  |_| /_/    \_\ /_/ \_\          |____/   \____/     |_|   
                                                                
    * Recode boleh tapi jgn ganti author doang plerrrr
    
    Github      : https://github.com/ranggaggngntt/
    Facebook    : https://facebook.com/Rangga.Haxor/
    '''
    return print(banner)

def option():
    option = '''
1. Reverse-Ip From HT (Must be IpList)          5. Remove Duplicate
2. Laravel Scanner                              6. Remove Subdomain
3. Laravel get SMTP,AWS,TWILIO,Shell,dll        7. Domain to IP
4. Bing Dorker
    '''
    return print(option)

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

def main():
    banner()
    sleep(1)
    option()
    choice = input('No : ')
    if choice == '1':
        clear()
        reverseIP.main()
    elif choice == '2':
        clear()
        scanner.main()
    elif choice == '3':
        clear()
        smtp.main()
    elif choice == '4':
        clear()
        dorker.main()
    elif choice == '5':
        clear()
        RemoveDuplicate.main()
    elif choice == '6':
        clear()
        RemoveSubdomain.main()
    elif choice == '7':
        clear()
        toIp.main()
if __name__ == '__main__':
    main()