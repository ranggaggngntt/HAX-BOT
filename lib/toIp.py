from lib.Convert.getIp import Converter
def main():
    file = input('File Web: ')
    thread = int(input('Thread: '))
    with open(file, 'r') as f:
        web = f.read().split('\n')
    Converter(web, thread).run()