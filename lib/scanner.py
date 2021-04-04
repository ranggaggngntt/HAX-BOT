from lib.Scan.cms_scanner import Scanner
import requests
from lib.Scan.laravel_scanner import LaravelScanner

def main():

    print('''
    1. Wp Scanner
    2. Laravel Scanner
    ''')
    choice = input('No: ')
    file = input('File: ')
    thread = input('Thread: ')

    with open(file, 'r') as f:
        web = f.read().split('\n')

    temp = []

    for i in web:
        if i.endswith('/'):
            temp.append(i.strip('/'))
        else:
            temp.append(i)
            
    temp = list(set(temp))

    if choice == '1':
        Scanner(temp, int(thread)).run()
    elif choice == '2':
        LaravelScanner(temp, int(thread)).run()
    else:
        print('Wrong Choice!')
        exit()