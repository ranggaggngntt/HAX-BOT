from lib.SMTP.getsmtp import GET_SMTP

def main():
    file = input('File: ')
    thread = int(input('Thread: '))
    temp = []
    with open(file, 'r') as f:
        site = f.read().splitlines()
    for url in site:
        if "://" in url:
            temp.append(url)
        else:
            url = "http://"+url
            temp.append(url)
        if url.endswith('/'):
            url = url[:-1]
            temp.append(url)
    runner = GET_SMTP(temp, thread)
    runner.run()