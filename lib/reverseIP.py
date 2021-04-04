from lib.Reverse.reverse import ReverseIP
from lib.Reverse.proxygrabber import create_proxy

def main():
    ip_file = input('IP List: ')
    thread = int(input('Thread: '))

    with open(ip_file, 'r') as f:
        ip = f.read().splitlines()
    temp = []
    while len(ip) > 50:
        try:
            p = open('proxy.txt', 'a')
            p.truncate(0)
            p.close()
            create_proxy()
            with open('proxy.txt', 'r') as f:
                proxies = f.read().splitlines()
            for i in range(len(proxies)):
                try:
                    temp.append(ip[i])
                except:
                    break

            for i in temp:
                try:
                    ip.remove(i)
                except:
                    pass
            ReverseIP(thread, temp, proxies).run()
            with open('err_ip.txt','r') as f:
                err = f.read().splitlines()
                ip.extend(err)
            err_ip = open('err_ip.txt', 'a')
            err_ip.truncate(0)
            err_ip.close()
            temp.clear()
        except Exception as e:
            print(e)
            exit()