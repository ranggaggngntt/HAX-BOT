from lib.SMTP.getsmtp import GET_SMTP

def main():
    file = input('File: ')
    thread = int(input('Thread: '))
    temp = []
    z = []
    with open(file, 'r') as f:
        site = f.read().splitlines()
    for url in site:
        if "://" in url:
            temp.append(url)
        else:
            url = "http://"+url
            temp.append(url)
    
    for i in temp:
        if i == '':
            pass
        elif i.endswith('/'):
            i = i[:-1]
            z.append(i)
        else:
            z.append(i)
    runner = GET_SMTP(z, thread)
    runner.run()