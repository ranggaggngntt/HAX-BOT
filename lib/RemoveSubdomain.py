from lib.Remove.getdomain import getHost
def main():
    file = input('File: ')
    thread = int(input('Thread: '))
    temp = []
    with open(file, 'r') as f:
        web = f.read().splitlines()
    for i in web:
        if i.startswith('cpanel.'):
            z = i.replace('cpanel.', '')
            temp.append(z)
        elif i.startswith('mail.'):
            z = i.replace('mail.', '')
            temp.append(z)
        elif i.startswith('autodiscover.'):
            z = i.replace('autodiscover.', '')
            temp.append(z)
        elif i.startswith('webdisk.'):
            z = i.replace('webdisk.', '')
            temp.append(z)
        elif i.startswith('webmail.'):
            z = i.replace('webmail.', '')
            temp.append(z)
        elif i.startswith('.cdn.cloudflare.net'):
            z = i.replace('.cdn.cloudflare.net', '')
            temp.append(z)
        else:
            temp.append(i)
    temp = list(set(temp))
    runner = getHost(thread, web)
    runner.run()