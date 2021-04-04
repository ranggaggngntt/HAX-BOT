from lib.Dorker.grab import Dorker

def main():

    print('''
    1. Grab Domain
    2. Grab IP
    ''')
    choice = input('Choice: ')
    file = input('Dork: ')
    thread_count = int(input('Thread: '))

    with open(file, 'r') as f:
        dorks = f.read().splitlines()

    runner = Dorker(thread_count, choice, dorks)
    runner.run()